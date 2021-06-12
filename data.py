import tensorflow as tf;
import numpy as np;
import matplotlib.pyplot as plt;
import os;
import skimage

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

# Print dimensions and number of elements in 'images' + first instance
#print(images.ndim);
#print(images.size);
#print(images[0]);

# Print dimensions and number of elements in 'labels' + number of labels
#print(labels.ndim);
#print(labels.size);
#print(len(set(labels)));

# Let's make and show a histogram
#plt.hist(labels, 62);
#plt.show();

traffic_signs = [300, 2250, 3650, 4000];

# Fill subplots with random images we've selected
for i in range(len(traffic_signs)):
    plt.subplot(1, 4, i+1);
    plt.axis('off');
    plt.imshow(images[traffic_signs[i]]);
    plt.subplots_adjust(wspace=0.5);

    print("Image {0} - shape: {1}, min: {2}, max: {3}".format(i+1,
                                                  images[traffic_signs[i]].shape,
                                                  images[traffic_signs[i]].min(),
                                                  images[traffic_signs[i]].max()));

plt.show();
