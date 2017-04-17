import random
import sys

def mimick(file, length=5, slength=5, extra_random=False):
    #repeatable_words = ['the', 'in', 'this', 'a', 'because', 'on', 'of', 'for', 'with']
    words = dict()
    with open(file, 'r') as f:
        neat_line = f.read().replace(",", '').lower().replace(".", "").split(" ")

        # Build the mimicking Dictionary.
        for index, word in enumerate(neat_line):
            next_words = neat_line[index+1:index+slength]
            #words[word] = words.get(word, next_words) + next_words
            try:
                words[word] + next_words
            except KeyError:
                words[word] = next_words
                
        # Dictionary has been built.
        message = list()
        sample = random.sample(words.keys(), length)

        for key in sample:

            seed = set(words[key])

            for index, word in enumerate(seed):
                message.append(word)

        message = " ".join(message)
        print(message)


file = sys.argv[1]
mimick(file)
