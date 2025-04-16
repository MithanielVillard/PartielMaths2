PI = 3.14159265358979

def factorial( n: int ) -> float:
    out: int = 1
    for i in range( 2, n+1 ):
        out *= i
    return out

def cos( x: float, order: int = 30 ) -> float:
    output: float = 1
    signe: int = -1
    for i in range( 2, order, 2 ):
        output += x**i / factorial(i) * signe
        signe = -signe
    return output

def sin( x: float, order: int = 30 ) -> float:
    return cos( x + PI/2, order )