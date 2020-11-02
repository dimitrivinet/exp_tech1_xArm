import time
from numpy import add

is_down = True


def start(arm):
    # arm.set_tool_position(z=-5, wait=True, speed=100, mvacc=100) #base, très lent
    # arm.set_tool_position(z=-5, wait=True, speed=300, mvacc=100) #toujours lent
    # arm.set_tool_position(z=-5, wait=True, speed=500, mvacc=500) #un peu plus rapide, acc ok
    # arm.set_tool_position(z=-5, wait=True, speed=10000, mvacc=100000)
    arm.set_tool_position(z=-5, wait=True, speed=10, mvacc=100)

    # test = arm.position
    # print(test)
    # test[2] += 10
    # down_vect = [0, 0, 10, 0, 0, 0]
    # arm.set_position(*list(add(arm.position, down_vect))[:6], wait=True, speed=100, mvacc=100, relative=False)


def Invalid(arm):
    print("invalid")


def space(arm):
    move(arm, [[0, 6, 0, 0, 0, 0, 0, True]])


def move(arm, paths):
    last_pos = arm.position + [0, 0]

    arm.set_pause_time(3)
    for path in paths:
        last_pos = list(add(last_pos[:6], path[:6])) + [0, 0]
        last_pos[6] = path[6]
        last_pos[7] = path[7]
        # print(last_pos)
        ret = arm.set_position(*last_pos[:7], is_radian=False, wait=last_pos[7], speed=5, mvacc=500, relative=False)
        if ret < 0:
            print('set_position, ret={}'.format(ret))
            return -1


def A(arm):

    paths = [  # [x, y, z, roll, pitch, yaw,radius, is_rad, wait]
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 5, 0, 0, 0, 0, 0, False],
        [-10, 5, 0, 0, 0, 0, 0, False],
        [5, -2.5, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, -5, 0, 0, 0, 0, 0, False],
        [-5, 7.5, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]

    move(arm, paths)


def B(arm):

    paths = [  # [x, y, z, roll, pitch, yaw,radius, is_rad, wait]
        [0, 0, 5, 0, 0, 0, 0, True],
        [10, 0, 0, 0, 0, 0, 0, True],
        [0, 5, 0, 0, 0, 0, 5, False],
        [-5, 0, 0, 0, 0, 0, 5, False],
        [0, -6, 0, 0, 0, 0, 5, False],
        [0, 6, 0, 0, 0, 0, 5, False],
        [-5, 0, 0, 0, 0, 0, 5, False],
        [0, -6, 0, 0, 0, 0, 5, False],
        [0, 9, -5, 0, 0, 0, 0, True]
    ]

    move(arm, paths)


