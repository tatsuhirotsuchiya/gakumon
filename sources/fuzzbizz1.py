for i in range(1,51):
    if i % 15 == 0:
        print("Fuzz-Bizz")
    else:
        if i % 5 == 0:
            print("Bizz")
        else:
            if i % 3 == 0:
                print("Fuzz")
            else:
                print(i)
            
