# hangman
import random
def get_word():
    WORDS = "turaco shoebill tropicbird eagle crane peafowl dove \
            hummingbird puffin cassowary lorikeet flamingo penguin \
            heron booby owl toucan".split()
    offset = random.randint(0, len(WORDS)-1)
    return WORDS[offset]

def unmask_word(word, letters):
    st = ""
    for c in word:
        for l in letters:
            if c == l:
                st = st + c
                break
        else:
            st = st + "_"
    return st

def is_correct(secretword, letters):
    for c in secretword:
        for l in letters:
            if c == l:
                break
        else:
            return False
    return True

def input_letter():
    while True:
        print("英文字を1字入力")
        st = input()
        st = st.lower()
        if len(st) == 1:
            if st in 'abcdefghijklmnopqrstuvwxyz':
                break
    return st

life = 5 # (1)
inputLetters = ""
secret = get_word()
st = unmask_word(secret, inputLetters)
print("life:", life)
print(st)
while is_correct(secret, inputLetters) == False:
    inputLetters = inputLetters + input_letter()
    st_next = unmask_word(secret, inputLetters) # (2)
    print(st_next)
    if st == st_next: # (3)
        life = life - 1
        print("life:", life)
        if life <= 0:
             break # (4)
    st = st_next # (5)

print(secret)


