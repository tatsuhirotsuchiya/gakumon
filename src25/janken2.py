import random
JAN = ['グー', 'チョキ', 'パー']

a_win = 0
b_win = 0
while a_win < 3 and b_win < 3:
    a = random.randint(0, 2)
    b = None
    while b != '0' and b != '1' and b != '2':
        print(0, JAN[0], 1, JAN[1], 2, JAN[2], '?')
        b = input()
    b = int(b)  # 入力を整数に変換
    print('こちら', JAN[b])
    print('あいて', JAN[a])

    if a == b:
        print('あいこ')
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        print('まけ :-(')
        a_win = a_win + 1
        print('あいて: ', a_win, ' こちら: ', b_win)
    else:
        print('かち :-)')
        b_win = b_win + 1
        print('あいて: ', a_win, ' こちら: ', b_win)
