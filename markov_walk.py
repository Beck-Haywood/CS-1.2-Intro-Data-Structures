from histogram import *
from sample import random_sentence
from sentence_generator import markov, random_word

def random_walk_sentence():
    word_list = read_word_file('poemtest.txt')
    histogram = make_histogram(word_list)
    starting_word = random_word_frequency(histogram)
    markovv = markov(word_list)
    sentence_list = []
    word = random_word(markovv, starting_word)
    sentence_list.append(word)
    for _ in range(7):
        word = random_word(markovv, word)
        sentence_list.append(word)
    sentence = []
    
    s = ' '.join(sentence_list)
    s = s.capitalize()
    s += '.'
    return s

if __name__ == "__main__":

    random_walk_sentence()
   