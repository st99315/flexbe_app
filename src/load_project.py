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
    get_states_list()

def get_states_list():
    statelib = []
    # states in solomon_flexbe_states
    state_path = rospack.get_path('solomon_flexbe_states')
    statelist = os.listdir(state_path + '/src/solomon_flexbe_states/')
    for files in statelist:
        filename = files.split('.py')
        if len(filename) > 1 and filename[0]!='__init__':
            statelib.append(filename[0])
            # print(filename)

    # states in flexbe_states
    state_path = rospack.get_path('flexbe_states')
    statelist = os.listdir(state_path + '/src/flexbe_states/')
    for files in statelist:
        filename = files.split('.py')
        if len(filename) > 1 and filename[0]!='__init__':
            statelib.append(filename[0])

    # states in flexbe_manipulation_states
    state_path = rospack.get_path('flexbe_manipulation_states')
    statelist = os.listdir(state_path + '/src/flexbe_manipulation_states/')
    for files in statelist:
        filename = files.split('.py')
        if len(filename) > 1 and filename[0]!='__init__':
            statelib.append(filename[0])

    # states in flexbe_navigation_states
    state_path = rospack.get_path('flexbe_navigation_states')
    statelist = os.listdir(state_path + '/src/flexbe_navigation_states/')
    for files in statelist:
        filename = files.split('.py')
        if len(filename) > 1 and filename[0]!='__init__':
            statelib.append(filename[0])

    # states in flexbe_utility_states
    state_path = rospack.get_path('flexbe_utility_states')
    statelist = os.listdir(state_path + '/src/flexbe_utility_states/')
    for files in statelist:
        filename = files.split('.py')
        if len(filename) > 1 and filename[0]!='__init__':
            statelib.append(filename[0])

    rospy.set_param("/statelib",statelib)

rospack = rospkg.RosPack()


if __name__ == '__main__' :
    rospy.init_node('flexbe_load_project')
    args1 = {}#init(rospack.get_path('flexbe_app'))
    rospy.Subscriber("/flexbe_open/ready", Empty, start_init)
    rospy.Subscriber("/flexbe_save/commend", String, save_project)
    rospy.spin()