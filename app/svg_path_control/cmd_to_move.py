#!/usr/bin/env python3

import queue
import time
from numpy import add

command_queue = queue.Queue()

def start(arm):
    arm.set_tool_position(z=-5, wait=True, speed=10, mvacc=100)

def space(arm):
    return [[0, 6, 0, 0, 0, 0, 0, True]]


def move(arm):
    count = 0
    #start(arm)
    base_pos = arm.position
    goal_pos = base_pos.copy()

    while True:
        time.sleep(0.05)
        if not command_queue.empty():
            path = command_queue.get(block = False)          

            goal_pos[:3] = list(add(base_pos[:3], path[:3]))

            # print(goal_pos)

            ret = arm.set_position(*goal_pos[:6], radius=0, is_radian=False, wait=False, relative=False,)
            if ret < 0:
                print('set_position, ret={}'.format(ret))
                return -1

            command_queue.task_done()
            # print(count)
            count += 1
        else:
            pass