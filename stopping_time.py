import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integrate
from scipy.stats import norm
from math import sqrt

fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8,0.8])





from matplotlib.colors import cnames

N=30000

  # Total time.
T = 100.0
  # max Number of steps.
  # Time step size
dt = T/N
# Initialize point p, the starting point
p = np.empty((2,N))
start = 3
  #Assuming that the motion of the particle starts at (5,5)
p[0,0] = start
p[1,0] = start
starting_point= np.empty((2,N))
starting_point[0,0] = start
starting_point[1,0] = start
epsilon = 0.0001
delta=1
corner_radius= 100*epsilon
boundary= 5

time_text = ax.text(0.02,-0.95,'')
class particle:


  def __init__(self,f):

    self.initial_position_x=f[0,0]
    self.initial_position_y=f[1,0]
    self.time_elapsed=0


  def step(self,dt):
    self.time_elapsed+=dt


def brownian(p, dt,epsilon, delta, boundary,corner_radius, out=None):

    p = np.asarray(p)
    start=[]
    start.append(p[0])
    start.append(p[1])
    # set above wiener variance parameter
    #print(x0)
    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    #same dimsneion as x0

    output=np.zeros((2,) + (1,))

    #initialize the starting point of trajectory\

    output[0,0]=p[0]
    output[1,0]=p[1]
    i=1
    boundary_crossed=False

    if ((start[0]**2 + start[1]**2 > boundary**2)):
        boundary_reached1 = True
    else:
        boundary_reached1 = False

    stepsize_limit= 0.3

    hit_corner=False
    output=output.tolist()
    while(p[0]>epsilon and p[1] >epsilon):

    #Here we change our random variables to have integer value

            #Both coordinates grow with delta*dt = dt' determines the time setep. R_x = sqrt(x^2y) * dt'
      if (not boundary_reached1):
            #Both coordinates grow with delta*dt = dt' determines the time setep. R_x = sqrt(x^2y) * dt'
        r_x=norm.rvs(size= 1, scale=1)*delta**2*sqrt((p[0]**2)*p[1])*sqrt(dt)
        r_y=norm.rvs(size= 1, scale= 1)*delta**2*sqrt(p[0]*p[1])*sqrt(dt)
        #update our points

        p[0] = p[0] + r_x
        p[1] = p[1] + r_y
        output[0].append(p[0])
        output[1].append(p[1])
                

        
      if (boundary_reached1):
    #Here we change our random variables to have integer value
        r_x=norm.rvs(size= 1, scale=sqrt(dt)*delta**2)
        r_y=norm.rvs(size= 1, scale= sqrt(dt)*delta**2)
        #update our points
        p[0] = p[0] + r_x
        p[1] = p[1] + r_y
        output[0].append(p[0])
        output[1].append(p[1])
      if ((start[0]**2 + start[1]**2 > boundary**2) and (p[0]**2 + p[1]**2 <= boundary**2) and (not boundary_crossed)):
        boundary_crossed = True
      if ((start[0]**2 + start[1]**2 < boundary**2) and (p[0]**2 + p[1]**2 >= boundary**2) and (not boundary_crossed)):
        boundary_crossed = True

      if ((p[0]**2 + p[1]**2) > boundary**2):
        boundary_reached1 = True
      if ((p[0]**2 + p[1]**2) <= boundary**2):
        boundary_reached1 = False

      if (p[0]**2 + p[1]**2 <= corner_radius**2):
        hit_corner=True


    indicator=0
    output=np.asarray(output)
    for num in range(0, len(output[0])):
        if output[0,num] <epsilon or output[1,num] <epsilon or (output[0,num]**2 + output[1,num]**2 <=corner_radius**2) :
            indicator=num
            break;
    if (hit_corner):
        print ("HIIIIITTTTT")

    if (boundary_crossed):
        print ("boundary crossed")
    else:
        print ("boundary not crossed")
    if indicator >0.0:
        print ("The index of impact is ", (indicator), "and the impact coordinate is " ,  "(",p[0],",",p[1],")")
        print ('The final coordinate is (',output[0,indicator],',',output[1,indicator],')')
        return output[:,:indicator+1]
    else:
        print ("There is no collision")
        print ('The final coordinate is (',output[0,end], ',' ,output[1,end], ')')
        return output[:,:]

    if out is None:
        out = output
particle1=particle(p)
number_of_particles=1
colors = plt.cm.jet(np.linspace(0, 1, number_of_particles))
lines = sum([ax.plot([], [],  '-', c=c,lw=1) for c in colors], [])
pts = sum([ax.plot([], [],  'o', c=c) for c in colors], [])

f=[]
f.append(brownian(p[:,0], dt, epsilon, delta, boundary,corner_radius))



plt.plot(starting_point[0,0],starting_point[1,0], 'go')
def init():
  for line, pt in zip(lines, pts):
    line.set_data([], [])
    pt.set_data([], [])


  ax.set_ylim(-0.1,15)
  ax.set_xlim(-0.1, 15)
  return lines, pts





def animate(i):
    """perform animation step"""
    

    i = 5*i % N


    """Speed up process"""


    particle1.step(5*dt)
    for line, pt, fi in zip(lines, pts,f):
        x=fi[0,:i].T
        y=fi[1,:i].T
        pt.set_data(x[-1:], y[-1:])
        line.set_data(x, y)


    line.set_linestyle('-')
    time_text.set_text('time = %.3f' % particle1.time_elapsed)
    return lines, pts, time_text





print ("Point =" ,"(" , p[0,0],",",p[1,0],  ")")
print ('Number of steps = ', len(f[0]))
print ('Total time =', T)
print ('Iterations =', number_of_particles)
print ('epsilon =', epsilon)
print ('delta =', delta)
print ('boundary =', boundary)
print ('corner size  =', corner_radius)
#for boundaries
x1 = np.arange(0.0, boundary+0.01, 0.1)
y1 = np.sqrt(boundary**2 - x1**2)
corner1 = np.arange(0.0, corner_radius, corner_radius/10000)
corner2= np.sqrt((corner_radius)**2 - corner1**2)
  

plt.plot(x1,y1, '--',c='black')
plt.plot(corner1,corner2, 'pink')
edge = np.arange(0, 100, 0.0001)
zero= np.zeros(shape=len(edge))

plt.plot(zero,edge)
plt.plot(edge,zero)
ax.grid(True)

plt.title('2D Brownian Motion')
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.axis('equal')



from time import time
t0=time()
animate(0)
t1=time()
interval=N*dt-(t1-t0)


ani = animation.FuncAnimation(fig, animate,  blit=False, interval=interval, repeat=True, init_func=init)

plt.show()