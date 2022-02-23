from transformers import AutoTokenizer
from pathlib import Path
import re

pos_file = Path('../text/RV_VedaWeb_XML/RV_forPOS.txt')
# pos_file = Path('../text/rv_pos.txt')
assert(pos_file.exists())

pct_train = 0.8
pct_dev = 0.1
pct_test = 0.1

with open(pos_file) as f:
  lines = f.readlines()
  line_count = len(lines)
  train_lines_count = int(pct_train * line_count)
  dev_lines_count = int(pct_dev * line_count)
  test_lines_count = line_count - (train_lines_count + dev_lines_count)
  assert(train_lines_count + dev_lines_count + test_lines_count == line_count)

train_lines = lines[:train_lines_count]
dev_lines = lines[train_lines_count:train_lines_count + dev_lines_count]
test_lines = lines[:test_lines_count]
assert(len(train_lines) == train_lines_count)
assert(len(dev_lines) == dev_lines_count)
assert(len(test_lines) == test_lines_count)


def create_pos_file(lines, target_file):
  with open(target_file, mode='w') as target:
    for line in lines:
      for word in line.split(' '):
        pair = re.split('_(?=[^_]+$)', word)
        # print(pair)
        target.write(f'{pair[0]} {pair[1]}\n')
      target.write('\n')


create_pos_file(train_lines, './data/train.txt.tmp')
create_pos_file(dev_lines, './data/dev.txt.tmp')
create_pos_file(test_lines, './data/test.txt.tmp')


max_length = 128
bert_model = 'bert-base-multilingual-cased'


def remove_confusing_tokens(ds_file, target_file):
  tokenizer = AutoTokenizer.from_pretrained(bert_model)
  subword_len_counter = 0
  with open(ds_file, 'rt') as f_p, open(target_file, 'w') as t:
    for line in f_p:
      line = line.rstrip()

      if not line:
        t.write(f'{line}\n')
        subword_len_counter = 0
        continue

      token = line.split()[0]
      current_subwords_len = len(tokenizer.tokenize(token))

      if current_subwords_len == 0:
        continue
      if (subword_len_counter + current_subwords_len) > max_length:
        t.write('\n')
        t.write(f'{line}\n')
        subword_len_counter = current_subwords_len
        continue

      subword_len_counter += current_subwords_len

      t.write(f'{line}\n')


remove_confusing_tokens('./data/train.txt.tmp', './data/train.txt')
remove_confusing_tokens('./data/dev.txt.tmp', './data/dev.txt')
remove_confusing_tokens('./data/test.txt.tmp', './data/test.txt')



