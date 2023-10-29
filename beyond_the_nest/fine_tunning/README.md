# Beyond-the-Nest

The following script finetunes falcon model with a dataset.
On a high level, The main goal from security experimentation perspective is to find if overfitted models are less robust to certain kind of attacks. 

We will first finetune the falcon7b-instruct model on sst2 dataset ( chosen over IMDB ) because it has more training files. 
Taking into account transformers example folder, we can run the following script

dataset="sst2"
#subset="en"
python fine_tune_classifier.py \
    --model_name_or_path  tiiuae/falcon-7b-instruct \
    --dataset_name sst2 \
    --dataset_config_name dataset_infos.json \
    --shuffle_train_dataset \
    --metric_name accuracy \
    --text_column_delimiter "\n" \
    --label_column_name label \
    --do_train \
    --do_eval \
    --max_seq_length 512 \
    --per_device_train_batch_size 32 \
    --learning_rate 2e-5 \
    --num_train_epochs 1 \
    --do_regression=False \
    --output_dir /tmp/fine-tunned-falcon-7b-instruct 

