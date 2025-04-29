# hangman
import random


def get_word():
    WORDS = "turaco shoebill tropicbird eagle crane peafowl dove \
            hummingbird puffin cassowary lorikeet flamingo penguin \
            heron booby owl toucan".split()
    index = random.randint(0, len(WORDS)-1)
    return WORDS[index]


def unmask_word(word, letters):
    st = ""
    for c in word:
        tmp = "_"
        for ltr in letters:
            if c == ltr:
                tmp = c
        st = st + tmp
    return st


def is_correct(secret_word, letters):
    for c in secret_word:
        is_covered = False
        for ltr in letters:
            if c == ltr:
                is_covered = True
        if not is_covered:
            return False
    return True


def input_letter():
    while True:
        print("英文字を1字入力")
        st = input()
        if len(st) == 1 and st in 'abcdefghijklmnopqrstuvwxyz':
            return st


life = 6  # <1>
letters = ""
secret = get_word()
st = unmask_word(secret, letters)
print("life:", life)
print(st)
while not is_correct(secret, letters):
    letters = letters + input_letter()
    st_next = unmask_word(secret, letters)  # <2>
    print(st_next)
    if st == st_next:  # <3>
        life = life - 1
        print("life:", life)
        if life <= 0:
            break  # <4>
    st = st_next
