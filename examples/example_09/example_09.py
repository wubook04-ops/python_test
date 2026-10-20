from scipy.optimize import minimize
from numpy import ones

def obj(x):
    x1, x2, x3 = x
    return (2+x1)/(1+x2) - 3*x1 + 4*x3

LB = [0.1]*3; UB = [0.9]*3
bound = tuple(zip(LB,UB))
res = minimize(obj, ones(3), bounds = bound)
print(res.fun,'\n',res.success,'\n',res.x)

from scipy.optimize import minimize
from numpy import ones
def f(x):
    x1,x2,x3 = x
    return (2+x1)/(1+x2) - 3*x1 +4*x3
#定义上下限
LB = [0.1]*3; UB = [0.9, 0.9, 0.9]
bound = tuple(zip(LB,UB))
Rres = minimize(f,ones(3),bounds= bound)
print(Rres.fun,'\n',Rres.success,'\n',Rres.x)
