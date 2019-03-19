import click
from interactive_dictionary import translate


@click.command()
@click.option(
    '--word',
    '-w',
    help='Word to translate'
)


def translation(word):
    outcome = translate(word)

    if type(outcome) == list:
        for i in range(len(outcome)):
            print(str(i + 1) + '. ' + outcome[i])
    else:
        print(outcome)


if __name__ == "__main__":
    translation()
