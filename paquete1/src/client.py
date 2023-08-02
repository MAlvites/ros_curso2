#!/usr/bin/env python3

import rospy, random
from paquete1.srv import *

if __name__ == "__main__":
    rospy.init_node('distance_caller')
    c_client = rospy.ServiceProxy('distance_shift', SetDistanceSensorShift)
    r = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        a = random.randint(0, 5)
        rospy.loginfo("Pidiendo cambio a %d" % a)
        req = SetDistanceSensorShiftRequest()
        req.distance = a
        resp = c_client(req)
        rospy.loginfo("Respuesta %d %s" % (resp.success, resp.message))
        r.sleep()