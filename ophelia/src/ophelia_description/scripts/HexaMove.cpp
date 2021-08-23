#include <math.h>
#include <stdio.h>

#include "ros/ros.h"
#include "std_msgs/Header.h"
#include "std_msgs/String.h"
#include "sensor_msgs/JointState.h"

typedef struct
{
	int *firstStep;
	float *x, *y;
	float *x1, *y1, *z1;
	float *x2, *y2, *z2;
	float *z, *z3;
} Coordinates;

typedef struct
{
	std::vector<double> joints = std::vector<double>(18, 0);
	/*
	dx_a_1, dx_f_1, dx_t_1;
	dx_a_2, dx_f_2, dx_t_2;
	dx_a_3, dx_f_3, dx_t_3;
	sx_a_1, sx_f_1, sx_t_1;
	sx_a_2, sx_f_2, sx_t_2;
	sx_a_3, sx_f_3, sx_t_3;
	*/
} Position;

typedef struct
{
	float anca;
	float femore;
	float tibia;
} Joint;

Position position;
Joint joint = {.anca=49.8, .femore=76.2, .tibia=136.4};
ros::Publisher pub;

void jointPosition(double output[], double x, double y, double z)
{
	//joint1
	output[0] = atan(y/x);
	
	//joint2
	double l1 = sqrt(pow(x,2)+pow(y,2))-joint.anca;
	double l2 = sqrt(pow(l1,2)+pow(z,2));
	double a1 = asin(l1/l2);
	double a2 = acos((pow(joint.femore,2)-pow(joint.tibia,2)+pow(l2,2))/(2*joint.femore*l2));
	output[1] = (a1+a2)-(M_PI/2);

	//joint3
	double temp = pow(joint.tibia, 2)+pow(joint.femore, 2)-pow(x, 2)-pow(y, 2)-pow(joint.anca, 2)-pow(z, 2)+(2*joint.anca*sqrt(pow(x, 2)+pow(y, 2)));
	double b = acos(temp/(2*joint.femore*joint.tibia));
	output[2] = -((M_PI/2)-b);
}

void moving(Position position)
{
	ros::Rate rate(200);
	sensor_msgs::JointState joint_msg;
	joint_msg.header = std_msgs::Header();
	joint_msg.name = {"anca_dx_1_joint", "femore_dx_1_joint", "tibia_dx_1_joint",
			  			"anca_dx_2_joint", "femore_dx_2_joint", "tibia_dx_2_joint",
						"anca_dx_3_joint", "femore_dx_3_joint", "tibia_dx_3_joint",
			  			"anca_sx_1_joint", "femore_sx_1_joint", "tibia_sx_1_joint",
                        "anca_sx_2_joint", "femore_sx_2_joint", "tibia_sx_2_joint",
			  			"anca_sx_3_joint", "femore_sx_3_joint", "tibia_sx_3_joint"};
	joint_msg.position = position.joints;
	joint_msg.velocity = {};
	joint_msg.effort = {};
	joint_msg.header.stamp = ros::Time::now();

	pub.publish(joint_msg);
	rate.sleep();
}

void avantiPrimaParte(Coordinates coord)
{
	double jointRes[3];

	jointPosition(jointRes, *coord.x1, *coord.y1, *coord.z);
	position.joints[0] = jointRes[0];
	position.joints[1] = jointRes[1];
	position.joints[2] = jointRes[2];

	jointPosition(jointRes, *coord.x, *coord.y, *coord.z1);
	position.joints[3] = jointRes[0];
	position.joints[4] = jointRes[1];
	position.joints[5] = jointRes[2];

	jointPosition(jointRes, *coord.x2, *coord.y1, *coord.z);
	position.joints[6] = -jointRes[0];
	position.joints[7] = jointRes[1];
	position.joints[8] = jointRes[2];

	jointPosition(jointRes, -*coord.x2, *coord.y1, *coord.z2);
	position.joints[9] = jointRes[0];
	position.joints[10] = -jointRes[1];
	position.joints[11] = -jointRes[2];

	jointPosition(jointRes, *coord.x, *coord.y, *coord.z);
	position.joints[12] = -jointRes[0];
	position.joints[13] = -jointRes[1];
	position.joints[14] = -jointRes[2];

	jointPosition(jointRes, -*coord.x1, *coord.y1, *coord.z2);
	position.joints[15] = jointRes[0];
	position.joints[16] = -jointRes[1];
	position.joints[17] = -jointRes[2];

	moving(position);
	*coord.y = *coord.y-1;
	*coord.x1 = *coord.x1-(1/sqrt(2));
	*coord.x2 = *coord.x2+(1/sqrt(2));
	*coord.y1 = -*coord.x1+135;
	*coord.z1 = -(*coord.y*(*coord.y)*0.01875+100);
	*coord.z2 = -0.0375*pow(*coord.x1-135, 2)-100;
}

