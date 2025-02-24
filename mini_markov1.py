# I am following this tutorial on markov chains
# https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb

# retroactive importing
import string
from collections import Counter
import random

# unit of the n-gram is called leve (character word etc)
# length is called order
# level: character order: 2 example word: doggy
# do, og, gg, gy

# source for text: https://www.gutenberg.org/cache/epub/84/pg84.txt

# open an ethically sourced free range organic cruelty free .txt file
in_text = open("frank_text_clean.txt").read()
# split text into words on spaces
words = in_text.split()
# make n-gram pairs of words
pairs = [ (words[i], words[i+1])
           for i in range(len(words)-1)]
print(pairs[:10])

#gives how many times each pair showed up
pair_counts = Counter(pairs)
print("most common pairs:\n", pair_counts.most_common(50),"\n")
#note: find a way to do least common
print("percent of the book that is 'of', 'the':\n",pair_counts[('of', 'the')] / sum(pair_counts.values()) )

char_pairs = [(in_text[i], in_text[i+1]) 
              for i in range(len(in_text)-1)]
print(char_pairs[:10])

n = 7
# convert the list slice (words[i:i+n]) into a tuple.

ngram_obj = [tuple(words[i:i+n]) for i in range(len(words)-(n-1))]
print(ngram_obj[:20],"\n")

def ngrams(n):
    return [tuple(words[i:i+n]) for i in range(len(words)-(n-1))]



def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]

n_gram_x = ngrams(5)
n_gram_seq = ngrams_for_sequence(3, open("frank_text_clean.txt").read())
print(random.sample(n_gram_x, 10),"\n")
print(random.sample(n_gram_seq, 10),"\n")

# 2/4 11:57pm - got far enough to sample random n grams from texts by word or by character
# tomorrow going to make the prediction modeler in the tutorial

src = "condesecendences"
src += "$" #end of string idicator
model = {}
for i in range(len(src)-2):
    #get a tuple of just current position and next two
    ngram = tuple(src[i:i+2])
    # next item is current index plus two (i.e., right after the slice)
    next_item = src[i+2] 
    # check if we've already seen this ngram; if not...
    if ngram not in model: 
        # value for this key is an empty list
        model[ngram] = [] 
    # append this next item to the list for this ngram
    model[ngram].append(next_item) 
# prints (ngram: [list of possible characters that come one after])
print(model)

def add_to_model(model, n, seq):
    #make a copy of the sequence and append None to the end
    seq = list(seq[:])   + [None]
    for i in range(len(seq)-n):
        # tuple because we're using it as a dict key!
        gram = tuple(seq[i:i+n])
        next_item = seq[i+n]
        if gram not in model:
            model[gram] = []
        model[gram].append(next_item)

def markov_model(n, seq):
    model = {}
    add_to_model(model, n, seq)
    return model

markov_model(2, "condescendences")
frankenstein_markov_model = markov_model(2, open("frank_text_clean.txt").read().split())
# print(frankenstein_markov_model,"\n")

# print("predict from frank:\n",frankenstein_markov_model[('that', 'he')])

n=5
blorbo_model = markov_model(n, open("simple_sabotage_clean.txt").read())
# print(blorbo_model)
output = "the st"
for i in range(300):
    ngram = tuple(output[-n:])
    next_item = random.choice(blorbo_model[ngram])
    output += next_item
# print("from sab:",output, "\n")ƒor

def markov_predictor(in_file, n, out_len, start = None):
    in_model = markov_model(n, open(in_file).read())

    # print(in_model)
    if start is None:
        start = random.choice(list(model.keys()))
    '''
    if start not in model.keys():
        print("trying to avoid key error")
        start = random.choice(list(in_model.keys()))
    '''
    output = start
    # print(output, type(output))
    for i in range(out_len):
        ngram = tuple(output[-n:])
        next_item = random.choice(in_model[ngram])
        output += next_item
    print(output)

print("pred from func:\n")
markov_predictor("frank_text_clean.txt", 3, 300, "I w")

# GRAVEYARD
'''
print("hello world")
tester = "hello world".split()
print(tester)
print(in_text) <- don't print all of frankenstein to console if you can help it thx
'''