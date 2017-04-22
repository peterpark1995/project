#!/usr/bin/python

import numpy
import matplotlib.pyplot as plt
from brownian import brownian
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys
import numpy as np
def update(data):
    line.set_ydata(data[1])
    line.set_xdata(data[0])
    return line,

def main():

    # Total time.
    T = 50.0
    # max Number of steps.
    N = 3000
    # Time step size
    dt = T/N
    # Initialize point p, the starting point
    p = numpy.empty((2,N+1))
    start = 1
    #Assuming that the motion of the particle starts at (5,5)
    p[0,0] = start
    p[1,0] = start
    Iterations = 3000
    epsilon = 0.0001
    delta=0.5
    corner_radius= 100*epsilon
    boundary= 5

    print 'Point =','(' , p[0,0],',',p[1,0], ')'
    print 'Number of steps = ', N
    print 'Total time =', T
    print 'Iterations =', Iterations
    print 'epsilon =', epsilon
    print 'delta =', delta
    print 'boundary =', boundary
    print 'corner size  =',
    #for boundaries
    x1 = np.arange(0.0, boundary, 0.0001)
    y1 = np.sqrt(boundary**2 - x1**2)
    corner1 = np.arange(0.0, corner_radius, corner_radius/10000)
    corner2= np.sqrt((corner_radius)**2 - corner1**2)

    # The Wiener process parameter. We will define two where intial delta1 = x^2y and delta2 = xy. Then this is a function mapper
    for i in range(0,Iterations):
        x=brownian(p[:,0], N, dt, epsilon, delta, boundary)

        fig, ax = plt.subplots()

        #Two brownian motions one with x coordinate and the other with y coordinate

        #x_trajectory= brownian(x[0,0], N, dt, delta, out=x[:,1:])
        #y_trajectory= brownian(x[1,0], N, dt, delta, out=x[:,1:])

        # Plot the 2D trajectory.
        plt.plot(x[0],x[1])
        plt.plot(x1,y1, '--')
        plt.plot(corner1,corner2, 'pink')
        edge = np.arange(0, np.amax(x), 0.0001)
        zero= np.zeros(shape=len(edge))

        plt.plot(zero,edge)
        plt.plot(edge,zero)
       # fig,ax = plt.subplots()
        # Mark the start and end points.
        plt.plot(x[0,0],x[1,0], 'go')
        plt.plot(x[0,-1], x[1,-1], 'ro')
        # More plot decorations.
        plt.title('2D Brownian Motion')
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
        plt.axis('equal')
        plt.grid(True)
        if (i<Iterations-10):
            plt.show(block=False)
            plt.close()
        else:
            plt.show()
        p[0,0] = start
        p[1,0] = start

        f= open('1.txt', 'w')
if __name__ == "__main__":
    main()
