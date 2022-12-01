import tensorflow as tf
from tensorflow import keras
import numpy as np
import streamlit as st
import os


def detect_tumor(img):
    model = keras.models.load_model('my_model.h5')

    img = tf.keras.utils.load_img(img, target_size=(180, 180))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    dic = {0: "hasn't a brain tumor", 1: "has a brain tumor"}
    result = dic[np.argmax(score)]
    percent_result = 100 * np.max(score)

    return result, percent_result
