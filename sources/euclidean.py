print('a?')
a = int(input())
print('b?')
b = int(input())

mod = a % b
while mod != 0:
    a = b
    b = mod
    mod = a % b
print(b)
