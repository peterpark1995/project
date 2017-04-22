import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from brownian import brownian
import scipy.integrate as integrate

fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8,0.8])

from matplotlib.colors import cnames


  # Total time.
T = 100.0
  # max Number of steps.
N = 30000
  # Time step size
dt = T/N
# Initialize point p, the starting point
p = np.empty((2,N))
start = 2
  #Assuming that the motion of the particle starts at (5,5)
p[0,0] = start
p[1,0] = start
starting_point= np.empty((2,N))
starting_point[0,0] = start
starting_point[1,0] = start
Iterations = 3000
epsilon = 0.0001
delta=1
corner_radius= 100*epsilon
boundary= 5

time_text = ax.text(0.02,-0.1,'')
class particle:


  def __init__(self,f):

    self.initial_position_x=f[0,0]
    self.initial_position_y=f[1,0]
    self.time_elapsed=0


  def step(self,dt):
    self.time_elapsed+=dt

particle1=particle(p)
number_of_particles=1000
colors = plt.cm.jet(np.linspace(0, 1, number_of_particles))
lines = sum([ax.plot([], [],  '-', c=c,lw=1) for c in colors], [])
pts = sum([ax.plot([], [],  'o', c=c) for c in colors], [])




f=[]
for i in range(0,number_of_particles):
  f.append(brownian(p[:,0], N, dt, epsilon, delta, boundary,corner_radius))
  p[0,0] = start
  p[1,0] = start


plt.plot(starting_point[0,0],starting_point[1,0], 'go')

def init():
  for line, pt in zip(lines, pts):
    line.set_data([], [])
    pt.set_data([], [])


  ax.set_ylim(-0.1,8)
  ax.set_xlim(-0.1, 8)
  return lines, pts





def animate(i):
    """perform animation step"""
    

    i = i % N


    """Speed up process"""


    particle1.step(dt)
    for line, pt, fi in zip(lines, pts,f):
        x=fi[0,:i].T
        y=fi[1,:i].T
        pt.set_data(x[-1:], y[-1:])
        line.set_data(x, y)


    line.set_linestyle('-')
    time_text.set_text('time = %.3f' % particle1.time_elapsed)
    return lines, pts, time_text





print ("Point =" ,"(" , p[0,0],",",p[1,0],  ")")
print ('Number of steps = ', N)
print ('Total time =', T)
print ('Iterations =', Iterations)
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


ani = animation.FuncAnimation(fig, animate,  blit=False, frames=35000, interval=300, init_func=init)
ani.save('test1.mp4', fps=15, extra_args=['-vcodec', 'libx264'])

plt.show()
