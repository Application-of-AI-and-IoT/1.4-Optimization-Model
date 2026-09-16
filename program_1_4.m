clc;
clear all;
c = [2; 3];
Aeq = [1 1];
beq = 10;

lb = [0; 0];
ub = [9; 8];

[x, fval] = linprog(c, [], [], Aeq, beq, lb, ub);

fprintf('Optimal Cost of Generation = %.4f\n', -fval);
disp('Optimal Generation:')
disp(x)

