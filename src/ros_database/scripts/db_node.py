#!/usr/bin/env python2.7
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
import json
import mysql.connector

def db_cmd_callback(data):
  cmd, place = (data.data).split(",")

  if (cmd == "add"):
    data_add(place)
  elif (cmd == "remove"):
    data_remove(place)
  elif (cmd == "go"):
    go_to(place)

def pose_callback(data):
  global pose
  pose = data.pose.pose

def pose_to_dict(msg):
  pose_dict = {
    'position': {
        'x': msg.position.x,
        'y': msg.position.y,
        'z': msg.position.z
      },
    'orientation': {
        'x': msg.orientation.x,
        'y': msg.orientation.y,
        'z': msg.orientation.z,
        'w': msg.orientation.w
    }
  }
  return pose_dict

def json_to_pose(json_str):
  pose_dict = json.loads(json_str)
  pose_msg = PoseStamped()
  pose_msg.pose.position.x = pose_dict['position']['x']
  pose_msg.pose.position.y = pose_dict['position']['y']
  pose_msg.pose.position.z = pose_dict['position']['z']
  pose_msg.pose.orientation.x = pose_dict['orientation']['x']
  pose_msg.pose.orientation.y = pose_dict['orientation']['y']
  pose_msg.pose.orientation.z = pose_dict['orientation']['z']
  pose_msg.pose.orientation.w = pose_dict['orientation']['w']
  pose_msg.header.frame_id = "map"
  return pose_msg

def data_add(place):
  my_cursor = mydb.cursor()
  pose_dict = pose_to_dict(pose)
  pose_string = json.dumps(pose_dict)

  sqlStuff = "INSERT INTO places (place, pose) VALUES (%s, %s)"
  record = (place, pose_string)

  my_cursor.execute(sqlStuff,record)
  mydb.commit()

def data_remove(place):
  my_cursor = mydb.cursor()
  my_sql = "DELETE FROM places WHERE place = %s" 
  val = (place,)
  my_cursor.execute(my_sql, val)
  mydb.commit()

def go_to(place):
  my_cursor = mydb.cursor()
  my_sql = "SELECT * FROM places WHERE place = %s"
  val = (place,)
  my_cursor.execute(my_sql,val)
  result = my_cursor.fetchall()
  print(result[0][2])
  pose = json_to_pose(result[0][2])
  print(pose)
  pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
  pub.publish(pose)

def db_to_string():
  my_cursor = mydb.cursor()
  my_cursor.execute("SELECT * FROM places")
  result = my_cursor.fetchall()
  db_string =""
  for row in result:
      db_string += row[1]+","

  return db_string.strip(",")

def db_listener():
  rospy.init_node('db_node', anonymous=True)
  
  rospy.Subscriber("db_cmd", String, db_cmd_callback)
  rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped,pose_callback)
  
  try:
    db_talker()
  except rospy.ROSInterruptException:
    pass
  
  rospy.spin()

def db_talker():
  pub = rospy.Publisher('database', String, queue_size=10)
  
  rate = rospy.Rate(10) # 10hz
  
  while not rospy.is_shutdown():
    db_string = db_to_string()
    pub.publish(db_string)
    rate.sleep()
   
if __name__ == '__main__':

  mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "diyazen123",
    database = "rosdb" ,
  ) 

  db_listener()

  
