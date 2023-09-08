#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

k=1

if __name__ == "__main__":
    rospy.init_node('move_rectangle')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    msg = Twist()
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        for i in range(0,120):
            #Translation
            if(i>=0 and i<25):
                msg.linear.x = 0.1
                msg.angular.z = 0.0
                pub.publish(msg)
            #Rotation
            elif (i>=25 and i<75):
                msg.linear.x = 0.0
                msg.angular.z = 0.31415926535  
                pub.publish(msg)
            #Translation
            elif(i>=75 and i<100):
                msg.linear.x = 0.1
                msg.angular.z = 0.0
                pub.publish(msg)
            #Rotation
            elif (i>=100 and i<150):
                msg.linear.x = 0.0
                msg.angular.z = 0.31415926535  
                pub.publish(msg)
            #Translation
            elif(i>=150 and i<175):
                msg.linear.x = 0.1
                msg.angular.z = 0.0
                pub.publish(msg)
            #Rotation
            elif (i>=175 and i<225):
                msg.linear.x = 0.0
                msg.angular.z = 0.31415926535 
                pub.publish(msg)
            #Translation
            elif(i>=225 and i<250):
                msg.linear.x = 0.1
                msg.angular.z = 0.0
                pub.publish(msg)
            #Rotation
            else:
                msg.linear.x = 0.0
                msg.angular.z = 0.31415926535 
                pub.publish(msg)
            r.sleep()
            