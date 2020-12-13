# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:44:33 2020

@author: Szafa
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
    
def predict(image_path):
    
    image_path = 'staticfiles/' + image_path

    img_height = 128
    img_width = 128
    
    model = tf.keras.models.load_model(r'C:\Users\Szafa\Documents\Machine learning\Palce\base_model')
    
    class_names = ['0', '1', '2', '3', '4', '5']
    
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_height, img_width),color_mode='rgb'
    )
    img = img.convert('LA').convert('RGB')
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    with tf.device('/cpu:0'):
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
    
    return [class_names[np.argmax(score)], 100 * np.max(score)];
    