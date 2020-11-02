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
    pass


def up(arm):
    arm.set_tool_position(z=-5, wait=True)


def down(arm):
    arm.set_tool_position(z=5, wait=True)


def next(arm):
    arm.set_tool_position(y=1, wait=True)


def space(arm):
    arm.set_tool_position(y=7, wait=True)


def A(arm):
    # down(arm)
    # arm.set_tool_position(x=10, y=5, wait=True)
    # arm.set_tool_position(x=-10, y=5, wait=True)
    # up(arm)
    # arm.set_tool_position(x=5, y=-2.5, wait=True)
    # down(arm)
    # arm.set_tool_position(x=0, y=-5, wait=True)
    # up(arm)
    # arm.set_tool_position(x=-5, y=7.5, wait=True)

    # next(arm)

    paths = [
        [0, 0, 5, 0, 0, 0, 0, False],
        [10, 5, 0, 0, 0, 0, 0, False],
        [-10, 5, 0, 0, 0, 0, 0, False],
        [5, -2.5, -5, 0, 0, 0, 0, False],
        [0, 0, 5, 0, 0, 0, 0, False],
        [0, -5, 0, 0, 0, 0, 0, False],
        [-5, 7.5, -5, 0, 0, 0, 0, False],
        [0, 3, 0, 0, 0, 0, 0, True]
    ]

    last_pos = arm.position + [0, 0]

    arm.set_pause_time(1)
    for path in paths:
        last_pos = list(add(last_pos[:6], path[:6]))
        last_pos[6] = path[6]
        last_pos[7] = path[7]
        # print(last_pos)
        ret = arm.set_position(*last_pos[:7], is_radian=False, wait=last_pos[7], speed=10, mvacc=500, relative=False)
        if ret < 0:
            print('set_position, ret={}'.format(ret))
            return -1


def B(arm):
    # arm.set_tool_position(x=10, y=0, wait=True)
    # down(arm)
    # arm.set_tool_position(x=-10, y=0, wait=True)
    # up(arm)
    # arm.set_tool_position(x=10, y=0, wait=True)
    # down(arm)
    # arm.set_tool_position(x=0, y=4, wait=True)
    # arm.set_tool_position(x=-5, y=0, wait=True)
    # arm.set_tool_position(x=0, y=-4, wait=True)
    # arm.set_tool_position(x=0, y=6, wait=True)
    # arm.set_tool_position(x=-5, y=0, wait=True)
    # arm.set_tool_position(x=0, y=-6, wait=True)
    # up(arm)
    # arm.set_tool_position(x=0, y=6, wait=True)

    # next(arm)

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

    last_pos = arm.position + [0, 0]

    arm.set_pause_time(1)
    for path in paths:
        last_pos = list(add(last_pos[:6], path[:6])) + [0, 0]
        last_pos[6] = path[6]
        last_pos[7] = path[7]
        # print(last_pos)
        ret = arm.set_position(*last_pos[:7], is_radian=False, wait=last_pos[7], speed=10, mvacc=500, relative=False)
        if ret < 0:
            print('set_position, ret={}'.format(ret))
            return -1
    arm.set_position(*last_pos[:7], is_radian=False, wait=last_pos[7], speed=10, mvacc=500, relative=False)


def C(arm):
    arm.set_tool_position(x=10, y=7, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=-7, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=7, wait=True)
    up(arm)

    next(arm)


def D(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=7, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=-7, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=7, wait=True)

    next(arm)


def E(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=0, y=6, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=-6, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=3, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=-3, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=6, wait=True)
    up(arm)

    next(arm)


def F(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=0, y=6, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=-6, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=3, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=3, wait=True)

    next(arm)


def G(arm):
    arm.set_tool_position(x=10, y=7, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=-7, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=7, wait=True)
    arm.set_tool_position(x=3, y=0, wait=True)
    arm.set_tool_position(x=0, y=-2, wait=True)
    up(arm)
    arm.set_tool_position(x=-3, y=2, wait=True)

    next(arm)


