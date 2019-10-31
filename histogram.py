#from test_time import time_it
#from util import read_text_file
import sys 
import os 
import random
import numpy as np
from timeit import default_timer as timer

def read_word_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    return words

def make_histogram(word_list):
    #Using dictionarys
    #word_list = read_word_file(file_name)
    histogram = {}
    for word in word_list:
        #word = word.replace('"', '')
        word = word.strip('?!,.-*[]:').lower()
        histogram[word] = histogram.get(word, 0) + 1 
    #print(len(words))
    return histogram   
    
def unique_words(histogram):
    """This function returns the length of the histogram
    """
    return len(histogram)

def frequency(histogram, word):
    '''This function asks for a histogram and a word and outputs the frequency for the specific word
    '''
    word = word.lower()
    if word in histogram.keys():
        return histogram[word]
    else:
        return 0

def random_word(histogram):
    """Returns a random word from the histogram
    """
    return random.choice(list(histogram.keys()))

def random_word_frequency(histogram):
    """makes two lists for the numpy random.choice to operate. Returns a random word
    """
    #Reads file to use words
    #Copys histogram so we can edit it in a loop without breaking the loop
    new_histogram = histogram.copy()
    #Defining total words
    total_words = sum(histogram.values())
    #This makes a new histogram that has values of percentage frequency/total_words. Instead of the frequency
    for word in histogram:
        frequency = histogram.get(word)
        
        new_histogram[word] = (frequency / total_words)
    #Initilizes the lists
    list_of_probabilites = []
    list_of_unique_words = []
    #Creates the weighed word list
    for word in new_histogram:
       list_of_probabilites.append(new_histogram[word])
    #Creates the unique word list
    for word in new_histogram:
       list_of_unique_words.append(word)
    #The numpy function that takes the array, and the list of weight for each item in the array
    random_word = np.random.choice(a = list_of_unique_words, p = list_of_probabilites)
    return random_word

def write_histogram_to_file(histogram, file_name):
   """Writes a histogram to a file
   """
   '''total_words = sum(histogram.values())
   
   with open(file_name, 'w+') as file:
       for key in histogram.keys():
           file.write(f'{key} {histogram[key]/total_words}\n')'''
   pass

if __name__ == "__main__":
    file_name = sys.argv[1]
    start = timer()
    word_list = read_word_file(file_name)
    histogram = make_histogram(word_list)
    end = timer()
    print(end - start)
    #write_histogram_to_file(histogram, 'wat.txt')
    #print(frequency(histogram, 'it'))
    #print(random_word_frequency(histogram))


    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))