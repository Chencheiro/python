def minimum_three(x, y, z):
    if x <= y and x <= z:
        min = x
    elif y <= z:
        min = y
    else:
        min = z
    return(min)

def sum_squares(x, y, z):
    sum_of_squares = x**2 + y**2 + z**2
    return(sum_of_squares)



count = 1
x = 0
y = 0
z = 0
while count <= 3:
    num = int(input("Give me a number: "))
    count += 1
    x = y
    y = z
    z = num
print("The minimum is:",minimum_three(x, y, z),"and the sum of squares is:",sum_squares(x, y, z))
