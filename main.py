import turtle
from turtle import Screen
from random import *
import numpy as np

turtle.shape('circle')
turtle.width = 2
turtle.penup()
screen=Screen()

number = 50 # Количество черепах
steps = 100 # Количество шагов (за 1 шаг все черепахи перемещаются 1 раз)

pool = [turtle.Turtle(shape='circle') for r in range(0, number, 1)] # Задание набора черепах

for trt in pool:
    trt.penup()
    trt.speed(50)

def moveturtles(turtlenumber, sm ,sn):
    """Переместить черепаху в точку (sm, sn)"""
    pool[turtlenumber].goto(sm, sn)

x = []
y = []
vx = []
vy = []
dist = [[0] * number for i in range(0, number, 1)]
ax = []
ay = []

x_border = 350
y_border = 250
maxspeed = 30

for i in range(0, number, 1):
    x.append(randint(-1 * x_border, x_border))
    y.append(randint(-1 * y_border, y_border))
    vx.append(randint(1,maxspeed))
    vy.append(randint(1,maxspeed))
    ax.append(0)
    ay.append(0)

def body():

    global ax, ay, vx, vy, x, y, dist

    gravity_power = 2
    gravity_coefficient = 10
    push_power = 3
    push_coefficient = 10
    dt = 1
    gap = 0.1

    atan = 0

    for i in range(0, number, 1):
        for j in range(0, number, 1):
            dist[i][j] = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)

        ax[i]=0
        ay[i]=0

        for j in range(0, number, 1):

            if (x[j]-x[i] != 0):
                atan = np.arctan((y[j] - y[i]) / (x[j] - x[i]))
            else:
                if ((y[j] - y[i]) > 0):
                    atan = np.pi / 2
                elif ((y[j] - y[i]) < 0):
                    atan = 3 * np.pi / 2

            if ((dist[i][j]) == 0):
                (dist[i][j]) = gap

            if (i != j):
                ax[i] += gravity_coefficient/np.power((dist[i][j]), gravity_power) * np.cos(atan)
                ay[i] += gravity_coefficient/np.power((dist[i][j]), gravity_power) * np.sin(atan)
                ax[i] -= push_coefficient/np.power((dist[i][j]), push_power) * np.cos(atan)
                ay[i] -= push_coefficient/np.power((dist[i][j]), push_power) * np.sin(atan)

        for e in range(0, number, 1):
            moveturtles(e, x[e],y[e])

        vx[i] += ax[i] * dt
        vy[i] += ay[i] * dt
        if (np.abs(x[i] + vx[i] * dt) < x_border):
            x[i] += vx[i] * dt
        else:
            vx[i] = -1 * vx[i]
            x[i] += vx[i] * dt
        if (np.abs(y[i] + vy[i] * dt) < y_border):
            y[i] += vy[i] * dt
        else:
            vy[i] = -1 * vy[i]
            y[i] += vy[i] * dt

for q in range (0, steps, 1):
    body()
screen.exitonclick()