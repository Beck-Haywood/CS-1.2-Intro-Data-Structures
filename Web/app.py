from flask import Flask
from histogram import *
from sample import random_sentence
#test


app = Flask(__name__)

@app.route('/')
def sentence():
    word_list = read_word_file('words.txt')
    histogram = make_histogram(word_list)
    return random_sentence(histogram, 10)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))