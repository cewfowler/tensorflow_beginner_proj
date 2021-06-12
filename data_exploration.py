import matplotlib.pyplot as plt;

# Displays
def display_images(images, signs):
    # Fill subplots with random images we've selected
    for i in range(len(signs)):
        plt.subplot(1, 4, i+1);
        plt.axis('off');
        plt.imshow(images[signs[i]]);
        plt.subplots_adjust(wspace=0.5);

        print("Image {0} - shape: {1}, min: {2}, max: {3}".format(i+1,
                                                      images[signs[i]].shape,
                                                      images[signs[i]].min(),
                                                      images[signs[i]].max()));

    plt.show();


def display_histogram(labels):
    plt.hist(labels, 62);
    plt.show();
