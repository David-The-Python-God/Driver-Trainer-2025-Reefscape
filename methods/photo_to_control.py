import pygame, random
import os, sys, ctypes
import time, PIL
from PIL import Image, ExifTags
from inputs import get_gamepad


if __name__ == "__main__":
    from config import trigger_actions, moving_action_codes, joystick_dead_band_used, trigger_dead_band_used
else:
    from methods.config import trigger_actions, moving_action_codes, joystick_dead_band_used, trigger_dead_band_used

def show_photo(action):

    if action == "reset":
        action_done = None
        action = None
        image_path = None
        time_before = None
        exit
    
    else:
        # to parse categoories of the action being done and the scenario prior to action being done
        directory_list = ["photos/action_being_done/", "photos/scenario_before_action_has_been_done/"]
        r = random.randint(0, 1)  # randomizes which category the image comes from
        
        photo = action + ".jpg"
        print("directory " , directory_list[1-r]+photo)

        print("directory " , directory_list[r]+photo)
        if os.path.exists(directory_list[r]+photo):
            image_path = directory_list[r]+photo

        elif os.path.exists(directory_list[1-r]+photo):  # [1-r] is so smart, I know.
            image_path = directory_list[1-r]+photo

        else:
            print("No image found")
            return
        
        

        # Load and rotate image using PIL
        img = Image.open(image_path)

        # Auto-rotate based on EXIF orientation
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation': # for orienting images taken from phone
                    break

            exif = img._getexif()
            if exif is not None:
                orientation_value = exif.get(orientation, None)
                if orientation_value == 3:
                    img = img.rotate(180, expand=True)
                elif orientation_value == 6:
                    img = img.rotate(270, expand=True)
                elif orientation_value == 8:
                    img = img.rotate(90, expand=True)
        except Exception as e:
            print(f"EXIF rotation failed: {e}")

        # Convert to a format pygame can use
        img = img.resize((800, 600))  # Resize as needed
        image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)

        # Initialize and display using pygame
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{0},{200}"
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Photo:")
        screen.blit(image, (0, 0))
        pygame.display.flip()

        ctypes.windll.user32.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001 | 0x0002) # supposed to send image to front


        # if sys.platform == "win32":
        #     hwnd = pygame.display.get_wm_info()['window']
        #     ctypes.windll.user32.SetForegroundWindow(hwnd)

        print("\033[1;34mIMAGE_IS_BEING_SHOWN\033[0m")

        action_done = None
        time_before = time.time()
        while action_done == None:  # wait for the user to press the button
                events = []
                events = get_gamepad()  # listner function, but not in background?

                for event in events:    # goes through ALL events recorded

                    if (event.ev_type == "Absolute" or event.ev_type == "Key") and event.state !=0:
                        
                        event_code = event.code.lower()
                        if not (event_code in moving_action_codes and event.state < joystick_dead_band_used):  # filter out minor joystick movements
                        
                            if (event_code in trigger_actions and event.state >= trigger_dead_band_used) or (event_code not in trigger_actions): # so triggers must be fully pressed

                                print(f"Event detected: {event.ev_type} - {event_code} - {event.state}")
                                pygame.quit()
                                return([event.code, time_before])
                    
                time.sleep(0.01) # prevent high CPU usage


if __name__ == "__main__":
    print(show_photo("station_intake"))
