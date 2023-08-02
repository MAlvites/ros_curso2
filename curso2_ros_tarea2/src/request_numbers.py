#!/usr/bin/env python3

import rospy, random
from curso2_ros_tarea2.srv import *

if __name__ == "__main__":
    rospy.init_node('req_numbers')
    c_client = rospy.ServiceProxy('sum_compare', SumComparison)
    r = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        a = random.randint(1, 8)
        b = random.randint(1, 8)
        enable=bool(random.randint(0, 5))
        rospy.loginfo("Enviado los numeros %d, %d, enable %s" % (a, b, str(enable)))
        req = SumComparisonRequest()
        req.a = a
        req.b = b
        req.enable = enable
        resp = c_client(req)
        rospy.loginfo("Respuesta %d, %s" % (resp.c, resp.message))
        r.sleep()