import random
def get_word():
    WORDS = "turaco shoebill tropicbird eagle crane peafowl dove \
            hummingbird puffin cassowary lorikeet flamingo penguin \
            heron booby owl toucan".split()
    index = random.randint(0, len(WORDS)-1)
    return WORDS[index]

# print(get_word())

def unmask_word(word, letters):
    st = ""
    for c in word:
        tmp = "_"
        for l in letters:
            if c == l:
                tmp = c
        st = st + tmp
    return st

def input_letter():
    while True:
        print("英文字を1字入力")
        st = input()
        if len(st) == 1 and st in 'abcdefghijklmnopqrstuvwxyz':
            return st

def is_correct(secretword, letters):
    for c in secretword:
        is_covered = False
        for l in letters:
            if c == l:
                is_covered = True
        if is_covered == False:
            return False
    return True


inputLetters = ""
secret = get_word()
st = unmask_word(secret, inputLetters)
print(st)
while is_correct(secret, inputLetters) == False:
    inputLetters = inputLetters + input_letter()
    print(inputLetters)
    st = unmask_word(secret, inputLetters)
    print(st)
