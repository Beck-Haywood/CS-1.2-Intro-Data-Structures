from test_time import time_it
from util import read_text_file
import sys 
import os 

def make_histogram(file_name):
    f = open(file_name, 'r')
    words = f.read().split()
    histogram = {}
    
    for word in words:
        word = word.lower()
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram        

def unique_words():
    histogram = make_histogram(file_name)
    print(len(histogram))
def frequency():
    word = input("Enter a word to check how many times it is said in the text document! ")
    histogram = make_histogram(file_name)
    print(histogram[word])

if __name__ == "__main__":
    file_name = sys.argv[1:]
    file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/words.txt'
    make_histogram(file_name)
    unique_words()
    frequency()

    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))
