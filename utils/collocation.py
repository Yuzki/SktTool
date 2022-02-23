import re
import os
import sys
import itertools
from collections import Counter


class Collocation:
    def __init__(self, filename='', lemma=''):
        self.fname = filename
        self.lemma = lemma
    
    def makeCollocDict(self):
        with open(self.fname, mode='r', encoding='utf-8') as f:
            sentences = []

            for line in f:
                sentences.append(line.rstrip())
            
        word_list = [sentence.split(' ') for sentence in sentences]
        pair_list = [list(itertools.combinations(n, 2)) for n in word_list if len(word_list) > 1]

        all_pairs = []
        for u in pair_list:
            all_pairs.extend(u)
        cnt_pairs = Counter(all_pairs)

        cnt_pairs_word = {}
        for key, value in cnt_pairs.items():
            if self.lemma in key:
                colloc = tuple(sorted(key))
                if colloc in cnt_pairs_word.keys():
                    cnt_pairs_word[colloc] += value
                else:
                    cnt_pairs_word[colloc] = value
            
        return sorted(cnt_pairs_word.items(), key=lambda x:x[1])

# c = Collocation(filename='./text/rv_lemma_verse.txt', lemma='agní')
# d = c.makeCollocDict()
# print(d)

# a = 0
# for i in cnt_pairs_word_sorted:
#     print(len(cnt_pairs_word_sorted) - a, i)
#     a += 1
