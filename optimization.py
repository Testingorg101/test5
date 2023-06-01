from pulp import LpProblem, LpVariable, LpMaximize, LpStatus

# Create the LP problem
problem = LpProblem("Business Optimization", LpMaximize)

# Define the decision variables
x = LpVariable("x", lowBound=0)  # Number of product X to produce
y = LpVariable("y", lowBound=0)  # Number of product Y to produce

# Define the objective function
profit = 40 * x + 30 * y  # Profit function
problem += profit

# Define the constraints
constraint1 = 2 * x + y <= 100  # Constraint 1: Resource limitation
constraint2 = x + 2 * y <= 80   # Constraint 2: Resource limitation
problem += constraint1
problem += constraint2

# Solve the problem
status = problem.solve()

# Print the status of the solution
print("Status:", LpStatus[status])

# Print the optimal values of the decision variables
print("Optimal Solution:")
print("x =", x.value())
print("y =", y.value())

# Print the optimal objective value
print("Optimal Profit =", profit.value())
