#!/usr/bin/env python3

from alphabet import letters_v2
from copy import deepcopy
from numpy import add
from speech_control import speech_recog_v1
from xarm.wrapper import XArmAPI

import signal
import string
import sys
import time
import unicodedata


def sigint_handler(sig, frame):
    print("\nSIGINT Captured, terminating")
    arm.set_state(state=4)
    arm.disconnect()
    sys.exit(0)


# signal.signal(signal.SIGINT, sigint_handler)

letter_functions = {"a": letters_v2.A, "b": letters_v2.B, "c": letters_v2.C, "d": letters_v2.D, "e": letters_v2.E,
                    "f": letters_v2.F, "g": letters_v2.G, "h": letters_v2.H, "i": letters_v2.I, "j": letters_v2.J,
                    "k": letters_v2.K, "l": letters_v2.L, "m": letters_v2.M, "n": letters_v2.N, "o": letters_v2.O,
                    "p": letters_v2.P, "q": letters_v2.Q, "r": letters_v2.R, "s": letters_v2.S, "t": letters_v2.T,
                    "u": letters_v2.U, "v": letters_v2.V, "w": letters_v2.W, "x": letters_v2.X, "y": letters_v2.Y,
                    "z": letters_v2.Z, " ": letters_v2.space, "Invalid": letters_v2.Invalid}
# letter_functions = {letter: letter.upper() for letter in list(string.ascii_lowercase)} #dict of all alphabet letters_v2 to call associated functions
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

sentence = ""
while sentence[:6] != "écris":
    sentence = speech_recog_v1.return_sentence()

sentence = ''.join((c for c in unicodedata.normalize(
    'NFD', sentence) if unicodedata.category(c) != 'Mn'))

to_write = list(sentence)
print("sentence: {}".format(sentence))
# print("letters_v2: {}".format(to_write))


letters_v2.start(arm)

for letter in to_write:
    # calls the function for each letter you want to write
    letter_functions.get(letter, letters_v2.Invalid)(arm)
