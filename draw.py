import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np


# magins
min_val = 0.2
max_val = 0.6

max_cycles = 500
details = 500

# make these smaller to increase the resolution
delta = max_val - min_val
# dx, dy = 0.005, 0.005
dx, dy = delta/details, delta/details

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(min_val, max_val + dy, dy),
                slice(min_val, max_val + dx, dx)]
y *= -1
# x = np.arange(0, 5, 0.5)
# print("Printing x values:")
# print(x)
# print(len(x))
# print("Printing y values:")
# print(y)
# print(len(x))

# Function
# z = np.sin(y) * np.sin(x)
z = x+y

# for n in range(len(x)):
#     for k in range(len(y)): 
#         for a in range(max_cycles):
#             temp = 
#             z[[k],[n]] = a 
#             # print(k*n)

n = 0
k = 0
a = 0
Zr= 0
Zi= 0
while n < len(x):
    while k < len(y):
        # print(k)
        while a < max_cycles:
            tempZr = Zr**2 - Zi**2
            tempZi = 2 * Zr * Zi
            temp = tempZr**2 + tempZi**2
            if temp >= 4:
                break
            z[[k],[n]] = a 
            a += 1 
            Zr = tempZr + x[[k],[n]]
            Zi = tempZi + y[[k],[n]] 
        k += 1
        a = 0
        Zr= 0
        Zi= 0
    n += 1
    k = 0

# print("Printing z values:")
# print(z)
# z[[k],[n]] = 0
# print(z)
# print(len(z))

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
# print(len(z))
# print(z)
# print(z.min() , z.max())
# print(levels)

# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.

fig, ax = plt.subplots()

cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
# print(cmap)
# print(norm)

# im = ax.pcolor(x, y, z, cmap=cmap, norm=norm)

# contours are *point* based plots, so convert our bound into point
# centers

im = ax.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, cmap=cmap, levels=levels)

fig.colorbar(im, ax=ax)

#fig = plt.figure()  # an empty figure with no axes
#fig.suptitle('Title of Figure')  # Add a title so we know which it is

plt.xlabel('real')
plt.ylabel('imaginary')

plt.title("Manderbrot set")

# plt.legend()

plt.show()

