import math

# function to solve for roots
def rootSolver(f, a, b, Po, TOL):
    low = a
    high = b

    steps = 1
    maxIter = 1000

    while steps < maxIter and abs(high - low) > TOL:
        if f(high) - f(low) == 0:
            return bisectionMethod(f, a, b, Po, TOL)
        c = high - ((f(high) * (high - low)) / (f(high) - f(low)))
        high, low = c, high
        steps += 1

    if c.real >= a and c.real <= b:
        return c.real
    else:
        return bisectionMethod(f, a, b, Po, TOL)

# function to solve root using bisection method
def bisectionMethod(f, a, b, Po, TOL):
    low = a
    high = b

    while high - low >= TOL:
        c = (low + high) / 2
        if (f(c) == 0.0):
            break
        if f(c) * f(low) < 0:
            high = c
        else:
            low = c
    return c


f1 = lambda x: x**3 - 2 #Defining functions
f2 = lambda x: (x-2)**2
f3 = lambda x: x ** (1/3)

val = rootSolver(f1, 0, 2, 1, 0.01) #Calling root finding functions
print ("Root for x^3 -2 on [0, 2]: ", val)
val = rootSolver(f2, 1, 3, 1.5, 0.01)
print ("Root for (x-2)^2 on [1, 3]: ", val)
val = rootSolver(f3, -1, 1, 0.5, 0.01)
print ("Root for x^(1/3) on [-1, 1]: ", val)
