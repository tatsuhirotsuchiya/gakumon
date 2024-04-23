def is_prime(number):
    for i in range(2, number - 1):
        if number % i == 0:  # number is not prime
            return False

    return True  # number is prime


for i in range(2, 100):
    if is_prime(i):
        print(i)
