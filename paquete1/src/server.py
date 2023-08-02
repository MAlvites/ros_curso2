#!/usr/bin/env python3

import rospy
from paquete1.srv import *

shift_val = 0.0

def callback(req):
    global shift_val

    rospy.loginfo("Cambiando distancia a %f" % req.distance)
    shift_val = req.distance

    resp = SetDistanceSensorShiftResponse()
    resp.success = True
    resp.message = "cambio realizado"
    return resp

if __name__ == "__main__":
    rospy.init_node('distance_server')
    rospy.Service('distance_shift', SetDistanceSensorShift, callback)
    cur_f = 0.0
    r = rospy.Rate(10)
    
    while (not rospy.is_shutdown()):
        cur_f += 0.01
        r.sleep()