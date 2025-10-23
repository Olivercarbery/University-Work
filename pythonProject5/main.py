from No_Drag import trajectory
from Drag import trajectory_drag
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

u0 = 100
theta = 30
g = 9.81
h = 0

x, y = trajectory_drag(g, 0.1125, 0.25, 0.25, 0.45, u0, h, theta)
a, b = trajectory(u0, theta, g, h)
plt.plot(x, y)
plt.plot(a, b)
plt.axis('equal')
plt.show()

