def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i

    return result


for i in range(1, 10):
    a = factorial(i)
    print("i", i, "f(i)", a)

