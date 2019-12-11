from dictogram import Dictogram
from random import *
from histogram import read_word_file

class HigherOrderMarkov(dict):
    """The higher order markov chain is stored in a dictionary.
    With a word pair tuple as a key then the value is the possible outcomes.
    {('I', 'went'): ['left,', 'left,', 'right,']}
    """
    def __init__(self, word_list=None): #order = 2
        #self.order = order #Not used
        self.word_list = word_list #defines word list
        self.generate_markov(word_list) #creates markov
     
    def generate_markov(self, word_list):
        #n being the created enumerated value. key1 being the word in the list.
        for n, key1 in enumerate(word_list):
            if len(word_list) > (n + 2): #order 
                key2 = word_list[n + 1]
                #print(key2)
                word = word_list[n + 2]
                #print(word)
                #print('______')
                #if key is not in the dictogram create one with the new tuple
                if (key1, key2) not in self:
                    self[(key1, key2)] = [word]
                else:
                #if it is then add the word to the possible options
                    self[(key1, key2)].append(word)

    def generate_sentence(self, length=10): #+2
        rng = randint(0, len(self.word_list) - 1)
        #print(rng)
        #key is a tuple and after random work is choosen the next word is just +1 index. The -1 is nessesary so it doesnt check for a item out of range
        couple = (self.word_list[rng - 1], self.word_list[rng])
        #define sentence put first two words in
        sentence = couple[0] + ' ' + couple[1]
        #Loop through the length of the sentence
        for _ in range(length):
            #word is set equal to random choice of the possibilitys of words after the word couple
            word = choice(self[couple])
            #print(self[key])
            #adds word to sentence
            sentence += ' ' + word
            #key is set equal to a new couple
            #print(couple)
            couple = (couple[1], word)
        sentence += '.'
        return sentence.capitalize()

if __name__ == "__main__":
    #Second order test
    words = read_word_file('markovtest.txt')
    secondordermarkov = HigherOrderMarkov(word_list = words)
    #print(secondordermarkov)
    print(secondordermarkov.generate_sentence())