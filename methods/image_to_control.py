import pygame
import os, sys, ctypes
import time
from inputs import get_gamepad

if __name__ == "__main__":
    from config import trigger_actions, moving_action_codes, codes_for_actions_dict, actions_list, non_holding_actions
else:
    from methods.config import trigger_actions, moving_action_codes, codes_for_actions_dict, actions_list, non_holding_actions

def show_image(action):

    if action == "reset":
        action_done = None
        action = None
        image_path = None
        time_before = None
        exit
    
    else:
        # print("\033[1;34mIMAGE_IS_BEING_SHOWN\033[0m") #commented out so no warnign

        image_path = f"images/{action}.png"
        """Display an image using pygame until close_signal is True"""
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Image Viewer")

        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            return

        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (800, 600))
        screen.blit(image, (0, 0))
        pygame.display.flip()

        if sys.platform == "win32":
            hwnd = pygame.display.get_wm_info()['window']
            ctypes.windll.user32.SetForegroundWindow(hwnd)

        time_before = time.time()
        print("\033[1;34mIMAGE_IS_BEING_SHOWN\033[0m")

        # Wait for close signal
        action_done = None
        while action_done == None:  # wait for the user to press the button
                events = []
                events = get_gamepad()  # listner function, but not in background?

                for event in events:    # goes through ALL events recorded

                    if (event.ev_type == "Absolute" or event.ev_type == "Key") and event.state !=0:
                        
                        event_code = event.code.lower()
                        if not (event_code in moving_action_codes and event.state < 1000):  # filter out minor joystick movements
                        
                            if (event_code in trigger_actions and event.state >= 240) or (event_code not in trigger_actions): # so triggers must be fully pressed

                                print(f"Event detected: {event.ev_type} - {event_code} - {event.state}")
                                pygame.quit()
                                print(["image_return:", event.code, time_before])
                                return([event.code, time_before])
                    
                time.sleep(0.01) # prevent high CPU usage


if __name__ == "__main__":
    print(show_image("levy"))
