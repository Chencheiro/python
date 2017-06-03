def fibonacci(a):
    count = 4
    x = 0
    y = 1
    z = x + y
    while count <= a:
        count += 1
        x = y
        y = z
        z = x + y
    return(z)

print(fibonacci(5))
