#!/usr/bin/env python3

from xarm.wrapper import XArmAPI
from alphabet import letters
import string
import signal
import sys
from copy import deepcopy
import time
from numpy import add


def sigint_handler(sig, frame):
    print("\nSIGINT Captured, terminating")
    arm.set_state(state=4)
    arm.disconnect()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

letter_functions = {"a": letters.A, "b": letters.B, "c": letters.C, "d": letters.D, "e": letters.E,
                    "f": letters.F, "g": letters.G, "h": letters.H, "i": letters.I, "j": letters.J,
                    "k": letters.K, "l": letters.L, "m": letters.M, "n": letters.N, "o": letters.O,
                    "p": letters.P, "q": letters.Q, "r": letters.R, "s": letters.S, "t": letters.T,
                    "u": letters.U, "v": letters.V, "w": letters.W, "x": letters.X, "y": letters.Y,
                    "z": letters.Z, " ": letters.space, "Invalid": letters.Invalid}
# letter_functions = {letter: letter.upper() for letter in list(string.ascii_lowercase)} #dict of all alphabet letters to call associated functions
# letter_functions["Invalid"] = "Invalid" #add invalid and space functions
# letter_functions[" "] = "space"

# print(letter_functions)

arm = XArmAPI('172.21.72.121', do_not_open=True)
arm.connect()

arm.set_world_offset([0, 0, 0, 0, 0, 0])
time.sleep(0.5)
base_pos = deepcopy(arm.position)
print("base_pos: {}".format(base_pos))
print("world offset: {}".format(arm.world_offset))
arm.set_world_offset([0, 0, 0, base_pos[3], base_pos[4], base_pos[5]])
time.sleep(0.5)
print("world offset: {}".format(arm.world_offset))

arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)


# print("===============================================")
# print("Put robot in writing position, with pen touching the paper")
# print("type ok and hit enter when you're done")
# print("===============================================")

# arm.set_mode(2)
# ok = input()
# while ok != "ok":
#     ok = input()
# arm.set_mode(0)

if len(sys.argv) == 1:
    sentence = input("Enter sentence to write (no special characters)\n")
    sentence = sentence.lower()
else:
    sentence = sys.argv[1]
    sentence = sentence.lower()

to_write = list(sentence)
print("sentence: {}".format(sentence))
# print("letters: {}".format(to_write))


letters.start(arm)

for letter in to_write:
    letter_functions.get(letter, letters.Invalid)(arm)  # calls the function for each letter you want to write
