import tensorflow as tf;
import numpy as np;
import os;
import skimage;
import data_exploration;

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
images = np.array(images);
labels = np.array(labels);

#data_exploration.display_histogram(labels);
traffic_signs = [300, 2250, 3650, 4000];
data_exploration.display_images(images, traffic_signs);
