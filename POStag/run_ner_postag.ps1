$OUTPUT_DIR='sanskrit_pos_tag'
$BATCH_SIZE=32
$NUM_EPOCHS=3
$SAVE_STEPS=100
$SEED=1
$BERT_MODEL='bert-base-multilingual-cased'
$MAX_LENGTH=128
python .\run_ner.py --data_dir ./data --labels ./labels.txt --model_name_or_path $BERT_MODEL --output_dir $OUTPUT_DIR --max_seq $MAX_LENGTH --num_train_epochs $NUM_EPOCHS --per_device_train_batch_size $BATCH_SIZE --save_steps $SAVE_STEPS --seed $SEED --do_train --do_eval --do_predict --overwrite_output_dir --resume_from_checkpoint $OUTPUT_DIR
# python ./run_ner.py --data_dir ./data --labels ./labels.txt --model_name_or_path $BERT_MODEL --output_dir $OUTPUT_DIR --max_seq $MAX_LENGTH --num_train_epochs $NUM_EPOCHS --per_device_train_batch_size $BATCH_SIZE --save_steps $SAVE_STEPS --seed $SEED --do_train --do_eval --do_predict --overwrite_output_dir --resume_from_checkpoint $OUTPUT_DIR