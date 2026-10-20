import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import interp1d
from sympy.plotting import plot

x = np.arange(0,25,2)
y = np.array([2,3,0,16,26,12,26,10,12,24,16,6,2])
xnew = np.linspace(0,24,24*60)
f = interp1d(x,y,kind='quadratic')
ynew = f(xnew)
c = sum(ynew)
print('总的车辆数为：',c)
plt.plot(xnew, ynew, c = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('traffic.png',dpi = 150)
print('✅ 图片已经保存为 traffic.png')

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x = np.arange(0,25,2)
y = [2,3,0,16,26,12,26,10,12,24,16,6,2]
xnew = np.linspace(0,24,24*60)
f = interp1d(x,y,'quadratic')
ynew = f(xnew)
plt.plot(xnew,ynew,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.show()