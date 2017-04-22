
import numpy as np

x= raw_input('file name?')
f= open(x, 'r')
epsilon=0.0001
number_of_lines = -8
boundary_crossed= 0
collision=0
Both=0
interval= 0.1
list_x=[]
list_y=[]
count=0 
x=[]
y=[]
both_index=0
for line in f:
	if not "Point =" or "Number of steps" or "Total time" or "Iterations" or "epsilon =" or "delta =" or "boundary = " or "corner size" in line:
		number_of_lines = number_of_lines + 1
	if "boundary crossed" in line:
		boundary_crossed= boundary_crossed+1
		both_index=number_of_lines
	if "index" in line:
		collision = collision +1
		split = line.split(' ')
		list_y.append(float(split[-2]))
		list_x.append(float(split[-4]))
		if (number_of_lines== (both_index+1)):
			Both=Both+1

	if "boundary =" in line:
		boundary=line.split(' ')[2]
	if "The final coordinate is" in line:
		x.append(line.split(' ')[5])
		y.append(line.split(' ')[7])



print "number of simulations: ", number_of_lines/3
print "number of collision: ", collision
print "number of points that reached the boundaries: ", boundary_crossed
print "number of particles that reached the boundaries and collided with the wall", Both

print "boundary was", boundary

maximum=[max(list_x),max(list_y)]
length= round(max(maximum)/interval)
x_density = np.zeros(length)
y_density = np.zeros(length)
within=0
for n in range (0,collision):
	if list_y[n]< boundary or list_x[n] < boundary:
		within=within+1

print "collision within the boundary",within
collision_coordinate=[list_x,list_y]
for n in range(0,int(length)):
	for x,y in zip(collision_coordinate[0],collision_coordinate[1]):
		if ((n*interval) < x < (n+1)*interval  and y<epsilon):
			x_density[n]=x_density[n]+1

		if ((n*interval) < y < (n+1)*interval  and x<epsilon):
			y_density[n]=y_density[n]+1
		if (np.absolute(x)<epsilon and np.absolute(y)<epsilon):
			print x,y
			print "$$$$$$$$"

#for n in range(0,int(length)):
#	print "Hitting density of particle in", n*interval, "to" , (n+1)*interval, "is", x_density[n] ,"in the x-axis"

print "Hitting density of particle with x-axis and density"

for n in range(0,int(length)):

	print  n*interval, ',' , (n+1)*interval,  ',', x_density[n] 

#for n in range(0,int(length)):

#	print "Hitting density of particle in", n*interval, "to" , (n+1)*interval, "is", y_density[n] ,"in the y-axis"


print "Hitting density of particle with y-axis and density"

for n in range(0,int(length)):

	print  n*interval, ',' , (n+1)*interval,  ',', y_density[n] 









