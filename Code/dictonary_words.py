import random
import sys
import os

if __name__ == "__main__":

    num_of_words = int(sys.argv[1])

    f = open('/usr/share/dict/words')
    words = f.read()
    # for word in words:
    #     list_of_words = list(words.split())
    # randomized_sentence = []
    # for index in range(num_of_words):
    #         random_index = random.randint(0, len(list_of_words) -1)
    #         randomized_sentence.append(list_of_words[random_index])
    #         list_of_words.pop(random_index)
    # print(randomized_sentence)
    words1 = words.splitlines()
    words_list = []
    for i in range(num_of_words):
        random_index = random.randint(0, len(words1) - 1)
        words_list.append(words1[random_index])
        words1.pop(random_index)
    string = ''
    for word in words_list:
        string += (str(word) + ' ')
    print(string)
    '''words1 = words.split()
    words_list = []
    for i in range(num_of_words):
        words_list.append(random.choice(words1))
    #print(words_list)
    str1 = ''
    for word in words_list:
        str1 += (str(word) + ' ')
    print(str1)
    '''


    