extern "C"
{
	void shutdownPublisher()
	{
		ros::shutdown();
	}

	void initPublisher()
	{
		ros::init(std::map<std::string, std::string>(), "joint_state_publisher");
		ros::NodeHandle n;
		pub = n.advertise<sensor_msgs::JointState>("/joint_states", 1);
	}

	void alza(Coordinates coord)
	{
		double dx_aft[3];
		while (*coord.z > -130)
		{
			jointPosition(dx_aft, *coord.x, *coord.y, *coord.z);

			for (int i=0; i<3; i++)
			{
				position.joints[0+i*3] = dx_aft[0];
				position.joints[1+i*3] = dx_aft[1];
				position.joints[2+i*3] = dx_aft[2];
			}

			for (int i=3; i<6; i++)
			{
				position.joints[0+i*3] = dx_aft[0];
				position.joints[1+i*3] = -dx_aft[1];
				position.joints[2+i*3] = -dx_aft[2];
			}

			moving(position);
			*coord.z -= 1;
		}
	}

	void avanti(Coordinates coord)
	{
		double jointRes[3];

		*coord.z3 = *coord.z;
		if (*coord.firstStep == 1)
		{
			while (*coord.z3 < -100)
			{
				jointPosition(jointRes, *coord.x, *coord.y, *coord.z3);

				position.joints[3] = jointRes[0];
				position.joints[4] = jointRes[1];
				position.joints[5] = jointRes[2];

				position.joints[9] = jointRes[0];
				position.joints[10] = -jointRes[1];
				position.joints[11] = -jointRes[2];

				position.joints[15] = jointRes[0];
				position.joints[16] = -jointRes[1];
				position.joints[17] = -jointRes[2];

				moving(position);
				*coord.z3 += 1;
			}
		}

		*coord.firstStep = 0;
		*coord.z1 = *coord.z3;
		*coord.z2 = *coord.z3;

		while (*coord.y > -40)
		{
			avantiPrimaParte(coord);
		}

		while (*coord.y < 40)
		{
			jointPosition(jointRes, *coord.x1, *coord.y1, *coord.z2);
			position.joints[0] = jointRes[0];
			position.joints[1] = jointRes[1];
			position.joints[2] = jointRes[2];

			jointPosition(jointRes, *coord.x, *coord.y, *coord.z);
			position.joints[3] = jointRes[0];
			position.joints[4] = jointRes[1];
			position.joints[5] = jointRes[2];

			jointPosition(jointRes, *coord.x2, *coord.y1, *coord.z2);
			position.joints[6] = -jointRes[0];
			position.joints[7] = jointRes[1];
			position.joints[8] = jointRes[2];

			jointPosition(jointRes, -*coord.x2, *coord.y1, *coord.z);
			position.joints[9] = jointRes[0];
			position.joints[10] = -jointRes[1];
			position.joints[11] = -jointRes[2];

			jointPosition(jointRes, *coord.x, *coord.y, *coord.z1);
			position.joints[12] = -jointRes[0];
			position.joints[13] = -jointRes[1];
			position.joints[14] = -jointRes[2];

			jointPosition(jointRes, -*coord.x1, *coord.y1, *coord.z);
			position.joints[15] = jointRes[0];
			position.joints[16] = -jointRes[1];
			position.joints[17] = -jointRes[2];

			moving(position);
			*coord.y = *coord.y+1;
			*coord.x1 = *coord.x1+(1/sqrt(2));
			*coord.x2 = *coord.x2-(1/sqrt(2));
			*coord.y1 = -*coord.x1+135;
			*coord.z1 = -(*coord.y*(*coord.y)*0.01875+100);
			*coord.z2 = -0.0375*pow(*coord.x1-135, 2)-100;
		}
	}


	void avantiUscita(Coordinates coord)
	{
		double jointRes[3];

		*coord.firstStep = 1;
		while (*coord.y > 0)
		{
			avantiPrimaParte(coord);
		}

		while (*coord.z2 > -130)
		{
			jointPosition(jointRes, *coord.x, *coord.y, *coord.z2);

			position.joints[3] = jointRes[0];
			position.joints[4] = jointRes[1];
			position.joints[5] = jointRes[2];

			position.joints[9] = jointRes[0];
			position.joints[10] = -jointRes[1];
			position.joints[11] = -jointRes[2];

			position.joints[15] = jointRes[0];
			position.joints[16] = -jointRes[1];
			position.joints[17] = -jointRes[2];

			moving(position);
			*coord.z2 -= 1;
		}
	}
}


