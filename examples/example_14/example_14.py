import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from scipy import interpolate
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from sympy.printing.pretty.pretty_symbology import line_width


def func(x,y):
    return (x+y) * np.exp(-5.0 * (x**4 + y**4))

#X - Y 轴分为 20*20 的网格
y = np.linspace(-1,1,20)
x = np.linspace(-1,1,20)
x,y = np.meshgrid(x,y)
fvals = func(x,y)
fig = plt.figure(figsize=(18,10))
ax = plt.subplot(1,2,1,projection = '3d')
surfl = ax.plot_surface(x,y,fvals,
                        rstride = 2,
                        cstride = 2,
                        cmap = cm.coolwarm,
                        linewidth = 0.5,
                        antialiased = True)
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
plt.colorbar(surfl, shrink=0.5, aspect = 5)
#二维插值
newfunc = interpolate.interp2d(x,y,fvals,kind = 'cubic')
xnew = np.linspace(-1,1,100)
ynew = np.linspace(-1,1,100)
fnew = newfunc(xnew,ynew)
print(fnew)
np.random