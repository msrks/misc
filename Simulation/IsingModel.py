# coding: utf-8
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

SIZE = 150

def bc(i):
    '''check periodic boundary condition'''
    if i+1 > SIZE -1:
        return 0
    if i-1 < 0:
        return SIZE-1
    else:
        return i

def energy(system, N, M):
    '''calculate internal energy'''
    return -1*system[N,M]*(system[bc(N-1),M]
                          + system[bc(N+1),M]
                          + system[N, bc(M-1)]
                          + system[N, bc(M+1)])

def build_system():
    '''build the system'''
    system = 2*np.random.random_integers(0,1,(SIZE,SIZE)) - 1
    return system

print ("Choose the temperature for your run (0.1-100)")
T = float(input())
STEPS = 1000
SIZE = 150

system = build_system()

fig = plt.figure()
im = plt.imshow(system)

def updatefig(*args):
    global system
    for step, x in enumerate(range(STEPS)):
        M = np.random.randint(0, SIZE)
        N = np.random.randint(0, SIZE)
        E = -2.*energy(system, N, M)

        if E <= 0.:
            system[N,M] *= -1
        elif np.exp(-1./T*E) > np.random.rand():
            system[N,M] *= -1
    im.set_array(system)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, blit=True)
plt.show()
