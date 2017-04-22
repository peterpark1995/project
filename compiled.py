import numpy
from pylab import plot, show, grid, axis, xlabel, ylabel, title

from brownian import brownian


def main():

    # Total time.
    T = 10.0
    # max Number of steps.
    N = 100000
    # Time step size
    dt = T/N
    # Initialize point p, the starting point
    p = numpy.empty((2,N+1))


    #Assuming that the motion of the particle starts at (5,5)
    p[0,0] = 6.32277563288e-24
    p[1,0] = 11.99403568
    # The Wiener process parameter. We will define two where intial delta1 = x^2y and delta2 = xy. Then this is a function mapper
    x=brownian(p[:,0], N, dt)
    #Two brownian motions one with x coordinate and the other with y coordinate

    #x_trajectory= brownian(x[0,0], N, dt, delta, out=x[:,1:])
    #y_trajectory= brownian(x[1,0], N, dt, delta, out=x[:,1:])

    # Plot the 2D trajectory.
    plot(x[0],x[1])
    
    # Mark the start and end points.
    plot(x[0,0],x[1,0], 'go')
    plot(x[0,-1], x[1,-1], 'ro')
    # More plot decorations.
    title('2D Brownian Motion')
    xlabel('x', fontsize=16)
    ylabel('y', fontsize=16)
    axis('equal')
    grid(True)
    show()


if __name__ == "__main__":
    main()