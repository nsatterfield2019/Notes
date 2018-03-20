# PLOTTING (withmathploitlib)

import matplotlib.pyplot as plt

plt.figure(1) # creates a new window

plt.plot([1, 2, 3, 4]) # if there is no x axis, it just gives index 0, 1, 2...
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


plt.figure(2, facecolor ='limegreen') # opens up a new window/figure

x = [x for x in range(10)]
y = [y**2 for y in range(10)]

# plot.plt takes kwarg (keyword arguments)
plt.plot(x,y, color='violet', marker='o', markersize=10, linestyle="--", alpha=0.5)

plt.xlabel('time (days)')
plt.ylabel('excitement level (yays)', color = 'red')
plt.title('Example Plot', color = 'blue', fontsize=30)
plt.axis([1, 10, 10, 100])

plt.show()

