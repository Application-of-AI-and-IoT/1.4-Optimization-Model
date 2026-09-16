# 1.4 Optimization Model

This example uses linear programming to minimize the generation cost of two generators while meeting a total demand of 10 units. The same model is implemented in Python and MATLAB using `linprog`.

## Mathematical model

Let `x1` and `x2` represent the output of the two generators. Minimize:

```text
Cost = 2*x1 + 3*x2
```

Subject to:

```text
x1 + x2 = 10    (total generation meets demand)
0 <= x1 <= 9    (generator 1 capacity)
0 <= x2 <= 8    (generator 2 capacity)
```

The cost coefficients are 2 and 3 per unit of generation. The programs do not specify physical units or a currency.

## Files

| File | Description |
| --- | --- |
| [program_1_4.py](program_1_4.py) | Python implementation using SciPy's `linprog`. |
| [program_1_4.m](program_1_4.m) | MATLAB implementation using Optimization Toolbox's `linprog`. |

Both programs supply the cost coefficients, the equality constraint, and lower and upper generation bounds to the solver, then print the cost and generation values.

## Run the Python program

Install Python 3 and SciPy, then run these commands from the project folder:

```bash
python3 -m pip install scipy
python3 program_1_4.py
```

Output:

```text
Optimal Cost of Generation = -21.0
Optimal Generation: [9. 1.]
```

## Run the MATLAB program

MATLAB with Optimization Toolbox is required. Set MATLAB's Current Folder to this project folder, then enter:

```matlab
program_1_4
```

The program prints a cost of `-21.0000` and a generation column vector containing `9` and `1`. Vector display formatting depends on the current MATLAB format setting.

## Interpreting the result

The optimal generation is `x1 = 9` and `x2 = 1`. Generator 1 has the lower unit cost, so it supplies its full capacity; generator 2 supplies the remaining demand. The minimum objective value is:

```text
2*9 + 3*1 = 21
```

**Cost display note:** Both scripts currently negate the solver's objective value when printing it (`-res.fun` in Python and `-fval` in MATLAB). Consequently, they display `-21`, although the minimized cost is positive `21`. To display the actual minimum cost, use `res.fun` and `fval` without the minus sign.

## Developer
<p>
 <img src="https://venkataswamy.in/images/img1.jpg" alt="Venkat" width="100"> 
</p>

**[Venkataswamy R](https://github.com/venkataswamyr)**<br>
Associate Professor<br>
Department of Electrical and Electronics Engineering<br>
School of Engineering and Technology<br>
Christ (Deemed to be University)<br>
Bengaluru-560074, India

- Office: 080-4012-9961
- Mobile: +91-7829222446
- Website: [venkataswamy.in](https://venkataswamy.in)
