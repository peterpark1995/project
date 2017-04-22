
import numpy as np

x= raw_input('file name?')
f= open(x, 'r')

number_of_lines = -9
boundary_not_reached= 0
collision=0
Both=0
interval= 3
list_x=[]
list_y=[]
for line in f:
	if not "Point","Number of steps","Total time", "Iterations", "epsilon =", "delta =","boundary = " in
		number_of_lines = number_of_lines + 1
	if "not" in line:
		boundary_not_reached= boundary_not_reached+1
	if "index" in line:
		collision = collision +1
		split = line.split(' ')
		list_y.append(float(split[-2]))
		list_x.append(float(split[-4]))
	if "not" in line and "index" in line:
		Both= Both+1
		print "number of simulations: ", number_of_lines
print "number of collision: ", collision
print "number of points that reached the boundaries: ", number_of_lines - boundary_not_reached
print "number of particles that reached the boundaries and collided with the wall", Both

maximum=[max(list_x),max(list_y)]
length= round(max(maximum)/interval)
x_density = np.zeros(length)
y_density = np.zeros(length)




for n in range(0,int(length)):
	for x in list_x:
		if ((n*interval) < x < (n+1)*interval ):
			x_density[n]=x_density[n]+1
	for y in list_y:
		if ((n*interval) < y < (n+1)*interval ):
			y_density[n]=y_density[n]+1

for n in range(0,int(length)):
#	print "Hitting density of particle in", n*interval, "to" , (n+1)*interval, "is", x_density[n] ,"in the x-axis"
	print  n*interval, 'to ' , (n+1)*interval, ',' ,  x_density[n] ,

for n in range(0,int(length)):

	print  n*interval, 'to ' , (n+1)*interval, ',' ,  y_density[n] ,

#	print "Hitting density of particle in", n*interval, "to" , (n+1)*interval, "is", y_density[n] ,"in the y-axis"



print(x_density)
print(y_density)


print(length)



