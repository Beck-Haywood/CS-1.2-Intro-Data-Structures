import random
from histogram import make_histogram, read_word_file
import sys
from timeit import default_timer as timer

def sample_word(histogram):
    """Returns a word based on weighted probability
    """
    total_words = sum(histogram.values())
    rng = random.randint(1, total_words)
    count = 0
    for key in histogram.keys():
        count += histogram[key]
        if rng <= count:
            return key

if __name__ == "__main__":
    word_list = read_word_file(sys.argv[1])
    histogram = make_histogram(word_list)
    start = timer()
    print(sample_word(histogram))
    end = timer()
    print(end - start)


