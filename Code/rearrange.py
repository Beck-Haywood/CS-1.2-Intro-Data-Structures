import random
import sys

if __name__ == "__main__":
    listt = sys.argv[1:]
    #print(type(sentence))
    # listt = list(sentence.split())
    #print(type(listt))
    #print(sentence)
    #print(len(listt))
    randomized_sentence = []
    for index in range(len(listt)):
        random_index = random.randint(0, len(listt) -1)
        randomized_sentence.append(listt[random_index])
        listt.pop(random_index)
        # del listt[random_index]

    print(randomized_sentence)

