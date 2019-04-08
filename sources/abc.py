# a, b, c どれが一番大きい？
print("a?")
a = int(input())
print("b?")
b = int(input())
print("c?")
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)       
else:
    if b > c:
        print(b)
    else:
        print(c)
