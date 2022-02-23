cat train.txt dev.txt test.txt | cut -d " " -f 2 | grep -v "^$" | sort | uniq > labels.txt

output_dir='sanskrit_pos_tag'
batch_size=32
num_epochs=3
save_steps=750
seed=1

BERT_MODEL='bert-base-multilingual-cased'
MAX_LENGTH=128