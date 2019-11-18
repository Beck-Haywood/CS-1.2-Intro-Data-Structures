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
    #for word in sentence_list:
    #    sentence.append(word) #Innefficent could add it to list then join it together
    #','.join(sentence_list)
    test = ' '.join(sentence_list)
    test = test.capitalize()
    test += '.'
    return test
    
if __name__ == "__main__":

    random_walk_sentence()
   