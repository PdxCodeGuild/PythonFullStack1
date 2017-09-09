import glob
import nltk
import os
import re
import string

PUNCTUATION = [rf'\{v}|' for v in string.punctuation]

SUPPORTED_FILE_TYPES = ['txt']

ARI_SCALE = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def print_line(length=60, char='-'):
    print(char * 60)

def list_diff(a, b):
    return [aa for aa in a if aa not in b]

def get_user_input(options):
    option_choice = 0

    while True:
        option_choice = input(f'Enter an option between 1 and {len(options.keys())}: ')
        option_choice = option_choice.strip()

        if option_choice == 'q':
            break
            os.exit(-1)

        if 0 < int(option_choice) <= len(options.keys()):
            option_choice = int(option_choice)
            break
        else:
            print(f'Invalid option \'{option_choice}\'.')

    return option_choice

def main_prompt():
    current_directory = os.path.realpath(__file__)
    books_directory = '/'.join(current_directory.split('/')[:-2])
    books_directory += '/books'

    for file_type in SUPPORTED_FILE_TYPES:
        book_files = glob.glob(books_directory+ f'/*.{file_type}')
        book_files += glob.glob(books_directory+ f'/**/*.{file_type}')

    options = list()

    for book_file in book_files:
        local_path = list_diff(book_file.split('/'), books_directory.split('/'))
        option = ('/'.join(local_path), book_file)
        options += [option]

    options = {i + 1 : v for i, v in enumerate(options)}

    max_option_key_length = len(str(max(options.keys())))

    print_line()
    print()
    print("To compute it's automated readability index,\n"
          "pick one of the files below:\n")
    print_line()
    print()
    [print(f'{str(k).rjust(max_option_key_length)}) {v[0]}') for k, v in options.items()]
    print('\nor\n\nq) Quit\n')

    option_choice = get_user_input(options)

    file_to_open = options[option_choice][1]

    ari_sentence_count = 0
    ari_word_count = 0
    ari_character_count = 0

    with open(file_to_open, 'r') as book:
        book_data = book.read()

        sentence_tokens = nltk.sent_tokenize(book_data)
        ari_sentence_count += len(sentence_tokens)

        for sentence in sentence_tokens:
            word_tokens = nltk.word_tokenize(sentence)
            ari_word_count += len(word_tokens)

            for word in word_tokens:
                ari_character_count += len(word)

    ari_result = 4.71 * \
                  (ari_character_count / ari_word_count) + \
                  0.5 * \
                  (ari_word_count / ari_sentence_count)  - \
                  21.43

    ari_result = int(ari_result)
    ari_result = max(ARI_SCALE.keys()) if ari_result > max(ARI_SCALE.keys()) else ari_result

    print(
f'''
--------------------------------------------------------

The ARI for the file, {file_to_open.split('/')[-1]}, is {ari_result}.
This corresponds to a {ARI_SCALE[ari_result]['grade_level']} level of difficulty
that is suitable for an average person {ARI_SCALE[ari_result]['ages']} years old.

--------------------------------------------------------
'''
    )

if __name__ == '__main__':
    main_prompt()
