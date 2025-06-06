              
logitech_trigger_deadband = 255 # this is completely maxed out
logitech_joystick_deadband = 1000 # just below 10% of full trigger

xbox_trigger_deadband = 180  # this is because the trigger is set to not go all the way down (full down is 255 like logitech) (also triggers on my xbox elite have different 1/2 down maximums)
xbox_joystick_deadband = 3500   #around 11% deadband: xbox range is about 3x logitech 32k and very sensitive

joystick_dead_band_used = xbox_joystick_deadband
trigger_dead_band_used = xbox_trigger_deadband


"""
Acions need to add:
    manual L1s

    zeroe arm
    deadicted defualtt state (bumpers)

    level-intake combos

    manual l4-l2

    manual eject (this will just be other actions that we will use as eject)
"""


actions_list = [
    'left_l4', 'right_l4', 'left_l3', 'right_l3', 'left_l2', 'right_l2',
    'left_l1_base', 'right_l1_base', 'left_pyramid_l1', 'right_pyramid_l1',
    'go_to_net_position', "go_to_processor_position",
    'intake_coral_from_ground_straight', 'intake_coral_from_ground_horizontal', 'intake_coral_from_station_straight', 
    'intake_algea_from_reef', 'intake_algea_from_human_player', 'intake_algea_from_ground', 'intake_algea_from_mark', # mark
    'climb', 'switch_auto_scoring_method', 'arm_up_for_set_up'
]

succeding_actions_dict = {
    'go_to_net_position' : "score_in_net", "go_to_processor_position" : "score_in_processor"
}

images_list = [] # not needed, each image is just named the action

codes_for_actions_dict = {
    "left_l4" : "btn_tl", 
    "right_l4" : "btn_tr", 
    "left_l3" : "abs_z", 
    "right_l3" : "abs_rz", 
    'left_l2' : "btn_south",
    'right_l2' : 'btn_east',

    'left_l1_base' : 'btn_south',
    'right_l1_base' : 'btn_east',
    
    'left_pyramid_l1' : 'abs_z',
    'right_pyramid_l1' : 'abs_rz',


    "intake_coral_from_ground_straight" : "abs_rz", 
    'intake_coral_from_station_straight' : 'btn_east',
    'intake_coral_from_ground_horizontal' : 'btn_tr',
    "intake_algea_from_reef" : "abs_z", 
    'intake_algea_from_ground' : 'btn_tl', 
    'intake_algea_from_human_player' : 'btn_west',
    'intake_algea_from_mark' : 'btn_south',
    "climb" : "abs_hat0y", 
    "switch_auto_scoring_method" : "btn_thumbl",
    'go_to_net_position' : 'btn_tr',
    "go_to_processor_position" : 'abs_rz',
 
    "score_in_processor" : 'abs_z',  # scoring in processor and barge is combo, but choosing to use right button for position and left for score
    "score_in_net" : 'btn_tl',

    "arm_up_for_set_up" : 'abs_hat0x'

}

general_level_holding_time = [1, 1.7]
hold_time_for_actions_dict = {   # hold times based on practice match vids
    "left_l4" : general_level_holding_time,
    "right_l4" : general_level_holding_time, 
    "left_l3" : general_level_holding_time, 
    "right_l3" : general_level_holding_time, 
    "left_l2" : general_level_holding_time,
    "right_l2" : general_level_holding_time,  
    "intake_coral_from_ground_straight" : [0.85, 1.2], 
    'intake_coral_from_ground_horizontal': [0.8, 1],     
    'intake_algea_from_human_player' : [1.3, 1.8], # very subjective time amount need to hold until algea delivered)
    'intake_coral_from_station_straight' : [1.1, 1.5], # based of of auto only
    'intake_algea_from_ground' : [1.2, 1.6], 
    "intake_algea_from_reef" : [1.4, 1.7], 
    "climb" : [2.5, 3.5],
    'intake_algea_from_mark' : [1.3, 1.5], # Only in one video where processor needs to be scorred twice on our side
    'go_to_net_position' : [0.8, 1.1], 
    "go_to_processor_position" : [0.9, 1.2], 
    "score_in_processor" : [0.6, 0.8],
    "score_in_net" : [0.2, 0.5], 
    "arm_up_for_set_up" : [1, 1.5], # subjective time amount (need to hold until ready by technician)

    'left_pyramid_l1' : [1.25, 1.45],  #also need picture for this  
    'right_pyramid_l1' : [1.25, 1.45],
    'left_l1_base' : [0.9, 1.15],           
    'right_l1_base' : [0.9, 1.15]
}

key_actions = [ #button
    'left_l4', codes_for_actions_dict.get('left_l4'), 
    'right_l4',  codes_for_actions_dict.get('right_l4'), 
    'left_l2', codes_for_actions_dict.get('left_l2'),
    'right_l2', codes_for_actions_dict.get('rightl2'),
    'switch_auto_scoring_method',  codes_for_actions_dict.get('switch_auto_scoring_method'),
    'intake_coral_from_ground_horizontal', codes_for_actions_dict.get('intake_coral_from_ground_horizontal'),
    'intake_algea_from_human_player', codes_for_actions_dict.get('intake_algea_from_human_player'),
    'intake_coral_from_station_straight', codes_for_actions_dict.get('intake_coral_from_station_straight'),
    'intake_algea_from_ground', codes_for_actions_dict.get('intake_algea_from_ground'),
    'intake_algea_from_mark', codes_for_actions_dict.get('intake_algea_from_mark'),
    'go_to_net_position', codes_for_actions_dict.get('go_to_net_position'),
    "score_in_net",
    'left_l1_base', 'right_l1_base'
]

# POV is in absolute for some reason
absolute_actions = [ #trigger/joystick
    'climb', codes_for_actions_dict.get("climb"),
    'left_pyramid_l1', 'right_pyramid_l1',
    "arm_up_for_set_up", codes_for_actions_dict.get('arm_up_for_set_up'),
    'left_l3', 'right_l3', 'intake_coral_from_ground_straight', 'intake_algea_from_reef', "go_to_processor_position", codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3"), "score_in_processor"]

non_holding_actions = [ # actions on robot that are instant press 
    'switch_auto_scoring_method', codes_for_actions_dict.get("switch_auto_scoring_method")
]

trigger_actions = [
    'left_l3', 'right_l3', "go_to_processor_position", 'intake_coral_from_ground_straight', 'intake_algea_from_reef', 'score_in_processor', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3"),
    'left_pyramid_l1', 'right_pyramid_l1'
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
