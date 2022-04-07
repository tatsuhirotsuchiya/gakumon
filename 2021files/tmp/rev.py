def reverse(str):
    res = ""
    for c in str:
        print(res)
        res = c + res
    return res

s = input()
print(reverse(s))
