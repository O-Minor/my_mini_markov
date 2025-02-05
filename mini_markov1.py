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
in_text = open("frank_text.txt").read()
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
n_gram_seq = ngrams_for_sequence(3, open("frank_text.txt").read())
print(random.sample(n_gram_x, 10),"\n")
print(random.sample(n_gram_seq, 10),"\n")

# 2/4 11:57pm - got far enough to sample random n grams from texts by word or by character
# tomorrow going to make the prediction modeler in the tutorial

# GRAVEYARD
'''
print("hello world")
tester = "hello world".split()
print(tester)
print(in_text) <- don't print all of frankenstein to console if you can help it thx
'''