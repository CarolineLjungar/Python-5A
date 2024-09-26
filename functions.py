def double(n): # n är parameter
    return 2*n

def triple(n):
    return 3*n

def quadruple(n):
    return double(double(n))

def funky(n, m):
    return triple(n) + quadruple(m)

print(double(2)) # 2 är argument