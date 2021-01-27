#!/usr/bin/env python3

from alphabet import letters_v3
from copy import deepcopy
from numpy import add
from xarm.wrapper import XArmAPI
from speech_control import speech_recog_v1

import signal
import string
import sys
import threading
import time
import unicodedata

finished = True


def exit(arm):
    print("exiting...")
    time.sleep(0.5)
    arm.set_state(state=4)
    arm.disconnect()
    sys.exit(0)

def sigint_handler(sig, frame):
    print("\nSIGINT Captured, terminating")
    arm.set_state(state=4)
    arm.disconnect()
    sys.exit(0)

def write(to_write):
    paths = list()
    # letters_v3.start(arm)
    for letter in to_write:
        # print(letter)
        paths.append(letter_functions.get(letter, letters_v3.Invalid)(arm))

    arm.set_pause_time(1, False)

    # print(paths)

    for path in paths:
        # print(path)
        for pos in path:
            letters_v3.command_queue.put(pos)
            # print(pos)

    letters_v3.command_queue.join()

    arm.set_position(0, 0, 0, 0, 0, 0, 0, is_radian=False, wait=True, speed=5, mvacc=500, relative=True)

    return True
    # print(paths)



signal.signal(signal.SIGINT, sigint_handler)

letter_functions = {"a": letters_v3.A, "b": letters_v3.B, "c": letters_v3.C, "d": letters_v3.D, "e": letters_v3.E,
                    "f": letters_v3.F, "g": letters_v3.G, "h": letters_v3.H, "i": letters_v3.I, "j": letters_v3.J,
                    "k": letters_v3.K, "l": letters_v3.L, "m": letters_v3.M, "n": letters_v3.N, "o": letters_v3.O,
                    "p": letters_v3.P, "q": letters_v3.Q, "r": letters_v3.R, "s": letters_v3.S, "t": letters_v3.T,
                    "u": letters_v3.U, "v": letters_v3.V, "w": letters_v3.W, "x": letters_v3.X, "y": letters_v3.Y,
                    "z": letters_v3.Z, " ": letters_v3.space, "Invalid": letters_v3.Invalid}

arm = "dummy"
connected = False
while not connected:
    try:
        arm = XArmAPI('172.21.72.250', do_not_open=True)
        arm.connect()
        connected = True
    except:
        print("arm is not online. trying again in 3 seconds...")
        time.sleep(3)


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

arm.set_tool_position(z=-5, wait=True, speed=10, mvacc=100)

threading.Thread(target=letters_v3.move, args=(arm,), daemon=True).start()

while True:
    if finished is True:

        print("\n=================================================\n")

        if input("\nLancer une reconnaissance vocale ? (y/n)") == "y":
            sentence = ""
            rep = ""
            while rep != "ok":
                sentence = speech_recog_v1.return_sentence()
                sentence = sentence.split("écri")
                try:
                    print("to write: {}".format(sentence[1][2:]))
                    rep = input("ok pour continuer, autre pour réessayer\n")
                except:
                    print("erreur: utiliser le mot clé 'écris' pour faire écrire le robot")
                    try_again = input("recommencer? (y/n)")

                    if try_again != "y":
                        exit(arm)
                    else:
                        time.sleep(0.5)

            sentence = ''.join((c for c in unicodedata.normalize(
                'NFD', sentence[1][2:]) if unicodedata.category(c) != 'Mn'))

            to_write = list(sentence)
            print("writing: {}".format(sentence))
            
            finished = False
            finished = write(to_write)

        else:
            exit(arm)
            