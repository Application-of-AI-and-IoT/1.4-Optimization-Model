from scipy.optimize import linprog
c = [2, 3]
A = [[1, 1]]
b = [10]
x0_bounds = (0, 9)
x1_bounds = (0, 8)
res = linprog(c, A_eq=A, b_eq=b, bounds=[x0_bounds, x1_bounds])
print('Optimal Cost of Generation =',-res.fun)
print('Optimal Generation:',res.x)