# a, b, c どれが一番大きい？
print("a?")
a = input()
print("b?")
b = input()
print("c?")
c = input()

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
