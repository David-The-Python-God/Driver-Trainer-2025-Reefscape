import random, time, math
import keyboard
from inputs import get_gamepad
from config import left_reef_levels_to_score_dict,right_reef_levels_to_score_dict,left_letters_list,reef_letters_list, reef_levels_list


def generate_location_to_keybind():
    reef_letter = random.choice(reef_letters_list)
    reef_level = random.choice(reef_levels_list)

    if reef_letter in left_letters_list:
        correct_keybind = left_reef_levels_to_score_dict.get(reef_level)
    else:
        correct_keybind = right_reef_levels_to_score_dict.get(reef_level)

    return [reef_letter+" "+reef_level, correct_keybind]

def location_to_keybind():
    pass

if __name__ == "__main___":
    print(generate_location_to_keybind())