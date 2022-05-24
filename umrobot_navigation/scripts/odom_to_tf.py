#!/usr/bin/env python

import rospy
import tf2_ros

from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

class node:
    def __init__(self):
        rospy.init_node('odom_to_tf', anonymous=True)
        
        rospy.Subscriber('/vins_estimator/odometry', Odometry, self.OdomSubscriber)
        
        rospy.spin()
        
    def OdomSubscriber(self, data):
        br = tf2_ros.TransformBroadcaster()
        t = TransformStamped()

        t.header.stamp = rospy.Time.now()
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

        t2.header.stamp = rospy.Time.now()
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
        #t*t2

if __name__ == '__main__':
    n = node()
