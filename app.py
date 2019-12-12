from flask import Flask, render_template
from histogram import read_word_file
from markov_v2 import *
import os 
print(os.path.dirname(os.path.abspath('homer.jpg')))




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
    sentence = markov_second_order.generate_sentence()
    return render_template('index.html', sentence=sentence)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))