#!/usr/bin/env python3

import rospy
from paquete1.msg import DistanceSensorStatus

def callback(data):
    rospy.loginfo('I heard %d %f', data.status, data.distance)

if __name__ == '__main__':
    rospy.init_node('distance_listener')
    rospy.Subscriber('distance', DistanceSensorStatus, callback)
    rospy.spin()
    print("node terminated")