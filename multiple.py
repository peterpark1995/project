
import numpy
import matplotlib.pyplot as plt
from brownian import brownian
import matplotlib.animation as animation
from matplotlib.figure import Figure
import sys
import numpy as np


def main():

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_axes([0.1, 0.1, 0.8,0.8])
    # Total time.
    T = 50.0
    # max Number of steps.
    N = 3000
    # Time step size
    dt = T/N
    # Initialize point p, the starting point
    p = numpy.empty((2,N+1))
    start = 2
    #Assuming that the motion of the particle starts at (5,5)
    p[0,0] = start
    p[1,0] = start
    number_of_particles = 3000
    epsilon = 0.0001
    delta=1 #variance
    corner_radius= 100*epsilon
    boundary= 5
    colors = plt.cm.jet(np.linspace(0, 1, number_of_particles))

    print ("Point =" ,"(" , p[0,0],",",p[1,0],  ")")
    print ('Number of steps = ', N)
    print ('Total time =', T)
    print ('Iterations =', number_of_particles)
    print ('epsilon =', epsilon)
    print ('delta =', delta)
    print ('boundary =', boundary)
    print ('corner size  =', corner_radius)
    #for boundaries
    x1 = np.arange(0.0, boundary+0.1, 0.1)
    y1 = np.sqrt(boundary**2 - x1**2)
    corner1 = np.arange(0.0, corner_radius, corner_radius/10000)
    corner2= np.sqrt((corner_radius)**2 - corner1**2)

    # The Wiener process parameter. We will define two where intial delta1 = x^2y and delta2 = xy. Then this is a function mapper
    f=[]
    for i in range (0, number_of_particles):
        f.append(brownian(p[:,0], N, dt, epsilon, delta, boundary,corner_radius))
        p[0,0] = start
        p[1,0] = start
        #Two brownian motions one with x coordinate and the other with y coordinate

        #x_trajectory= brownian(x[0,0], N, dt, delta, out=x[:,1:])
        #y_trajectory= brownian(x[1,0], N, dt, delta, out=x[:,1:])
    for fi, ci  in zip(f,colors):
        x=fi[0].T
        y=fi[1].T
        plt.plot(x,y,'-',c=ci,lw=1)
        plt.plot(x[-1],y[-1],'o',c=ci)


        # Plot the 2D trajectory.
    plt.plot(x[0],x[1])
    plt.plot(x1,y1, '--')
    plt.plot(corner1,corner2, 'pink')
    edge = np.arange(0, 100, 0.0001)
    zero= np.zeros(shape=len(edge))

    plt.plot(zero,edge)
    plt.plot(edge,zero)
       # fig,ax = plt.subplots()
        # Mark the start and end points.
    plt.plot(p[0,0],p[1,0], 'go')

    plt.title('2D Brownian Motion')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.axis('equal')
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()