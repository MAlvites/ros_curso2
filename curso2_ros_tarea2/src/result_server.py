#!/usr/bin/env python3

import rospy
from curso2_ros_tarea2.srv import *

def callback(req):
    resp = SumComparisonResponse()
    if req.enable == True:
        resp.c = req.a + req.b
        if resp.c>10:
            resp.message = "Es mayor que 10"
        elif resp.c<10:
            resp.message = "Es menor que 10"
        else:
            resp.message = "Es igual que 10"
    else:
        resp.message = "No esta habilitado"
        resp.c = 0

    c = resp.c
    rospy.loginfo(resp.message + " y el resultado es %d" , c)
    return resp

if __name__ == "__main__":
    rospy.init_node('res_number')
    rospy.Service('sum_compare', SumComparison, callback)
    rate = rospy.Rate(10)
    
    while (not rospy.is_shutdown()):
        rate.sleep()