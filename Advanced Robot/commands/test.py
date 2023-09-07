print('Started....', end='\r')
import json
import time
import sys
import pyttsx3
import urllib
import numpy as np
import speech_recognition as sr
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama
colorama.init()
from colorama import Fore, Style, Back

import random 
import pickle

print('Libraries imported....', end='\r')
time.sleep(1)

with open("commands.json") as file:
    data = json.load(file)

def chat(command):
    model = keras.models.load_model('commands_model')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    max_len = 20
    inp = command
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    # print("Result: ", result)
    # print("Tag: ", tag)# [[0.06488758 0.10415693 0.08502355 0.27676386 0.05718468 0.07421175 0.07847793 0.09536088 0.16393292]]
    for i in data['intents']:
        if i['tag'] == tag:
            prase = np.random.choice(i['responses'])
            return prase
while True:
    a = input(">>: ")
    if a == "quit" or a == "exit":
        break
    else:
        print(chat(a))