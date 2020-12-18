#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import os
import xml.etree.ElementTree as ET

dirname = os.path.dirname(__file__)

def bezier_points(P: list, resolution: int) -> np.array:
    T = np.linspace(0, 1, resolution)
    return np.array([
        ((1 - t)**3) * P[0] + 3 * ((1 - t)**2) * t * P[1] + 3 * (1 - t) * (t**2) * P[2] + (t**3) * P[3] for t in T
    ])


def get_path_dict(filename: str) -> dict:
    stopcond = lambda d, i: d[i+1] not in ["M", "C", "Z",] and i+1 < len(d)-1

    tree = ET.parse(dirname + "/files/" + filename)
    root = tree.getroot()
    d = root[0].attrib["d"]
    points = dict()
    index = 0


    for i in range(len(d)):
        if d[i] == "M":
            start = i+1
            while stopcond(d,i):
                i+=1
                if  i < len(d)-2 and d[i+1] + d[i+2] == "  ":
                    end = i
                    points["M" + str(index)] = str(d[start+1:end+1])
                    index += 1

                    while d[i+1] == " " and i < len(d)-1:
                        i+=1                
                    start = i
            continue

        if d[i] == "C":
            start = i+1
            while stopcond(d,i):
                i+=1
                if i < len(d)-2 and d[i+1] + d[i+2] == "  ":
                    end = i
                    points["C" + str(index)] = str(d[start+1:end+1])
                    index += 1

                    while d[i+1] == " " and i < len(d)-1:
                        i+=1                
                    start = i
            continue

        if d[i] == "Z":
            points["Z" + str(index)] = 0
            index += 1
            continue

    mem = ""
    for key in points:
        if key[0] == "M":
            points[key] = np.array([list(map(float, points[key].split(",")))])
            mem = key
        
        if key[0] == "C":
            try:
                start = [points[mem][3].copy()]
            except:
                start = [points[mem][0].copy()]

            start += [list(map(float, x.split(","))) for x in points[key].split(" ")]
            points[key] = np.array(start)
            mem = key

    return points

points = get_path_dict("path")


def get_points_coords(points: np.array, res:int) -> list:
    coords = list()
    isUp = False

    for key in points:
        if key[0] == "C":
            P = points[key]

            # coords.append(np.array([bezier_points(P[:,0], res), bezier_points(P[:,1], res)]))
            coords.append(np.array([bezier_points(P[:,0], res), bezier_points(P[:,1], res), np.zeros(res)]))

            if isUp:
                coords[-2][0, 1:] = P[0,0]
                coords[-2][1, 1:] = P[0,1]
                isUp = False

        elif key[0] == "Z":
            coords.append(np.array([np.zeros(res), np.zeros(res), -5*np.ones(res)]))
            coords[-1][0,0] = coords[-2][0, -1]
            coords[-1][1,0] = coords[-2][1, -1]
            isUp = True

    return coords

# print(get_points_coords(get_path_dict("contourgroguraw"), 5))

""" 
points = get_path_dict("contourgroguraw")
for key in points:
    print(key)
    print(points[key])
 """


""" 
P = np.array([
    [0,100],
    [100,50],
    [200,150],
    [300,100],
]) 
"""



""" 
fig, ax = plt.subplots(1,1, figsize=(6,4))
plt.style.use('fivethirtyeight')

res = 5

for key in points:
    if key[0] == "C":
        P = points[key]
        ax.plot(bezier_points(P[:,0], res), bezier_points(P[:,1], res))

ax.set_ylim(ax.get_ylim()[::-1])

# ax.plot(bezier_points(P[:,0], 100), bezier_points(P[:,1], 100))
# plt.plot(bezier_points([100, 50, 150, 100], 100))

plt.show() 
 """
