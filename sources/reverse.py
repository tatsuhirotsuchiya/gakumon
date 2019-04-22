def reverse(str):
    res = ""
    for c in str:
        res = c + res
    return res

s = input()
print(reverse(s))

