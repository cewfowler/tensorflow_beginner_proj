import tensorflow as tf;
import os;

def load_data(data_directory):
    directories = [dir for dir in os.listdir(data_directory)
                   if os.path.isdir(os.path.join(data_directory, dir))];

    labels = [];
    images = [];

    for dir in directories:
        label_directory = os.path.join(data_directory, dir);

        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")];

        for f in file_names:
            images.append(skimage.data.imread(f));
            labels.append(int(dir));

    return images, labels;

ROOT_PROJ_PATH = os.getcwd();
TRAIN_DATA_DIR = os.path.join(ROOT_PROJ_PATH, "TrafficSigns/Training");
TEST_DATA_DIR = os.path.join(ROOT_PROJ_PATH, "TrafficSigns/Testing");

images, labels = load_data(TRAIN_DATA_DIR);
