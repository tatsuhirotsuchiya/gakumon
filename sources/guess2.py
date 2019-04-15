# これは数あてゲームです
import random

number = random.randint(1, 10)

print('この数は，1から10までの整数です')
guess = None #　Noneは値がないことをしめす，特別な記号
while number != guess:
    print('数をあててみて？')
    guess = input()
    guess = int(guess)

print('あたり！')
