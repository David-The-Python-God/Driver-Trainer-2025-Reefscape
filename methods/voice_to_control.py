import pyttsx3

import pygame
import os, sys, ctypes
import time
from inputs import get_gamepad
import random

if __name__ == "__main__":
    from config import trigger_actions, moving_action_codes, codes_for_actions_dict, actions_list, non_holding_actions
else:
    from methods.config import trigger_actions, moving_action_codes, codes_for_actions_dict, actions_list, non_holding_actions

def voice_to_control(action):
    # print("\033[1;34mVOICE IS SOUNDING\033[0m") # commented out so you don't have warning
    action = action.replace("_", " ")

    engine = pyttsx3.init()
    engine.setProperty('rate', random.randint(120, 230))     # randomness so you don't get used to a tempo???
    engine.setProperty('volume', random.uniform(0.8, 1.2))   

    engine.say(action)
    engine.runAndWait()
    print("\033[1;34mVOICE HAS SOUNDED\033[0m")

    
    # if action == "reset":
    #     action_done = None
    #     action = None
    #     image_path = None
    #     time_before = None
    #     exit
    
    # else:
    #     print("\033[1;34mVOICE_IS_BEING_SOUNDED\033[0m")

        

    #     time_before = time.time()

    #     # Wait for close signal
    #     action_done = None
    #     while action_done == None:  # wait for the user to press the button
    #             events = []
    #             events = get_gamepad()  # listner function, but not in background?

    #             for event in events:    # goes through ALL events recorded

    #                 if (event.ev_type == "Absolute" or event.ev_type == "Key") and event.state !=0:
                        
    #                     event_code = event.code.lower()
    #                     if not (event_code in moving_action_codes and event.state < 1000):  # filter out minor joystick movements
                        
    #                         if (event_code in trigger_actions and event.state >= 240) or (event_code not in trigger_actions): # so triggers must be fully pressed

    #                             print(f"Event detected: {event.ev_type} - {event_code} - {event.state}")
    #                             pygame.quit()
    #                             print(["image_return:", event.code, time_before])
    #                             return([event.code, time_before])
                    
    #             time.sleep(0.01) # prevent high CPU usage

if __name__ == "__main__":
    print(voice_to_control("beans_ beans"))

    