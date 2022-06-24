import os, shutil


# The path to the directory where the original
# dataset was uncompressed
original_dataset_dir = 'G:\img_datasets\dogs-vs-cats\train\train'

# The directory where we will
# store our smaller dataset
base_dir = 'G:\img_datasets\dogs-vs-cats\base_dir'

os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')



