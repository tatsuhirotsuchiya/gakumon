# a, b, c どれが一番大きい？
print("a?")
a = int(input())
print("b?")
b = int(input())
print("c?")
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
