import numpy as np
import time

def shuffle(input):
    ret = []
    while len(input):
        i = int(time.time()) % len(input)
        ret.append(input[i])
        del input[i]
    return ret

def generator(text, sep=" ", option=None):
    if isinstance(text, str):
        words = text.split(sep)
        if option == "snuffle":
            words = shuffle(words)
        elif option == "unique":
            np.unique(words)
        elif option == "ordered":
            list.sort(words)
        for w in words:
            yield w
    else:
        print("Text argument need to be a String")


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="snuffle"):
    print(word)
