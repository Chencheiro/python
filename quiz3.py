def square_root(x):
    if x >= 0:
        x = x**(1.0/2.0)
        return(x)
    else:
        return("\"Square root of negative numbers would be imaginary, so we don't want to do that.\" - Obi-Wan Kenobi")

def cube_root(x):
    if x >= 0:
        x = x**(1.0/3.0)
    else:
        x = -abs(x)**(1.0/3.0)
    return(x)



x = int(input("Give me a number and I am going to calculate the square and the cube root: "))
sqrt = square_root(x)
cbrt = cube_root(x)
print("Square root: {}".format(sqrt))
print("Cube root: {}".format(cbrt))
