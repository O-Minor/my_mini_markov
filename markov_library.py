# mini markov 2 exactly by the tutorial
# tutorial: https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb

text = open("frank_text_clean.txt").read()
words = text.split()
pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
print(pairs[:25])
from collections import Counter
pair_counts = Counter(pairs)
print(pair_counts.most_common(10))
print(pair_counts[("of", "the")]/sum(pair_counts.values()))
char_pairs = [(text[i], text[i+1]) for i in range(len(text)-1)]
char_pair_counts = Counter(char_pairs)
print(char_pair_counts.most_common(10))
seven_grams = [tuple(words[i:i+7]) for i in range(len(words)-6)]
print(seven_grams[:20])
def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]
import random
frank_9grams = ngrams_for_sequence(9, open("frank_text_clean.txt").read())
random.sample(frank_9grams, 10)
print(ngrams_for_sequence(2, "condescendences"))
print(ngrams_for_sequence(4, [5, 10, 15, 20, 25, 30]))
print(Counter(ngrams_for_sequence(3, open("frank_text_clean.txt").read())).most_common(20))
#predictors section