def H(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=10, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=5, y=-10, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=10, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=0, wait=True)

    next(arm)


def I(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)

    next(arm)


def J(arm):
    arm.set_tool_position(x=10, y=7, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=-7, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=7, wait=True)

    next(arm)


def K(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=5, y=5, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=-5, wait=True)
    down(arm)
    arm.set_tool_position(x=-5, y=5, wait=True)
    up(arm)

    next(arm)


def L(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=7, wait=True)
    up(arm)

    next(arm)


def M(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=-5, y=5, wait=True)
    arm.set_tool_position(x=5, y=5, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)

    next(arm)


def N(arm):
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=-10, y=5, wait=True)
    arm.set_tool_position(x=10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)

    next(arm)


def O(arm):
    arm.set_tool_position(x=10, y=5, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=-5, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=10, wait=True)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=0, y=-5, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=5, wait=True)

    next(arm)


def P(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=6, wait=True)
    arm.set_tool_position(x=-5, y=0, wait=True)
    arm.set_tool_position(x=0, y=-6, wait=True)
    up(arm)
    arm.set_tool_position(x=-5, y=6, wait=True)

    next(arm)


def Q(arm):
    arm.set_tool_position(x=10, y=5, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=-5, wait=True)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=10, wait=True)
    arm.set_tool_position(x=10, y=0, wait=True)
    arm.set_tool_position(x=0, y=-5, wait=True)
    up(arm)
    arm.set_tool_position(x=-8, y=3, wait=True)
    down(arm)
    arm.set_tool_position(x=-2, y=2, wait=True)
    up(arm)

    next(arm)


def R(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=6, wait=True)
    arm.set_tool_position(x=-5, y=0, wait=True)
    arm.set_tool_position(x=0, y=-6, wait=True)
    arm.set_tool_position(x=-5, y=6, wait=True)

    next(arm)


def S(arm):
    arm.set_tool_position(x=10, y=6, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=-6, wait=True)
    arm.set_tool_position(x=-5, y=0, wait=True)
    arm.set_tool_position(x=0, y=6, wait=True)
    arm.set_tool_position(x=-5, y=0, wait=True)
    arm.set_tool_position(x=0, y=-6, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=6, wait=True)

    next(arm)


def T(arm):
    arm.set_tool_position(x=0, y=5, wait=True)
    down(arm)
    arm.set_tool_position(x=10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=-5, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=10, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)


def U(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)
    arm.set_tool_position(x=0, y=6, wait=True)
    arm.set_tool_position(x=10, y=0, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)


def V(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=5, wait=True)
    arm.set_tool_position(x=10, y=5, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)

    next(arm)


def W(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=2.5, wait=True)
    arm.set_tool_position(x=2.5, y=2.5, wait=True)
    arm.set_tool_position(x=-2.5, y=2.5, wait=True)
    arm.set_tool_position(x=10, y=2.5, wait=True)
    up(arm)
    arm.set_tool_position(x=-10, y=0, wait=True)

    next(arm)


def X(arm):
    down(arm)
    arm.set_tool_position(x=10, y=10, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=-10, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=10, wait=True)
    up(arm)

    next(arm)


def Y(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=-5, y=5, wait=True)
    up(arm)
    arm.set_tool_position(x=5, y=5, wait=True)
    down(arm)
    arm.set_tool_position(x=-10, y=-10, wait=True)
    up(arm)
    arm.set_tool_position(x=0, y=10, wait=True)

    next(arm)


def Z(arm):
    arm.set_tool_position(x=10, y=0, wait=True)
    down(arm)
    arm.set_tool_position(x=0, y=10, wait=True)
    arm.set_tool_position(x=-10, y=-10, wait=True)
    arm.set_tool_position(x=0, y=10, wait=True)
    up(arm)

    next(arm)


# arm.set_tool_position(x=, y=, wait=True)
