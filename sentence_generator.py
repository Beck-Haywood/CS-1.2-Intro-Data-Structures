from dictogram import Dictogram
from histogram import read_word_file, make_histogram, random_word_frequency
from sample import sample_word
import random
import sys
def markov(words):
    """
    """
    couple = []
    #Creates a list of every couple in the corpus
    for index in range(len(words)-1):
        couple.append((words[index], words[index+1]))

    #print(couple)

    markov_dict = {}
    #Loops through each couple and makes a markov dictonary with 1st word and following word as value
    for first, second in couple:
        if first in markov_dict.keys():
            markov_dict[first].append(second)
        else:
            markov_dict[first] = [second]
    #print(markov_dict)
    return markov_dict
def random_word(markov, word):
    word_options = markov.get(word)
    print(word_options)
    rng = random.randint(0, len(word_options)-1)
    #print(word_options[rng])
    return word_options[rng]
def generate_sentence(markov, length):
   # word_list = read_word_file('words.txt')
   # histogram = make_histogram(word_list)
   # starting_word = random_word_frequency(histogram)
   # word_options = markov.get(starting_word)
   # while word_options == None:
   #     starting_word = random_word_frequency(histogram)
   #     word_options = markov.get(starting_word)
    # sentence_list = []
    # word = random_word(markov, starting_word)
    # sentence_list.append(word)
    # for _ in range(length):
    #     word = random_word(markov, word)
    #     sentence_list.append(word)
    # sentence = ''
    # for word in sentence_list:
    #     sentence += f'{word} ' #Innefficent could add it to list then join it together
    # return sentence
    pass


if __name__ == "__main__":
    file_name = sys.argv[1]

    word_list = read_word_file(file_name)

    bruh = markov(word_list)

    random_word(bruh, 'fish')

    print(generate_sentence(bruh, 5))
