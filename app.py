from flask import Flask
from histogram import read_word_file
from markov_v2 import *



app = Flask(__name__)

#@app.route('/')
#def sentence():
#    word_list = read_word_file('words.txt')
#    histogram = make_histogram(word_list)
#    return random_sentence(histogram, 10)

@app.route('/')
def tweet():
    words = read_word_file('homer_lines.txt')
    markov_second_order = HigherOrderMarkov(words)
    return markov_second_order.generate_sentence()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))