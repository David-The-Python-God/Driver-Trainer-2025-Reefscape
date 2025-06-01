# ones that aren't keyd to my controler yet:   'left_l2', 'right_l2', 'left_l1', 'right_l1', processor, pyramid L1, barge score(both raise and let go), manual vs auto l1, pick up from station, manual eject

actions_list = ['left_l4', 'right_l4', 'left_l3', 'right_l3', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', 'climb', 'switch_auto_scoring_method']
images_list = [] # probably not needed, each image is just named the action
codes_for_actions_dict = {"left_l4" : "btn_tl", "right_l4" : "btn_tr", "left_l3" : "abs_z", "right_l3" : "abs_rz", "pick_up_coral_from_ground" : "abs_rz", "pick_up_algea_from_reef" : "abs_z", "climb" : "abs_hat0y", "switch_auto_scoring_method" : "btn_thumbl"}


# l1/2 would be in key if I had them
key_actions = [ #button
    'left_l4', 'right_l4', 'switch_auto_scoring_method', codes_for_actions_dict.get('left_l4'), codes_for_actions_dict.get('right_l4'), codes_for_actions_dict.get('switch_auto_scoring_method')
]

# climb is in absolute for some reason
absolute_actions = [ #trigger/joystick
    'climb', 'left_l3', 'right_l3', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3"), codes_for_actions_dict.get("climb")]

non_holding_actions = [ # actions on robot that are instant
    'switch_auto_scoring_method', codes_for_actions_dict.get("switch_auto_scoring_method")
]

trigger_actions = [
    'left_l3', 'right_l3', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3")
]

moving_action_codes = [ # joystick codes (used to mitigate minor joystick movements)
    "abs_x", "abs_y", "abs_rx", "abs_ry"
]

# I apologize for making you see the above.

import pyfiglet
from colorama import Fore, Style, init


def show_false():
        # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("FALSE")

    # Print in red
    print(Fore.RED + ascii_text + Style.RESET_ALL)

def show_correct():
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("CORRECT")

    # Print in green
    print(Fore.GREEN + ascii_text + Style.RESET_ALL)

def show_custom(text, color = Fore.WHITE):
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format(text)

    # Print in green
    print(color + ascii_text + Style.RESET_ALL)


if __name__ ==  "__main__" :
    show_false()
    show_correct()
    show_custom("IF YOUR SEEING THIS, it is too late, I am already dead and you are reading my code thinking \"this bitch\"")
