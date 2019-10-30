from test_time import time_it
from util import read_text_file
import sys 
import os 
import random
import numpy as np

def read_word_file(file_name):
    f = open(file_name, 'r')
    words = f.read().split()
    f.close()
    return words
def make_histogram():
    #Using dictionarys
    words = read_word_file(file_name)
    histogram = {}
    for word in words:
        #word = word.replace('"', '')
        word = word.strip('?!,.-*[]:').lower()
        histogram[word] = histogram.get(word, 0) + 1 
    #print(len(words))
    return histogram   
    
def unique_words():
    #Using dictionarys
    
    histogram = make_histogram()
    print(len(histogram))
    
def frequency():
    #Using dictionarys
    
    #word = input("Enter a word to check how many times it is said in the text document! ")
    histogram = make_histogram()
    #print(histogram[word])
    #frequent_word = max(histogram, key=histogram.get)
    #least_frequent_word = min(histogram, key=histogram.get)

    #occursences1 = histogram.get(frequent_word)
    #occursences2 = histogram.get(least_frequent_word)

    #print(f'This is the most frequent word: {frequent_word}. This many times {occursences1}')
    #print(f'This is the least frequent word: {least_frequent_word}. This many times {occursences2}')

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
    histogram = make_histogram()
    random_word = random.choice(list(histogram.items()))
    print(random_word)
def random_word_frequency_genjis_version():
    words = read_word_file(file_name)
    histogram = make_histogram()
    #Needs
    #List of frequencys
    #Random int of every frequency added up.
    list_of_frequencys = []
    histogram_words = []
    random_number = random.randint(1, len(words))
    count = 0
    index = 0
    for key in histogram:
        list_of_frequencys.append(histogram[key])
    for word in histogram:
        histogram_words.append(word)
    #print(list_of_frequencys)
    for number in list_of_frequencys:
        count += number
        if random_number < count:
            break
        else: 
            index += 1
    #print(histogram_words)
   #print (f' rng:{random_number}  total:{count}  index#:{index}')
    #print (f' random weighted word: {histogram_words[index]} freq is {list_of_frequencys[index]}')
    #print(histogram_words[index])
    return histogram_words[index]

    

def random_word_frequency():
    #makes histogram
    histogram = make_histogram()
    #Reads file to use words
    words = read_word_file(file_name)
    #Copys histogram so we can edit it in a loop without breaking the loop
    new_histogram = histogram.copy()
    #Defining total words
    total_words = len(words)
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
def test_random_word_frequency():
    #Reads file to use words
    words = read_word_file(file_name)
    #Initilizes the random weighed histogram
    weighted_histogram = {}
    
    for index in range(len(words)): #Change len(words) to 1000 for a better test
        index += 1
        #random_word = random_word_frequency()
        random_word = random_word_frequency_genjis_version()
        weighted_histogram[random_word] = weighted_histogram.get(random_word, 0) + 1 
    #print(weighted_histogram)
    #Sorts the weighed histogram
    sortedwords = sorted(weighted_histogram, key=weighted_histogram.get, reverse=True)
    #Turns the histogram into a string
    new = ''
    place = 0
    for word in sortedwords: 
        place += 1
        value = weighted_histogram.get(word)
        new += (str(place) + '. ' + word + '    Occurrences: ' + str(value) + '\n')
    #Writes test file
    file = open('weightedsortedwords.txt', 'w+')
    file.write(new)
    file.close()

if __name__ == "__main__":
    file_name = sys.argv[1:]
    file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/words.txt'
    #file_name = '/Users/beckhaywood/dev/repos/tweet-gen-tutorial/Code/poemtest.txt'
    #make_histogram()
    #random_word_frequency_genjis_version()
    test_random_word_frequency()
    #frequency()


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