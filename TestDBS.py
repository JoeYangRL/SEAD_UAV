import dubins
import numpy
import matplotlib
import matplotlib.pyplot as plt

q0 = (40, 300, 0)
q1 = (100, 100, numpy.pi/3)
turning_radius = 20
step_size = 0.5

path = dubins.shortest_path(q0, q1, turning_radius)
configurations, _ = path.sample_many(step_size)
fig=plt.figure()
xs=[]
ys=[]
for i in range(0,len(configurations)):
    xs.append(configurations[i][0])
    ys.append(configurations[i][1])

plt.plot(xs,ys,'r-')
plt.show()
#print(configurations[0][0])

