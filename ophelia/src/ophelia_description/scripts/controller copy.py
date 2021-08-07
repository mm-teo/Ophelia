#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#from actionlib_msgs.msg import GoalID
from pynput import keyboard


time = {'time': '123'}
pub = rospy.Publisher('chatter', String, queue_size=1)
		     #data_class=GoalID,
                     # queue_size=1)

rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(50)

def talker(command):
  msg = String()
#  msg = GoalID()
#  msg.id = command
  msg.stamp = rospy.Time.now()
  pub.publish(msg)
  rate.sleep()

def on_press(key):
  try:
    if format(key.char)=="w":
      print("avanti")
      talker(format(key.char))
    elif format(key.char)=="x":
      print("indietro")
      talker(format(key.char))
    elif format(key.char)=="s":
      print("stop")
      talker(format(key.char))
    elif format(key.char)=="a":
      print("sinistra")
      talker(format(key.char))
    elif format(key.char)=="d":
      print("destra")
      talker(format(key.char))
    elif format(key.char)=="q":
      print("ruota sinistra")
      talker(format(key.char))
    elif format(key.char)=="e":
      print("ruota destra")
      talker(format(key.char))
    elif format(key.char)=="z":
      print("alza")
      talker(format(key.char))
    elif format(key.char)=="c":
      print("abbassa")
      talker(format(key.char))
    elif format(key.char)=="j":
      print("alza")
      talker(format(key.char))
    elif format(key.char)=="l":
      print("abbassa")
      talker(format(key.char))
    elif format(key.char)=="k":
      print("abbassa")
      talker(format(key.char))
    
      

  except AttributeError:
    print('special key {0} pressed'.format(key))

def on_release(key):
  if key == keyboard.Key.esc:
    return False

while not rospy.is_shutdown():
  with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
