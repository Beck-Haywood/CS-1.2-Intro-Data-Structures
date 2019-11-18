from flask import Flask
from histogram import *
from sample import random_sentence
from sentence_generator import markov, random_word
from markov_walk import random_walk_sentence
#test


app = Flask(__name__)

#@app.route('/')
#def sentence():
#    word_list = read_word_file('words.txt')
#    histogram = make_histogram(word_list)
#    return random_sentence(histogram, 10)

@app.route('/')
def sentence():
    # word_list = read_word_file('poemtest.txt')
    # histogram = make_histogram(word_list)
    # starting_word = random_word_frequency(histogram)
    # markovv = markov(word_list)
    # sentence_list = []
    # word = random_word(markovv, starting_word)
    # sentence_list.append(word)
    # for _ in range(7):
    #     word = random_word(markovv, word)
    #     sentence_list.append(word)
    # sentence = ''
    # for word in sentence_list:
    #     sentence += f'{word} ' #Innefficent could add it to list then join it together
    # return sentence
        
    # return random_sentence(histogram, 10)
    
    return random_walk_sentence()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))