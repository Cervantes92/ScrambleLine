import numpy as np
import random as rnd
import math as mth
import matplotlib.pyplot as plt

#Line metrics
yIntercept = 5
slope = 0.5
start = -2
stop = 8
resolution = 0.01 #dX

#Rnd metrics
maxDeviation = 2

#Coordinates
xPoints = []
yPoints = []

#Generate coords
i = start
while i < stop:
	xPoints.append(i)
	yPoints.append(i + rnd.randrange(-1, 2, 2) * rnd.random() * maxDeviation)
	i += resolution

#Plot results
plt.plot(xPoints, yPoints)
plt.show()

#Set to 2d array
a = np.asarray([xPoints,yPoints])

#Export as CSV
np.savetxt("xyTrainingData.csv", np.transpose(a), delimiter = ",")