def C(arm):
    paths = [
        [9, 8, 0, 0, 0, 0, 0, True],
        [0, 0, 5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)

    posA = arm.position
    posB = list(add(posA, [-3, -8, 0, 0, 0, 0]))
    posC = list(add(posB, [-5, 5, 0, 0, 0, 0]))

    arm.move_circle(posB, posC, percent=70, wait=True)

    move(arm, [[0, 3, -5, 0, 0, 0, 0, True]])


def D(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, True],
        [10, 0, 0, 0, 0, 0, 0, True],
        [0, 7, 0, 0, 0, 0, 7, False],
        [-10, 0, 0, 0, 0, 0, 7, False],
        [0, -7, 0, 0, 0, 0, 0, False],
        [0, 10, -5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def E(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 7, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-5, -7, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 5, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-5, -5, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 7, 0, 0, 0, 0, 0, False],
        [0, 3, -5, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def F(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 7, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-5, -7, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 5, 0, 0, 0, 0, 0, False],
        [-5, 5, -5, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def G(arm):
    posA = arm.position
    paths = [
        [9, 8, 0, 0, 0, 0, 0, True],
        [0, 0, 5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)

    posB = list(add(posA, [5, 0, 5, 0, 0, 0]))
    posC = list(add(posA, [0, 5, 5, 0, 0, 0]))

    arm.move_circle(posB, posC, percent=60, wait=True)

    paths = [
        [0, 3, 0, 0, 0, 0, 0, True],
        [3.5, 0, 0, 0, 0, 0, 0, True],
        [0, -3, 0, 0, 0, 0, 0, True],
        [-3.5, 6, -5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def H(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [-5, 0, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 7, 0, 0, 0, 0, 0, False],
        [5, 0, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def I(arm):
    paths = [
        [0, 3, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [7, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [3, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 4, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def J(arm):
    paths = [
        [10, 6, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 3, False],
        [0, -6, 0, 0, 0, 0, 0, False],
        [0, 9, -5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def K(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [-5, 0, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [5, 5, 0, 0, 0, 0, 0, False],
        [-5, -5, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-5, 5, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def L(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 0, False],
        [0, 6, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def M(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [-5, 5, 0, 0, 0, 0, 0, False],
        [5, 5, 0, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def N(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [-10, 6, 0, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def O(arm):
    posA = arm.position
    paths = [
        [0, 5, 0, 0, 0, 0, 0, True],
        [0, 0, 5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)

    posB = list(add(posA, [10, 5, 5, 0, 0, 0]))
    posC = list(add(posA, [5, 0, 5, 0, 0, 0]))

    arm.move_circle(posB, posC, percent=100, wait=True)

    paths = [
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 8, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def P(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 5, 0, 0, 0, 0, 3, False],
        [-5, 0, 0, 0, 0, 0, 3, False],
        [0, -5, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-5, 8, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def Q(arm):
    posA = arm.position
    paths = [
        [0, 5, 0, 0, 0, 0, 0, True],
        [0, 0, 5, 0, 0, 0, 0, True]
    ]
    move(arm, paths)

    posB = list(add(posA, [10, 5, 5, 0, 0, 0]))
    posC = list(add(posA, [5, 0, 5, 0, 0, 0]))

    arm.move_circle(posB, posC, percent=100, wait=True)

    paths = [
        [0, 0, -5, 0, 0, 0, 0, False],
        [4, 1, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-4, 4, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def R(arm):
    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 5, 0, 0, 0, 0, 3, False],
        [-5, 0, 0, 0, 0, 0, 3, False],
        [0, -5, 0, 0, 0, 0, 0, False],
        [-5, 5, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def S(arm):
    paths = [
        [10, 6, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, -6, 0, 0, 0, 0, 5, False],
        [-5, 0, 0, 0, 0, 0, 5, False],
        [0, 6, 0, 0, 0, 0, 5, False],
        [-5, 0, 0, 0, 0, 0, 5, False],
        [0, -6, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 9, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def T(arm):
    paths = [
        [10, 8, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [10, -4, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, 8, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


def U(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 0, 0, 0, 0, 0, 3, False],
        [0, 6, 0, 0, 0, 0, 3, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def V(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 4, 0, 0, 0, 0, 0, False],
        [10, 4, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def W(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, False],
        [4, 3, 0, 0, 0, 0, 0, False],
        [-4, 3, 0, 0, 0, 0, 0, False],
        [10, 3, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [-10, 3, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def X(arm):
    paths = [
        [10, 7, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, -7, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-10, 7, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def Y(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-4, 4, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [4, 4, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [-4, -4, 0, 0, 0, 0, 0, False],
        [-6, 0, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 7, 0, 0, 0, 0, 0, True],
    ]
    move(arm, paths)


def Z(arm):
    paths = [
        [10, 0, 0, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False], 
        [0, 8, 0, 0, 0, 0, 0, False],
        [-10, -8, 0, 0, 0, 0, 0, False],
        [0, 8, 0, 0, 0, 0, 0, False],
        [0, 0, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]
    move(arm, paths)


# arm.set_tool_position(x=, y=, wait=True)
# [0, 0, 0, 0, 0, 0, 0, False],
