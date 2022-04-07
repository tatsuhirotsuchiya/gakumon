import random
JAN = ('グー', 'チョキ', 'パー')

awin = 0
bwin = 0
while awin < 3 and bwin < 3:
    a = random.randint(0,2)
    b = ""
    while b != '0' and b != '1' and b != '2':
        print(0, JAN[0], 1, JAN[1], 2, JAN[2], '?')
        b = input()
    b = int(b) # 入力を整数に変換
    print('こちら', JAN[b])
    print('あいて', JAN[a])

    if a == b:
        print('あいこ')
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        print('まけ :-(')
        awin = awin + 1
        print('あいて: ', awin, ' こちら: ', bwin)
    else:
        print('かち :-)')
        bwin = bwin + 1
        print('あいて: ', awin, ' こちら: ', bwin)
        
