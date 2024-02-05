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

def bisectionMethod(f, a, b, Po, TOL):
    low = a
    high = b

    print (low, " ", high, " ", f(low), " ", f(high))
    if f(low) * f(high) >= 0:
        return
    while high - low >= TOL:
        c = (low + high) / 2
        if (f(c) == 0.0):
            break
        if f(c) * f(low) < 0:
            high = c
        else:
            low = c
    return c

'''
    while steps < maxIter:
        m = (low + high) / 2.0
        if m == 0 or abs(f(high - low)) < TOL:
            high = m
        else:
            low = m
        steps += 1

    estimate = (low + high) / 2.0
    return estimate, steps
'''

#f = lambda x: x**3 - 2
#f = lambda x: (x-2)**2
f = lambda x: x ** (1/3)

print(f(-1))

#val = rootSolver(f, -1, 1, 0.5, 0.01)
#print ("Root: ", val)
