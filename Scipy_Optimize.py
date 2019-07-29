import numpy as np
from scipy.optimize import minimize


def objective(x):
    return -20*x[0]-30*x[1]

def constraint1(x):
    return 100-(x[0]+2*x[1])

def constraint2(x):
    return 100-(2*x[0]+x[1])

# initial guesses
x0 = np.zeros(2)
x0[0]=1
x0[1]=1

##########
# show initial objective
print('Initial Objective: ' + str(-objective(x0)))

# bounds
b = (0,1000)
bnds = (b, b)

#constraints
con1 = {'type': 'ineq', 'fun': constraint1} 
con2 = {'type': 'ineq', 'fun': constraint2}
cons = ([con1,con2])

#initialize and solve
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)

x = solution.x

# show final objective
print('Final Objective: ' + str(-objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
