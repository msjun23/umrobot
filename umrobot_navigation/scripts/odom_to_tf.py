#!/usr/bin/env python

import rospy
import tf2_ros

from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped, Pose, Point, Quaternion, Twist, Vector3

class node:
    def __init__(self):
        rospy.init_node('odom_to_tf', anonymous=True)
        
        rospy.Subscriber('/vins_estimator/odometry', Odometry, self.OdomSubscriber)
        self.odom_pub = rospy.Publisher('/odom', Odometry, queue_size=100)
        
        rospy.spin()
        
    def OdomSubscriber(self, data):
        br = tf2_ros.TransformBroadcaster()
        t = TransformStamped()

        t.header.stamp = data.header.stamp
        t.header.frame_id = "odom"
        t.child_frame_id = "tmp"
        
        t.transform.translation.x = data.pose.pose.position.x
        t.transform.translation.y = data.pose.pose.position.y
        t.transform.translation.z = data.pose.pose.position.z
        
        
        t.transform.rotation.x = data.pose.pose.orientation.x
        t.transform.rotation.y = data.pose.pose.orientation.y
        t.transform.rotation.z = data.pose.pose.orientation.z
        t.transform.rotation.w = data.pose.pose.orientation.w
        
        t2 = TransformStamped()

        t2.header.stamp = data.header.stamp
        t2.header.frame_id = "tmp"
        t2.child_frame_id = "base_footprint"
        
        t2.transform.translation.x = 0
        t2.transform.translation.y = 0
        t2.transform.translation.z = 0.1
        
        
        t2.transform.rotation.x = 0.299
        t2.transform.rotation.y = -0.299
        t2.transform.rotation.z = 0.641
        t2.transform.rotation.w = 0.641
        br.sendTransform(t)
        br.sendTransform(t2)
        
        
        # # next, we'll publish the odometry message over ROS
        # odom = Odometry()
        # odom.header.frame_id = "odom"
        # odom.child_frame_id = "base_footprint"

        # # set the position
        # odom.pose.pose.position.x = data.pose.pose.position.x - 0.225
        # odom.pose.pose.position.y = data.pose.pose.position.y
        # odom.pose.pose.position.z = data.pose.pose.position.z 
        
        # odom.pose.pose.orientation.x = 
        # odom.pose.pose.orientation.y = 
        # odom.pose.pose.orientation.z = 
        # odom.pose.pose.orientation.w = 

        # set the velocity

        # publish the message
        # self.odom_pub.publish(odom)

if __name__ == '__main__':
    n = node()
