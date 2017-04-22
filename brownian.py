"""
brownian() implements one dimensional Brownian motion (i.e. the Wiener process).
"""

# File: brownian.py

from math import sqrt
from scipy.stats import norm
import numpy as np


def brownian(p, n, dt,epsilon, delta, boundary,corner_radius, out=None):

    end=n
    p = np.asarray(p)
    start=[]
    start.append(p[0])
    start.append(p[1])
    # set above wiener variance parameter
    #print(x0)
    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r=np.empty(p.shape)
    #same dimsneion as x0
    output=np.zeros((2,) + (n+1,))
    #initialize the starting point of trajectory\
    output[0,0]=p[0]
    output[1,0]=p[1]
    i=1
    boundary_crossed=False
    if ((start[0]**2 + start[1]**2 > boundary**2)):
        boundary_reached1 = True
    else:
        boundary_reached1 = False

    stepsize_limit= 1.5
    r_x=0
    r_y=0
    hit_corner=False

    while(n>0 and p[0]>epsilon and p[1] >epsilon):

    #Here we change our random variables to have integer value
        if (not boundary_reached1):
            #Both coordinates grow with delta*dt = dt' determines the time setep. R_x = sqrt(x^2y) * dt'
            r_x=norm.rvs(size= 1, scale=1)*delta**2*sqrt((p[0]**2)*p[1])*sqrt(dt)
            r_y=norm.rvs(size= 1, scale= 1)*delta**2*sqrt(p[0]*p[1])*sqrt(dt)


        #update our points
            if (abs(r_x)<=stepsize_limit) and (abs(r_y)<=stepsize_limit):
                p[0] = p[0] + r_x
                p[1] = p[1] + r_y
                output[0,i] = p[0]
                output[1,i] = p[1]
            else:
                output[0,i] = p[0]
                output[1,i] = p[1]                

        
        if (boundary_reached1):
    #Here we change our random variables to have integer value
            r_x=norm.rvs(size= 1, scale=sqrt(dt)*delta**2)
            r_y=norm.rvs(size= 1, scale= sqrt(dt)*delta**2)

        #update our points
            p[0] = p[0] + r_x
            p[1] = p[1] + r_y
            output[0,i] = p[0]
            output[1,i] = p[1]
        if ((start[0]**2 + start[1]**2 > boundary**2) and (p[0]**2 + p[1]**2 <= boundary**2) and (not boundary_crossed)):
            boundary_crossed = True
        if ((start[0]**2 + start[1]**2 < boundary**2) and (p[0]**2 + p[1]**2 >= boundary**2) and (not boundary_crossed)):
            boundary_crossed = True



        n=n-1
        i=i+1
        if ((p[0]**2 + p[1]**2) > boundary**2):
            boundary_reached1 = True
        if ((p[0]**2 + p[1]**2) <= boundary**2):
            boundary_reached1 = False

        if (p[0]**2 + p[1]**2 <= corner_radius**2):
            hit_corner=True
            break


    indicator=0

    for num in range(0, end):
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
    #print(r.shape)
    #print(r)
    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples. 
    #print(np.cumsum(r, axis=-1, out=out))
    # Add the initial condition.