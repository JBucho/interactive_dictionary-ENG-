# Simple English Dictionary

import json
from difflib import get_close_matches


DATA = json.load(open("data.json"))


def translate(word):
    while not word:
        word = input('\nNo word entered. Please enter a word to translate: ')

    word = word.lower()
    if word in DATA.keys():
        print('\n{:*^60}'.format(' %s - definition: ') % word)
        return DATA[word]
    elif word.title() in DATA:
        print('\n{:*^60}'.format(' %s - definition: ') % word.title())
        return DATA[word.title()]
    else:
        close_matches = get_close_matches(word, DATA.keys(), 1, cutoff=0.8)

        if close_matches:
            close_match = close_matches[0]
            yn = input('\nDid you mean %s?\nEnter Y if yes, or N if no:  ' % close_match)

            if yn.lower() == 'y':
                print('\n{:*^60}'.format(' %s - definition: ') % close_match)
                return DATA[close_match]
            else:
                return '\nPlease enter a word again.'

        else:
            return "Neither this or similar word is in dictionary.\n"


if __name__ == '__main__':
    print()
    print(' Welcome to simple English Dictionary! '.center(60, '*')
          + '\n\nDictionary contains 49537 available words/phrases.'
            '\nTo finish the program enter "exit".'
            '\nEnter word/phrase to check if the definition is in Dict.')

    while True:
        user_input = input('\nEnter a command or a word to translate: ')
        if user_input == 'exit':
            break

        else:
            outcome = translate(user_input)
            if type(outcome) == list:
                for i in range(len(outcome)):
                    print(str(i + 1) + '. ' + outcome[i])
            else:
                print(outcome)
