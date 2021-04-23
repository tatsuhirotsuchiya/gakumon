for i in range(1, 51):
    if i % 15 == 0:
        print("Fizz-Buzz")
    else:
        if i % 5 == 0:
            print("Buzz")
        else:
            if i % 3 == 0:
                print("Fizz")
            else:
                print(i)
            
