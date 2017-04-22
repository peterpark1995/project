"""
brownian() implements one dimensional Brownian motion (i.e. the Wiener process).
"""

# File: brownian.py

from math import sqrt
from scipy.stats import norm
import numpy as np


def brownian(p, n, dt, out=None):
    """\Generate an instance of Brownian motion (i.e. the Wiener process):
    
        X(t) = X(0) + N(0, delta**2 * t; 0, t)
    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1) and
    [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.
    
    Written as an iteration scheme,
        X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)
    If `x0` is an array (or array-like), each value in `x0` is treated as
    an initial condition, and the value returned is a numpy array with one
    more dimension than `x0`.
    Arguments
    ---------
    [] : float or numpy array (or something that can be converted to a numpy array
         using numpy.asarray(x0)).
        The initial position of the Brownian motion.
    n : int
        The number of steps to take.
    dt : float = sqrt(h)
        The time step.
    delta : float
        delta determines the "speed" of the Brownian motion.  The random variable
        of the position at time t, X(t), has a normal distribution whose mean is
        the position at time t=0 and whose variance is delta**2*t.
    out : numpy array or None
        If `out` is not None, it specifies the array in which to put the
        result.  If `out` is None, a new numpy array is created and returned.
    Returns
    -------
    A numpy array of floats with shape `x0.shape + (n,)`.
    
    Note that the initial value `x0` is not included in the returned array.
    """
    end=n
    p = np.asarray(p)
    epsilon = 0.0001
    delta=0.5

    boundary= 100.0
    # set above wiener variance parameter
    #print(x0)
    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r=np.empty(p.shape)
    #same dimsneion as x0
    output=np.zeros((3,) + (n+1,))
    #initialize the starting point of trajectory\
    output[0,0]=p[0]
    output[1,0]=p[1]
    output[2,0]=p[2]
    i=1
    boundary_reached=False
    while(n>0 and p[0]>epsilon and p[1] >epsilon and p[2]>epsilon):
    #Here we change our random variables to have integer value
        if (p[1] <= boundary or p[0] <= boundary) and (not boundary_reached):
            r_x=norm.rvs(size= 1, scale=delta*sqrt((p[0]**2)*p[1])*sqrt(dt))
            r_y=norm.rvs(size= 1, scale= delta*sqrt(p[0]*p[1])*sqrt(dt))
            r_z=norm.rvs(size=1, scale=delta*sqrt(p[0]*p[1])*sqrt(dt))
        #update our points
            p[0] = p[0] + r_x
            p[1] = p[1] + r_y
            p[2] = p[2] + r_z
            output[0,i] = p[0]
            output[1,i] = p[1]
            output[2,i] = p[2]
        if boundary_reached:
    #Here we change our random variables to have integer value
            r_x=norm.rvs(size= 1, scale=sqrt(dt))
            r_y=norm.rvs(size= 1, scale= sqrt(dt))
            r_z=norm.rvs(size= 1, scale=sqrt(dt))
        #update our points
            p[0] = p[0] + r_x
            p[1] = p[1] + r_y
            p[2] = p[2] + r_z
            output[0,i] = p[0]
            output[1,i] = p[1]
            output[2,i] = p[2]
        n=n-1
        i=i+1
        if p[0] > boundary or p[1] > boundary or p[2] > boundary:
            boundary_reached=True
    indicator=0
    for num in range(end,0, -1):
        if output[0,num] <epsilon or output[1,num] <epsilon or output[2,num] < epsilon:
            indicator=num
    if (boundary_reached):
        print "boundary reached"
    else:
        print "boundary not reached"
    if indicator >0.0:
        print "The index of impact is ", (indicator) ,  "and the impact coordinate is " ,  "(" , p[0], "," , p[1] , "," , p[2], ")"
        print 'The final coordinate is (', output[0,indicator], ',' ,output[1,indicator], ',' , output[2,indicator], ')'
        return output[:,:indicator+1]
    else:
        print "There is no collision"
        print 'The final coordinate is (', output[0,end], ',' ,output[1,end], ','  ,output[2,end], ')'
        return output[:,:]
    print output[:,:indicator]
    #s= "DATA SAMPLE:", "Point: ", p , "Number of steps", n , "dt: " , dt 
    #s=str(s)
    #print(s)
    with open('2.txt', 'a') as f:
        f.write(s)
        sys.stdout=f

    f.close()
    #size will tell us (number of dots, number of steps taken)
    # If `out` was not given, create an output array.

    if out is None:
        out = output
    #print(r.shape)
    #print(r)
    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples. 
    #print(np.cumsum(r, axis=-1, out=out))
    # Add the initial condition.