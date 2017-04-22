import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.colors import cnames
from math import sqrt

from scipy.stats import norm



number_of_particles = 50
start=[2,2,2]
def Gen_RandLine(length, dims):


    boundary= 5
    end=length
    epsilon= 0.0001
    stepsize_limit= 2000

    i=1
    boundary_crossed=False
    if ((start[0]**2 + start[1]**2 + start[2]**2 > boundary**2)):
        boundary_reached1 = True
    else:
        boundary_reached1 = False
    lineData = np.empty((dims, length))
    delta=1

    T = 100.0
    # max Number of steps.
    N = length
    # Time step size
    dt = T/N

    corner_radius= 100*epsilon
    hit_corner=False







    lineData = np.empty((dims, length))
    lineData[:, 0] = start

    for index in range(1, length):
        if (lineData[0,index-1]>epsilon and lineData[1,index-1]>epsilon and lineData[2,index-1] > epsilon):
            if (not boundary_reached1):
                r_x=norm.rvs(size= 1, scale=1)*(delta**2)*(((lineData[0,index-1]**2)*lineData[1,index-1]*lineData[2,index-1])**(1/3))*sqrt(dt)



                r_y=norm.rvs(size= 1, scale= 1)*delta**2*(((lineData[0,index-1])*lineData[1,index-1]*lineData[2,index-1])**(1/3))*sqrt(dt)
                r_z=norm.rvs(size= 1, scale= 1)*delta**2*(((lineData[0,index-1])*lineData[1,index-1]*(lineData[2,index-1]**2))**(1/3))*sqrt(dt)
                if (abs(r_x)<=stepsize_limit) and (abs(r_y)<=stepsize_limit) and (abs(r_z)<=stepsize_limit):
                    lineData[0,index] = lineData[0,index-1] + r_x
                    lineData[1,index] = lineData[1,index-1] + r_y
                    lineData[2,index] = lineData[2,index-1] + r_z
                else:
                    lineData[0,index] = lineData[0,index-1]
                    lineData[1,index] = lineData[1,index-1]
                    lineData[2,index] = lineData[2,index-1]
            if (boundary_reached1):

    #Here we change our random variables to have integer value
                r_x=norm.rvs(size= 1, scale=sqrt(dt)*delta**2)
                r_y=norm.rvs(size= 1, scale= sqrt(dt)*delta**2)
                r_z=norm.rvs(size =1, scale= sqrt(dt*delta**2))
        #update our points
                lineData[0,index] = lineData[0,index-1] + r_x
                lineData[1,index] = lineData[1,index-1] + r_y
                lineData[2,index] = lineData[2,index-1] + r_z
            if ((lineData[0,0]**2 + lineData[1,0]**2 + lineData[2,0]**2 > boundary**2) and (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2<= boundary**2) and (not boundary_crossed)):
                boundary_crossed = True
            if ((lineData[0,0]**2 + lineData[1,0]**2 + lineData[2,0]**2 > boundary**2) and (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2<= boundary**2)):
                boundary_crossed = True



            if (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2 > boundary**2):
                boundary_reached1 = True
            if (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2 <= boundary**2):
                boundary_reached1 = False

            if (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2 <= corner_radius**2):
                hit_corner=True
                print (lineData[0,index]**2 + lineData[1,index]**2 + lineData[2,index]**2 ) 
                break


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




# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.plot([start[0]],[start[1]],[start[2]], 'go')

# Fifty lines of random 3-D lines
dataLines = [Gen_RandLine(30000, 3) for index in range(number_of_particles)]


# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
colors = plt.cm.jet(np.linspace(0, 1, number_of_particles))

for data,c in zip(dataLines, colors):
    # NOTE: there is no .set_data() for 3 dim data...
    ax.plot(data[0],data[1],data[2], '-', c=c, lw=1)
    ax.scatter(data[0,-1],data[1,-1],data[2,-1], 'o', c=c)


#drawing the boundary 
u=np.linspace(0,np.pi/2,100)
v=np.linspace(0,np.pi/2,100)
boundary = 5
epsilon=0.0001
x=boundary*np.outer(np.cos(u),np.sin(v))
y=boundary*np.outer(np.sin(u),np.sin(v))
z=boundary*np.outer(np.ones(np.size(u)),np.cos(v))
#ax.plot_surface(x,y,z, linewidth=0, color = 'yellow', alpha=0.5)
x1=100*epsilon*np.outer(np.cos(u),np.sin(v))
y1=100*epsilon*np.outer(np.sin(u),np.sin(v))
z1=100*epsilon*np.outer(np.ones(np.size(u)),np.cos(v))
ax.plot_surface(x1,y1,z1,color='pink')



zeros=np.zeros(5000)
axis=np.linspace(0,50,5000)


ax.plot(axis,zeros,zeros)
ax.plot(zeros,axis, zeros)
ax.plot(zeros,zeros,axis)

# Setting the axes properties
ax.set_xlim3d([-1.0, 8.0])
ax.set_xlabel('X')
#ax.grid(False)
#ax.axis('off')
ax.set_ylim3d([-1.0, 8.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0, 8.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')
# Creating the Animation object


plt.show()