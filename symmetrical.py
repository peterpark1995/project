import numpy
import matplotlib.pyplot as plt
from symmetrical_brownian import brownian
import matplotlib.animation as animation
import sys
def update(data):
    line.set_ydata(data[1])
    line.set_xdata(data[0])
    return line,

def main():

    # Total time.
    T = 100.0
    # max Number of steps.
    N = 3000
    # Time step size
    dt = T/N
    # Initialize point p, the starting point
    p = numpy.empty((2,N+1))
    start = 3
    #Assuming that the motion of the particle starts at (5,5)
    p[0,0] = start
    p[1,0] = start
    Iterations = 40
    # The Wiener process parameter. We will define two where intial delta1 = x^2y and delta2 = xy. Then this is a function mapper
    for i in range(0,Iterations):
        x=brownian(p[:,0], N, dt)
        fig, ax = plt.subplots()

        #Two brownian motions one with x coordinate and the other with y coordinate

        #x_trajectory= brownian(x[0,0], N, dt, delta, out=x[:,1:])
        #y_trajectory= brownian(x[1,0], N, dt, delta, out=x[:,1:])

        # Plot the 2D trajectory.
        plt.plot(x[0],x[1])
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
        plt.show()
        p[0,0] = start
        p[1,0] = start
    plt.close()

if __name__ == "__main__":
    main()
