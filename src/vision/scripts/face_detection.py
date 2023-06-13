#!/usr/bin/env python2.7
# license removed for brevity
import rospy
from std_msgs.msg import String
import cv2 
import face_recognition

port = 0
    
def talker():
  pub = rospy.Publisher('face_detection', String, queue_size=10)
  rospy.init_node('face_detection', anonymous=True)
  rate = rospy.Rate(10) # 10hz
  cap  = cv2.VideoCapture(port)
  while not rospy.is_shutdown():
    success, img = cap.read()
    if success:
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      encoded_faces = face_recognition.face_encodings(img)
      if len(encoded_faces) > 0:
        pub.publish("Faces detected")
      else:
        pub.publish("No faces detected")
    rate.sleep()
   
if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass