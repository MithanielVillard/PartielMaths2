PI = 3.14159265358979

def factorial( n: int ) -> float:
    out: int = 1
    for i in range( 2, n+1 ):
        out *= i
    return out

def cos( x: float, order: int = 30 ) -> float:
    out: float = 1
    signe: int = -1
    for k in range( 2, order, 2 ):
        out += x**k / factorial(k) * signe
        signe = -signe
    return out

def sin( x: float, order: int = 30 ) -> float:
    return cos( x + PI/2, order )

# def sqrt( x: float ) -> float: # Pourquoi y'a une fonction sqrt ?
#     n: float = 1
#     for _ in range( 50 ):
#         n = ( n + x/n ) * 0.5
#     return n

def df_frontward(i, ip1, h):
    return (ip1 - i)/h