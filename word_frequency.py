from argparse import _AppendAction
from os import remove
from typing import Text


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        text = text.read()
        clean_text = text.replace("\n", "").replace(".", "").replace("’", "").replace(
            ";", "").replace("_", "").replace(",", "").lower().split(' ')
        for word in clean_text:
            if word in STOP_WORDS and clean_text:
                clean_text.remove(word)


    print(clean_text)

    # .count(clean_text)


# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     with open(file) as text:
#         lines = text.readlines()

#         for line in lines:
#             line = line.replace(".", " ")
#             line = line.replace(chr(39), " ")
#             line = line.replace(";", " ")
#             line = line.replace("_", " ")
#             line = line.replace(",", " ")
#             line = line.lower()
#             line = line.split(' ')
#     print(line)
#     print(lines)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
