import random
from histogram import make_histogram, read_word_file
import sys
from timeit import default_timer as timer
import os

def sample_word(histogram):
    """Returns a word based on weighted probability
    """
    total_words = sum(histogram.values())
    rng = random.randint(1, total_words)
    count = 0
    for key in histogram.keys():
        count += histogram[key]
        if rng <= count:
            return key

def random_sentence(histogram, words):
    """Returns a string of a randomly generated sentence
    """
    sentence_list = []
    for _ in range(words):
        word = sample_word(histogram)
        sentence_list.append(word)
    sentence = ''
    for word in sentence_list:
        sentence += f'{word} '
    #print(sentence)
    return sentence
    
if __name__ == "__main__":
    word_list = read_word_file(sys.argv[1])
    histogram = make_histogram(word_list)
    start = timer()
    #print(sample_word(histogram))
    print(random_sentence(histogram, 10))
    end = timer()
    print(end - start)


    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))