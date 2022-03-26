import random
from words import words

def getvalidword(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = getvalidword(words)
    wordletters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters)>0:
        print('You have used these letters: ' ,' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if used_letter in wordletters:
                    wordletters.remove(user_letter)

        elif user_letter in used_letters:
                print('You have already used that character. Please try again!! ')

        else:
                print('Invalid character.Please try again.')

user_input = input('Type Something: ')
print(user_input)