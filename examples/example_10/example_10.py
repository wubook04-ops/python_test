from scipy import optimize as opt
import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0]**2 + x[1]**2 +x[2]**2 + 8

def constraint1(x):
    return x[0]**2 - x[1] +x[2]**2

def constraint2(x):
    return -(x[0] + x[1]**2 +x[2]**2 -20)

def constraint3(x):
    return -x[0] - x[1]**2 + 2

def constraint4(x):
    return x[1] + 2*x[2]**2 - 3

#bound limit
b = (0.0, None)
bnds = (b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'eq', 'fun': constraint3}
con4 = {'type': 'eq', 'fun': constraint4}
cons = ([con1, con2, con3, con4])
x0 = np.array([0, 0, 0])
solution = minimize(objective, x0 ,method= 'SLSQP', bounds = bnds, constraints= cons)
x = solution.x
print('目标值：'+ str(objective(x)))
print('答案为：',end='\n')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))