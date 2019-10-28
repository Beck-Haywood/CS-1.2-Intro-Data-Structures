from test_time import time_it
from util import read_text_file
import sys 
import os 

def make_histogram(file_name):
    #Using dictionarys
    
    f = open(file_name, 'r')
    words = f.read().split()
    histogram = {}
    
    for word in words:
        word = word.strip('?!,.').lower()
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram   
    
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
    '''
    '''
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
    '''
def unique_words():
    #Using dictionarys
    
    histogram = make_histogram(file_name)
    print(len(histogram))
    
    #Using List of lists
    '''
    histogram = make_histogram(file_name)
    print(len(histogram))
    '''
    #Using List of tuples
    '''
    histogram = make_histogram(file_name)
    print(len(histogram))
    #Result 980
    '''
def frequency():
    #Using dictionarys
    
    word = input("Enter a word to check how many times it is said in the text document! ")
    histogram = make_histogram(file_name)
    print(histogram[word])
    
    '''
    #Using List of lists
    word = input("Enter a word to check how many times it is said in the text document! ") 
    histogram = make_histogram(file_name)
    for item in histogram:
        if item[0] == word:
            print(item[1])
    '''
    #Using List of tuples
    '''
    word = input("Enter a word to check how many times it is said in the text document! ") 
    histogram = make_histogram(file_name)
    for item in histogram:
        if item[0] == word:
            print(item[1])
    '''
if __name__ == "__main__":
    file_name = sys.argv[1:]
    file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/words.txt'
    make_histogram(file_name)
    unique_words()
    frequency()

    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))
