import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.colors import cnames
from math import sqrt

from scipy.stats import norm





def Gen_RandLine(length, dims=3):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    boundary= 5
    end=length
    start=[]
    epsilon= 0.0001
    stepsize_limit= 2000
    start.append(2)
    start.append(2)
    start.append(2)
    i=1
    boundary_crossed=False
    if ((start[0]**2 + start[1]**2 + start[2]**2 > boundary**2)):
        boundary_reached1 = True
    else:
        boundary_reached1 = False
    lineData = np.empty((dims, length))
    lineData[:, 0] = start
    delta=1

    T = 100.0
    # max Number of steps.
    N = length
    # Time step size
    dt = T/N

    corner_radius= 100*epsilon
    hit_corner=False

    #parameters adjusted


    for index in range(1, length):

    #Here we change our random variables to have integer value
        r_x=norm.rvs(size= 1, scale=1)* (sqrt(dt)*delta**2)
        r_y=norm.rvs(size= 1, scale=1)* (sqrt(dt)*delta**2)
        r_z=norm.rvs(size =1, scale=1)* (sqrt(dt)*delta**2)
        #update our points
        lineData[0,index] = lineData[0,index-1] + r_x
        lineData[1,index] = lineData[0,index-1] + r_y
        lineData[2,index] = lineData[0,index-1] + r_z



    indicator=0

    for num in range(0, end):
        if lineData[0,num] <epsilon or lineData[1,num] <epsilon or lineData[2,num] < epsilon or (lineData[0,num]**2 + lineData[1,num]**2 + lineData[2,num]**2 <=corner_radius**2) :
            indicator=num
            break;
    if (hit_corner):
        print ("HIIIIITTTTT")

    if (boundary_crossed):
        print ("boundary crossed")
    else:
        print ("boundary not crossed")
    if indicator >0.0:
        print ("The index of impact is ", indicator)
        print ('The final coordinate is (',lineData[0,indicator],',',lineData[1,indicator], ',' , lineData[2,indicator],')')
        return lineData[:,:indicator+1]
    else:
        print ("There is no collision")
        print ('The final coordinate is (',lineData[0,end-1], ',' ,lineData[1,end-1],',', lineData[2,end-1] ,')')
        return lineData[:,:]


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines
data = [Gen_RandLine(3000, 3) for index in range(1)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([-0.1, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-0.1, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-0.1, 10.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 3000, fargs=(data, lines),
                                   interval=50, blit=False)

plt.show()