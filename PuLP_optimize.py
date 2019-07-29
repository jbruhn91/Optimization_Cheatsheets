import pulp
import random


duration=10
# initializing LP
LP = pulp.LpProblem('LP',pulp.LpMaximize)  


#-----------CREATING VARIABLES
#Option 1:
#x = pulp.LpVariable.dicts("x", range(duration), cat=pulp.LpBinary)

#Option 2:
#y = {}
#for i in range(duration):
#	y[i] = pulp.LpVariable("y_"+str(i), cat='Binary')	
#----------------------------

# adding variables
x1 = pulp.LpVariable("x1", cat='Integer', lowBound=0)	
x2 = pulp.LpVariable("x2", cat='Integer', lowBound=0)	

#constraints
LP += 100>= x1+2*x2
LP += 100>= 2*x1+x2
	
#obj function
LP += 20*x1+30*x2

# if mip=False -> Integer constraints are ignored
# if msg=False -> Optimization script is not displayed
status = LP.solve(pulp.CPLEX_PY(mip=True, msg=False, timeLimit=15,epgap=None))

print( 'LP status: ' + pulp.LpStatus[status] + '')
print(x1.value(),x2.value())