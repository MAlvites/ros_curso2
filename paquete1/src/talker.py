#!/usr/bin/env python3

import rospy
from paquete1.msg import DistanceSensorStatus

if __name__ == '__main__':
    rospy.init_node('distance_talker')
    pub = rospy.Publisher('distance', DistanceSensorStatus, queue_size = 1)
    rate = rospy.Rate(10)
    cur_status = 1
    cur_f = 0.0
    
    while not rospy.is_shutdown():
        c = DistanceSensorStatus()
        c.status = cur_status
        c.distance = cur_f
        rospy.loginfo((cur_status, cur_f))
        pub.publish(c)
        rate.sleep()
        cur_status = 1 - cur_status
        cur_f += 0.01 