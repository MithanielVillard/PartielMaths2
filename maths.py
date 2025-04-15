PI = 3.14159265358979

def factorial(n):
    out = 1
    for i in range(2, n+1):
        out *= i
    return out

def cos(x : float, order : int = 30):
    out = 1
    signe = -1
    for k in range(2, order, 2):
        out += x**k / factorial(k) * signe
        signe = -signe
    return out

def sin(x : float, order : int = 30):
    #sin(x) = cos(x+PI/2)
    return cos(x + PI/2, order)

def sqrt(x):
    n = 1
    for i in range(50):
        n = (n + x/n) * 0.5
    return n

def df_frontward(i, ip1, h):
    return (ip1 - i)/h