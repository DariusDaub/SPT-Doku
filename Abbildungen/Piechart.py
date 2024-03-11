#Pie chart 
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = 'Tertiärsektor', 'Haushalte', 'Kommunale Liegenschaften', 'Verkehr (Land)'
sizes = [7171329, 4018133, 288918, 100000]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.1, 0.1)  # explode 1st slice


# Plot
#Bigger Fontsize for the labels
plt.rcParams.update({'font.size': 16})
plt.pie(sizes, labels=labels, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()