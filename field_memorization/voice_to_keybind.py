
import pyttsx3

import pygame
import os, sys, ctypes
import time
from inputs import get_gamepad
import random



def voice_to_control(action):
    # print("\033[1;34mVOICE IS SOUNDING\033[0m") # commented out so you don't have warning
    action = action.replace("_", " ")

    engine = pyttsx3.init()
    engine.setProperty('rate', random.randint(120, 230))     # randomness so you don't get used to a tempo???
    engine.setProperty('volume', random.uniform(0.8, 1.2))   

    engine.say(action)
    engine.runAndWait()
    print("\033[1;34mVOICE HAS SOUNDED\033[0m")

if __name__ == "__main__":
    voice_to_control("test action")