def exponentiate(x,y):
    """ Takes two arguments returns its exponentiation"""
    return x**y

output = exponentiate(2,4)
print(exponentiate.__doc__)

def raise_to_fourth_power(a):
    """Takes one argument and returns its 4th power"""
    
    return exponentiate(a,4)

square = lambda x,y: x**y
cube = lambda x,y: x**y


print(square(2,2))
print(cube(2,3))
print(raise_to_fourth_power(2))