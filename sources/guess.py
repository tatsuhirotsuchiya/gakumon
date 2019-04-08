# これは数あてゲームです
import random

number = random.randint(1, 20)

print('この数は，1から20までの整数です')

for i in range(5):
    print('数をあててみて？')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('小さすぎ')
    elif guess > number:
        print('大きすぎ')
    else:
        break

if guess == number:
    print('あたり！ トライした回数は' + str(i+1) + '回でした')
else:
    print('残念: 答えは' + str(number) + 'でした')
