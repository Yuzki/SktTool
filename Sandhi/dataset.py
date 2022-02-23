import collections
import logging
import os
import pathlib
import re
import string
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

import tensorflow_datasets as tfds
import tensorflow_text as text
import tensorflow as tf


logging.getLogger('tensorflow').setLevel(logging.ERROR)  # suppress warnings


def split_text():
    n = 0
    if n == 0:
        fsname = './text/samhita.txt'
        fpname = './text/padapatha.txt'
    elif n > 0 and n < 6:
        fsname = f'./text/samhita_{n}-gram.txt'
        fpname = f'./text/padapatha_{n}-gram.txt'
    else:
        print('Error: n = 0, 1, 2, 3, 4, 5')
    
    with open(fsname, mode='r', encoding='utf-8') as fs, open(fpname, mode='r', encoding='utf-8') as fp:
        samhita_lines = [elem.rstrip() for elem in fs.readlines()]
        padapatha_lines = [elem.rstrip() for elem in fp.readlines()]
    
    num_all = len(samhita_lines)
    num_train = int(num_all * 0.8)
    num_test = num_all - num_train

    id_all = np.random.choice(num_all, num_all, replace=False)
    id_train = id_all[0:num_train]
    id_test = id_all[num_train:num_all]

    train_data = [samhita_lines[id_train] + 

    