""" ones that aren't keyd to my controler yet:   
        'left_l1', 'right_l1', ( a lot to differentiate in here for level 1)
        processor,
            pyramid L1, 
            barge score(both raise and let go), 
            manual vs auto l1 (and relation to hamburger/hotdog)
            pick up from station, 
            manual eject (coral and algea)
            hot_dog l1,                             
           
    what key picks up in horizontal L1 if right trigger holds the coral in hotdog?
    How do you ground pick up algea if right trigger is coral pickup and left trigger is reef algea pickup?
    
    Is hotdog/straight l1 just the normal coral pickup and presing lower back paddle? (does it auto align or is it completely manual?)
    is there a manual horizontal L1 if lower backpaddle is horizontal auto-align L1?
    I know left stick press changes the auto align method, but does right stick presss do something?
    Is angle-based the default auto align method coming out of auto?
    Is there a pick up from station keybind in teleop?
    What is the combo for scoring a coral on the level and (without going down) picking up the algea of the reef there? (Is it level score and then jam left trigger?)
    Do the 2 buttons in the middle of the controller do anything?
"""

logitech_trigger_deadband = 255 # this is completely maxed out
logitech_joystick_deadband = 1000 # just below 10% of full trigger

xbox_trigger_deadband = 180  # this is because the trigger is set to not go all the way down (full down is 255 like logitech) (also triggers on my xbox elite have different 1/2 down maximums)
xbox_joystick_deadband = 3500   #around 11% deadband: xbox range is about 3x logitech 32k and very sensitive

joystick_dead_band_used = xbox_joystick_deadband
trigger_dead_band_used = xbox_trigger_deadband

actions_list = ['left_l4', 'right_l4', 'left_l3', 'right_l3', 'left_l2', 'right_l2', 'left_l1', 'right_l1', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', 'climb', 'switch_auto_scoring_method']
images_list = [] # probably not needed, each image is just named the action
codes_for_actions_dict = {
    "left_l4" : "btn_tl", 
    "right_l4" : "btn_tr", 
    "left_l3" : "abs_z", 
    "right_l3" : "abs_rz", 
    'left_l2' : "btn_south",
    'right_l2' : 'btn_east',
    'left_l1' : 'btn_west',
    'right_l1' : 'btn_north',
    "pick_up_coral_from_ground" : "abs_rz", 
    "pick_up_algea_from_reef" : "abs_z", 
    "climb" : "abs_hat0y", 
    "switch_auto_scoring_method" : "btn_thumbl"
}

level_holding_time = [1, 1.7]
hold_time_for_actions_dict = {
    "left_l4" : level_holding_time,
    "right_l4" : level_holding_time, 
    "left_l3" : level_holding_time, 
    "right_l3" : level_holding_time, 
    "left_l2" : level_holding_time,
    "right_l2" : level_holding_time, 
    "left_l1" : level_holding_time, 
    "right_l1" : level_holding_time, 
    "pick_up_coral_from_ground" : [0.9, 1.3], 
    "pick_up_algea_from_reef" : [1.4, 1.7], 
    "climb" : [2.5, 3.5]
}

# l1/2 would be in key if I had them
key_actions = [ #button
    'left_l4', codes_for_actions_dict.get('left_l4'), 
    'right_l4',  codes_for_actions_dict.get('right_l4'), 
    'left_l2', codes_for_actions_dict.get('left_l2'),
    'right_l2', codes_for_actions_dict.get('rightl2'),
    'left_l1', codes_for_actions_dict.get('left_l1'),
    'right_l1', codes_for_actions_dict.get('right_l1'),
    'switch_auto_scoring_method',  codes_for_actions_dict.get('switch_auto_scoring_method')
]

# climb is in absolute for some reason
absolute_actions = [ #trigger/joystick
    'climb', codes_for_actions_dict.get("climb"),
    'left_l3', 'right_l3', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3")]

non_holding_actions = [ # actions on robot that are instant press 
    'switch_auto_scoring_method', codes_for_actions_dict.get("switch_auto_scoring_method")
]

trigger_actions = [
    'left_l3', 'right_l3', 'pick_up_coral_from_ground', 'pick_up_algea_from_reef', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3")
]

moving_action_codes = [ # joystick codes (used to mitigate minor joystick movements)
    "abs_x", "abs_y", "abs_rx", "abs_ry"
]

# I apologize for making you see the above mess.

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

def show_wait_longer():
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("WAIT")

    # Print in green
    print(Fore.YELLOW + ascii_text + Style.RESET_ALL)


if __name__ ==  "__main__" :
    show_false()
    show_correct()
    show_custom("IF YOUR SEEING THIS, it is too late, I am already dead and you are reading my code thinking \"this bitch\"")
