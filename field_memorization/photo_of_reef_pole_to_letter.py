from config import reef_letters_list, show_false, show_correct
import random, time, math, os, sys
import pygame, ctypes
from PIL import Image, ExifTags

def display_photo_false():
    img = Image.open("field_memorization/photos/false.png")
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


    if sys.platform == "win32":
        hwnd = pygame.display.get_wm_info()['window']
        ctypes.windll.user32.SetForegroundWindow(hwnd)

    time.sleep(3)

    return


def display_photo(reef_letter):
    directory_list = ["field_memorization/photos/birds_eye_view/", "field_memorization/photos/driver_pov/"]
    r = random.randint(0, 1)  # randomizes which category the image comes from
    
    photo = reef_letter + ".png"

    if os.path.exists(directory_list[r]+photo):
        image_path = directory_list[r]+photo

    elif os.path.exists(directory_list[1-r]+photo):  # [1-r] is so smart, I know.
        image_path = directory_list[1-r]+photo

    else:
        print(f"No image found for{reef_letter}" + "\n----------------------------------------------\n")
        return
    
    

    # Load and rotate image using PIL
    img = Image.open(image_path)

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


    if sys.platform == "win32":
        hwnd = pygame.display.get_wm_info()['window']
        ctypes.windll.user32.SetForegroundWindow(hwnd)

    print("\033[1;34mIMAGE_IS_BEING_SHOWN\033[0m")

    time_before = time.time()

    reef_letter_inputed = input(' ')

    time_spent = time.time() - time_before

    return(reef_letter_inputed, time_spent)


    
if __name__ == "__main__":
    print(display_photo("D"))