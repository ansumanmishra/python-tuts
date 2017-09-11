import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7 , 8]

plt.xlabel('Speed')
plt.ylabel('Hr')

plt.plot(x, y)
plt.show()

''' Drawing a Pie Chart '''

# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()