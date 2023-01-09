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


#feynman 
#1. pick a topic
#2. explain to 12 year old
#3. review, simplify, repeat