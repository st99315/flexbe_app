#!/usr/bin/env python3

import os, sys, math
from math import pi, radians
import numpy as np
import json
import argparse
import time

import rospy, rospkg
from std_msgs.msg import String
from std_msgs.msg import Empty

def init(path):
    try:
        with open(path + '/src/default.json','r') as f:
            js = json.load(f)
        class args:
            pass
        args.project = str(js["project"])
        # msg = ""

        if args.project == "default":
            pass
        else:
            pub = rospy.Publisher('/flexbe/web/call_bevavior', String, queue_size=0)
            time.sleep(1)           #wait for flexbe app open
            msg = args.project
            pub.publish(msg)
            pass
    except Exception as e:
        args1 = {}
        args1["project"] = str("default")
        # args1["project"] = str("default")
        with open(path + '/src/default.json', 'w') as outfile:
            json.dump(args1, outfile, indent= 4)
        with open(path + '/src/default.json','r') as f:
            js = json.load(f)
   

    return js

def save_project(data):
    path = rospack.get_path('flexbe_app')

    args1["project"] = str(data.data)

    with open(path + '/src/default.json', 'w') as outfile:
        json.dump(args1, outfile, indent= 4)

def start_init(data):
    args1 = init(rospack.get_path('flexbe_app'))

rospack = rospkg.RosPack()


if __name__ == '__main__' :
    rospy.init_node('flexbe_load_project')
    args1 = {}#init(rospack.get_path('flexbe_app'))
    rospy.Subscriber("/flexbe_open/ready", Empty, start_init)
    rospy.Subscriber("/flexbe_save/commend", String, save_project)
    rospy.spin()