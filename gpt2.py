%tensorflow_version 1.x
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
from google.colab import files

#download model GPT-2 355M
gpt2.download_gpt2(model_name="355M")

#copy file from google drive
gpt2.mount_gdrive()

file_name = "tweet.csv"

gpt2.copy_file_from_gdrive(file_name)

#finetune model
sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              model_name='355M',
              steps=100,
              learning_rate=1e-4,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=500,
              save_every=500
              )

#copy checkpoint to google drive
gpt2.copy_checkpoint_to_gdrive(run_name='run1')

#load checkpoint from google drive
gpt2.copy_checkpoint_from_gdrive(run_name='run1')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

#generate .txt file (1000 lines)
gen_file = 'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow())

gpt2.generate_to_file(sess,
                      destination_path=gen_file,
                      length=200,
                      temperature=1.0,
                      top_p=0.9,
                      prefix='<|startoftext|>',
                      truncate='<|endoftext|>',
                      include_prefix=False,
                      nsamples=1000,
                      batch_size=20
                      )

#download .txt file
files.download(gen_file)
