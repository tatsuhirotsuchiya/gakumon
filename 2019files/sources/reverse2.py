def reverse(str):
    if str == "":
        return ""
    return reverse(str[1:]) + str[0]

s = input()
print(reverse(s))
