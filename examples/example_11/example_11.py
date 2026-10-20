from sympy.abc import *
from sympy import diff,dsolve,simplify,Function,sin

y = Function('y')
eq = diff(y(x),x,2) + 2*diff(y(x),x) + 2*y(x)
#define the function
con = {y(0):0, diff(y(x),x).subs(x,0):1}
y =dsolve(eq, ics = con)
print(simplify(y))

y = Function('y')
eq = diff(y(x),x,2) + 2*diff(y(x),x) + 2*y(x) - sin(x)
con = {y(0):0, diff(y(x),x).subs(x, 0): 1}
y = dsolve(eq, ics = con)
print(simplify(y))

y = Function('y')
eq = diff(y(x),x,2) + 2*diff(y(x), x) + 2*y(x) - sin(x)
cons = {y(0):0, diff(y(x),x).subs(x, 0): 1}
y = dsolve(eq, ics = cons)
print(simplify(y))