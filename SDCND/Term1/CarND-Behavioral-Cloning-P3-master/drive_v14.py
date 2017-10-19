# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:00:25 2017

@author: navneet123
"""

import argparse
import base64
import json
import cv2

import numpy as np
import socketio
import eventlet
import eventlet.wsgi
import time
from PIL import Image
from PIL import ImageOps
from flask import Flask, render_template
from io import BytesIO

from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array
from keras.optimizers import Adam

# Fix error with Keras and TensorFlow
import tensorflow as tf
tf.python.control_flow_ops = tf

'''
def roi(img): # For model 5
    img = img[64:295 ,:]
    image = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    return cv2.resize(image, (200, 66),interpolation=cv2.INTER_AREA)
'''
#ch, img_rows, img_cols = 3, 64,64 
ch, img_rows, img_cols = 3, 16, 32

def roi(img): # For model 5
    #img = img[60:210 ,:]
    img = img[60:140, :]
    #image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    return cv2.resize(image, (img_cols, img_rows),interpolation=cv2.INTER_AREA)

    
def preprocess_input(img):
    return roi(img)


sio = socketio.Server()
app = Flask(__name__)
model = None
prev_image_array = None


@sio.on('telemetry')
def telemetry(sid, data):
    # The current steering angle of the car
    steering_angle = data["steering_angle"]
    # The current throttle of the car
    throttle = data["throttle"]
    # The current speed of the car
    speed = data["speed"]
    # The current image from the center camera of the car
    imgString = data["image"]
    image = Image.open(BytesIO(base64.b64decode(imgString)))
    x = np.asarray(image)
    image_array = preprocess_input(x)           
    transformed_image_array = image_array[None, :, :, :]
    # This model currently assumes that the features of the model are just the images. Feel free to change this.
    steering_angle = 1.0*float(model.predict(transformed_image_array, batch_size=1))
    # The driving model currently just outputs a constant throttle. Feel free to edit this.
    throttle = 0.1
    print(steering_angle, throttle)
    send_control(str(steering_angle), throttle)


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)
    send_control(0, 0)


def send_control(steering_angle, throttle):
    sio.emit("steer", data={
    'steering_angle': steering_angle.__str__(),
    'throttle': throttle.__str__()
    }, skip_sid=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Driving')
    parser.add_argument('model', type=str,
    help='Path to model definition json. Model weights should be on the same path.')
    args = parser.parse_args()
    with open(args.model, 'r') as jfile:
        model = model_from_json(jfile.read())

    opt = Adam(lr=0.0001)    
    model.compile(loss="mse", optimizer=opt)        
    #model.compile("adam", "mse")
    weights_file = args.model.replace('json', 'h5')
    model.load_weights(weights_file)

    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)