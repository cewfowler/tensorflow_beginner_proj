# TF 2.0 supports eager execution which means a session doesnt' have to be
#   explicitly created
import tensorflow as tf;

v1 = tf.constant([1, 2, 3, 4]);
v2 = tf.constant([5, 6, 7, 8]);

result = tf.multiply(v1, v2);



print(result);
