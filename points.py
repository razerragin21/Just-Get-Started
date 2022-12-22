import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset, assuming this is our daily points

# days passed
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# points per day
y = np.array([20, 30, 5, 12, 39, 48, 50, 3])

# linear interpolation between x and y
X_Y_Spline = make_interp_spline(x, y)

# Returns evenly spaced numbers
# over a specified interval
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# plot  the Graph
plt.plot(X_, Y_, color = '#40CA58', linewidth = 2)
plt.title("Your progress mapped")
plt.xlabel("Days")
plt.ylabel("Points")
# Show the plot
plt.show()
