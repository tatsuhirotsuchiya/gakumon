import random
jan = ('グー', 'チョキ', 'パー')

while True:
    a = random.randint(0,2)
    b = ""
    while b != '0' and b != '1' and b != '2':
        print(0, jan[0], 1, jan[1], 2, jan[2], '?')
        b = input()
    b = int(b) # 入力を整数に変換
    print('こちら', jan[b])
    print('あいて', jan[a])

    if a == b:
        print('あいこ')
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        print('まけ :-(')
        break
    else:
        print('かち :-)')
        break
