# Simple English Dictionary

import json
from difflib import get_close_matches
import sys


DATA = json.load(open("data.json"))


def translate(word):
    while not word:
        word = input("\nNo word entered. Please enter a word to translate: ")

    word = word.lower()
    if word in DATA.keys():
        decorate_definition(word)
        return DATA[word]

    elif word.title() in DATA:
        decorate_definition(word.title())
        return DATA[word.title()]

    elif word.upper() in DATA:
        decorate_definition(word.upper())
        return DATA[word.upper()]

    else:
        close_matches = get_close_matches(word, DATA.keys(), 1, cutoff=0.8)

        if close_matches:
            close_match = close_matches[0]
            yn = input(
                "\nDid you mean %s?\nEnter Y if yes, or N if no:  " % close_match
            )

            if yn.lower() == "y":
                decorate_definition(close_match)
                return DATA[close_match]
            else:
                translate(word=input("Please enter a word again"))

        else:
            return "Neither this or similar word/phrase is in dictionary.\n"


def decorate_definition(word):
    print("\n{:*^60}".format(" %s - definition: ") % word)


def handle_outcome(wtt):  # wtt - word to translate
    outcome = translate(wtt)
    if type(outcome) == list:
        for i in range(len(outcome)):
            yield str(i + 1) + ". " + outcome[i]
    else:
        yield outcome


if __name__ == "__main__":

    if len(sys.argv) > 1:
        to_translate = " ".join(sys.argv[1::])
        final_message = handle_outcome(to_translate)
        for message in final_message:
            print(message)

    else:
        print()
        print(
            " Welcome to simple English Dictionary! ".center(60, "*")
            + "\n\nDictionary contains 49537 available words/phrases."
            '\nTo finish the program enter "exit".'
            "\nEnter word/phrase to check if the definition is in Dict."
        )

        while True:
            user_input = input("\nEnter a command or a word to translate: ")
            if user_input == "exit":
                break

            else:
                final_message = handle_outcome(user_input)
                for message in final_message:
                    print(message)
