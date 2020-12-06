# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:44:33 2020

@author: Szafa
"""

import sys
if len(sys.argv) != 2:
    print("Pass the path to the image in the parameters")
    exit()

import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras

img_height = 128
img_width = 128

model = tf.keras.models.load_model(r'C:\Users\Szafa\Documents\Machine learning\Palce\base_model')

img_path = sys.argv[1];
class_names = ['0', '1', '2', '3', '4', '5']

img = keras.preprocessing.image.load_img(
    img_path, target_size=(img_height, img_width),color_mode='rgb'
)
img = img.convert('LA').convert('RGB')
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
with tf.device('/cpu:0'):
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)