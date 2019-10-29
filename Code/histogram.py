from test_time import time_it
from util import read_text_file
import sys 
import os 
import random
import numpy as np


def make_histogram(file_name):
    #Using dictionarys
    
    f = open(file_name, 'r')
    words = f.read().split()
    f.close()
    histogram = {}
    for word in words:
        #word = word.replace('"', '')
        word = word.strip('?!,.-*[]:').lower()
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram   
    
def unique_words():
    #Using dictionarys
    
    histogram = make_histogram(file_name)
    print(len(histogram))
    
def frequency():
    #Using dictionarys
    
    word = input("Enter a word to check how many times it is said in the text document! ")
    histogram = make_histogram(file_name)
    print(histogram[word])
    frequent_word = max(histogram, key=histogram.get)
    least_frequent_word = min(histogram, key=histogram.get)

    occursences1 = histogram.get(frequent_word)
    occursences2 = histogram.get(least_frequent_word)

    print(f'This is the most frequent word: {frequent_word}. This many times {occursences1}')
    print(f'This is the least frequent word: {least_frequent_word}. This many times {occursences2}')

    #print(sorted(histogram, key=histogram.get, reverse=True))
    sortedwords = sorted(histogram, key=histogram.get, reverse=True)
    new = ''
    place = 0
    for word in sortedwords: 
        place += 1
        value = histogram.get(word)
        new += (str(place) + '. ' + word + '    Occurrences: ' + str(value) + '\n')

    file = open('sortedwords.txt', 'w+')
    file.write(new)
    file.close()
def random_word():
    histogram = make_histogram(file_name)
    random_word = random.choice(list(histogram.items()))
    print(random_word)
def random_word_frequency():
    histogram = make_histogram(file_name)
    f = open(file_name, 'r')
    words = f.read().split()
    f.close()
    #new_histogram = {}
    #for word in words:
    #    #word = word.replace('"', '')
    #    word = word.strip('?!,.-*[]:').lower()
    #    new_histogram[word] = new_histogram.get(word, 0) + 1 
    new_histogram = histogram.copy()
    total_words = len(words)
    for word in histogram:
        frequency = histogram.get(word)
        #This one works but we need to change it to a seperate histogram
        #histogram[frequency / total_words] = histogram.pop(word)
        #new_histogram[frequency / total_words] = new_histogram.pop(word)
        #value = new_histogram.get[word]
        '''
        new_histogram[frequency / total_words] = new_histogram[word]
        del new_histogram[word]
        '''
        new_histogram[word] = (frequency / total_words)
        #print(frequency / total_words)
        #print(new_histogram)
        list_of_probabilites = []
        list_of_unique_words = []
    for word in new_histogram:
        list_of_probabilites.append(new_histogram[word])
    for word in new_histogram:
        list_of_unique_words.append(word)
    #print(list_of_unique_words)
    test = np.random.choice(a = list_of_unique_words, p = list_of_probabilites)
    return test
    #print(test)
def test_random_word_frequency():
    pass




if __name__ == "__main__":
    file_name = sys.argv[1:]
    #file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/words.txt'
    file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/poemtest.txt'
    make_histogram(file_name)
    x = 0
    while x < 10000:
        random_word_frequency()

        x += 1

    random_word_frequency()
    #unique_words()
    #frequency()
    #random_word()

    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))

#Using List of lists
    '''
    f = open(file_name, 'r')
    words = f.read().split()
    histogram = []
    for word in words:
        word = word.strip('?!,.').lower()
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else:
            histogram.append([word, 1])
    #print(histogram)
    return histogram
    
    #Using List of lists
    word = input("Enter a word to check how many times it is said in the text document! ") 
    histogram = make_histogram(file_name)
    for item in histogram:
        if item[0] == word:
            print(item[1])
    
    #Using List of lists
    
    histogram = make_histogram(file_name)
    print(len(histogram))
    

    
    #List of tuples
    
    f = open(file_name, 'r')
    words = f.read().split()
    histogram = []
    for word in words:
        word = word.strip('?!,.').lower()
        for i, item in enumerate(histogram):
            if item[0] == word:
                item = (word, item[1] + 1)
                histogram[i] = item
                break
        else:
            histogram.append((word, 1))
    print(histogram)
    return histogram
    
    #Using List of tuples
    
    histogram = make_histogram(file_name)
    print(len(histogram))
    #Result 980
    
    #Using List of tuples
    
    word = input("Enter a word to check how many times it is said in the text document! ") 
    histogram = make_histogram(file_name)
    for item in histogram:
        if item[0] == word:
            print(item[1])
    '''