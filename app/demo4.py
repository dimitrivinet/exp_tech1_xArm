#!/usr/bin/env python3

from copy import deepcopy
from numpy import add
from xarm.wrapper import XArmAPI
from svg_path_control import cmd_to_move, svg_path_to_cmd

import signal
import sys
import threading
import time
import numpy as np


def sigint_handler(sig, frame):
    print("\nSIGINT Captured, terminating")
    arm.set_state(state=4)
    arm.disconnect()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

try:
    arm = XArmAPI('172.21.72.250', do_not_open=True)
    arm.connect()

    arm.set_world_offset([0, 0, 0, 0, 0, 0])
    time.sleep(0.5)
    base_pos = deepcopy(arm.position)
    print("base_pos: {}".format(base_pos))
    print("world offset: {}".format(arm.world_offset))
    arm.set_world_offset([0, 0, 0, -179.7, base_pos[4], base_pos[5]])
    time.sleep(0.5)
    print("world offset: {}".format(arm.world_offset))

    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)
except:
    print("arm not connected")
    pass


if len(sys.argv) == 1:
    filename = input("\nEnter file name:\n")
else:
    filename = sys.argv[1]

coords = np.array(svg_path_to_cmd.get_points_coords(
    svg_path_to_cmd.get_path_dict(filename), 5), dtype=object)

coords = coords/10


# for coord in coords:
#     print(coord)
#     print("\n")


try:
    threading.Thread(target=cmd_to_move.move, args=(arm,), daemon=True).start()
except:
    pass


speed = 10 # < 250
acc = 10*speed

arm.set_tool_position(0, 0, -5, 0, 0, 0, is_radian=False, wait=True, relative=True, speed=speed, mvacc=acc,) #start e.g. lift pen up
for coord in coords:
    print(coord)
    for i in range(len(coord[0])):
        cmd = [coord[0,i], coord[1,i], -5 if coord[2,i] != 0 else 0]
        cmd_to_move.command_queue.put(cmd)


cmd_to_move.command_queue.join()


while arm.get_cmdnum()[1] != 0:
    time.sleep(0.1)

try:
    print("\nstopping\n")
    arm.set_position(0, 0, 0, 0, 0, 0, is_radian=False, wait=True, relative=True,)
    arm.set_state(state=4)
    arm.disconnect()
except:
    pass


