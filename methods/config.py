logitech_trigger_deadband = 255 # this is completely maxed out
logitech_joystick_deadband = 1000 # just below 10% of full trigger
xbox_trigger_deadband = 175  # this is because the trigger is set to not go all the way down (full down is 255 like logitech) (also triggers on my xbox elite have different 1/2 down maximums)
xbox_joystick_deadband = 3500   #around 11% deadband: xbox range is about 3x logitech 32k and very sensitive

joystick_dead_band_used = xbox_joystick_deadband
trigger_dead_band_used = xbox_trigger_deadband

from itertools import chain



"""
Actions need to add:
    

 """


actions_list = [
    'left_l4', 'right_l4', 'left_l3', 'right_l3', 'left_l2', 'right_l2',
    'left_l1_base', 'right_l1_base', 'left_pyramid_l1', 'right_pyramid_l1', 'go_to_manual_l1',
    'go_to_net_position', "go_to_processor_position",
    'intake_coral_from_ground_straight', 'intake_coral_from_ground_horizontal', 'intake_coral_from_station_straight', 
    'intake_algea_from_reef', 'intake_algea_from_human_player', 'intake_algea_from_ground', 'intake_algea_from_mark', # mark
    'climb', 'zeroe_gyro', 'zeroe_arm', 
    'switch_auto_scoring_method', 'prematch_check','exit_climb',
    'score_left_l4_and_intake_algea', 'score_right_l4_and_intake_algea',
    'score_left_l2_and_intake_algea', 'score_right_l2_and_intake_algea'
]

testing_list = []

important_actions = []

succeding_actions_dict = {} # actions that ALWAYS happen after the other


# As scores happen after intake in pick-place, but not nessasarily in shoot
all_intakes = []

all_scores = []

all_important_intakes = list(set(all_intakes) & set(important_actions))

all_important_scores = list(set(all_intakes) & set(important_actions))

# kept for reference when keybinding
codes_for_actions_dict = {
    "left_l4" : "btn_tl", 
    "right_l4" : "btn_tr", 
    "left_l3" : "abs_z", 
    "right_l3" : "abs_rz", 
    'left_l2' : "btn_south",
    'right_l2' : 'btn_east',

    'left_l1_base' : 'btn_south',
    'right_l1_base' : 'btn_east',
    'left_pyramid_l1' : 'btn_tl',   
    'right_pyramid_l1' : 'btn_tr',
    'go_to_manual_l1' : 'btn_north',
    'score_manual_l1' : 'btn_west',

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
    'slow_drivetrain_whilst_climbing' : 'abs_rz', #
 
    "score_in_processor" : 'abs_z',  # scoring in processor and barge is combo, but choosing to use right button for position and left for score
    "score_in_net" : 'btn_tl',

    "prematch_check" : 'abs_hat0x',  #needs secenario picture (funny time)
    'exit_climb' : "abs_hat0y", # techincially this is the same code as pov up even though on seperate buttons but just ignore it in operation
    'zeroe_gyro' : 'btn_start',
    'zeroe_arm' : 'btn_select',


# Put first button of combo here.
    'score_left_l4_and_intake_algea' : 'btn_thumbr',
    'score_right_l4_and_intake_algea' : 'btn_thumbr',

    'score_left_l2_and_intake_algea' : 'btn_thumbr',
    'score_right_l2_and_intake_algea' : 'btn_thumbr'     

}

# put second button of combo here
second_combo_code_dict =  {}

general_level_holding_time = [1.1, 1.65]
hold_time_for_actions_dict = {   # hold times based on practice match vids
    
    #l3 had the most variance among the same side, but l2 is very variant when it comes to front vs back
    "left_l4" : [1.4, 1.65],
    "right_l4" : [1.4, 1.65], 
    "left_l3" : [1.3, 1.6],    
    "right_l3" : [1.3, 1.6], 
    "left_l2" : [1.2, 1.6],     # very noticable that back l2 is 0.2 secodns faster than front L2 (without even counting the no-turning bonus with back l2)
    "right_l2" : [1.2, 1.6],  

    'left_pyramid_l1' : [1.5, 1.75],  
    'right_pyramid_l1' : [1.5, 1.75],
    'left_l1_base' : [1.35, 1.5],              # auto L1 increased by ~0.25 seconds than what you might see on camera becuase backing up is part of the l1 movement (although a sometimes optional part)
    'right_l1_base' : [1.35, 1.5],
    'go_to_manual_l1' : [1.3, 1.6],  #guestimated
    'score_manual_l1' : [0.3, 0.6], 

    "intake_coral_from_ground_straight" : [0.85, 1.2], 
    'intake_coral_from_ground_horizontal': [0.8, 1],     
    'intake_algea_from_human_player' : [1.3, 1.8], # very subjective time amount need to hold until algea delivered)
    'intake_coral_from_station_straight' : [1.1, 1.5], # time based off of auto only
    'intake_algea_from_ground' : [1.2, 1.6], 
    "intake_algea_from_reef" : [1.4, 1.7], 
    # "climb" : [2.5, 3.5], # climb is press now??
    'intake_algea_from_mark' : [1.3, 1.5], # Only in one video where processor needs to be scorred twice on our side
    'go_to_net_position' : [1.15, 1.4],   #increased since original
    "go_to_processor_position" : [0.9, 1.2], 
    "score_in_processor" : [0.6, 0.8],  
    "score_in_net" : [0.4, 0.6], #icnreased bottom boudnary since original

    "prematch_check" : [1, 1.5], # subjective time amount (need to hold until ready by technician)

    'score_left_l4_and_intake_algea' : [2.9, 3.4],
    'score_right_l4_and_intake_algea' : [2.9, 3.4],
    'score_left_l2_and_intake_algea' : [2.5, 3],  # couldn't find in video, just a guess of -0.5 from l4 combo
    'score_right_l2_and_intake_algea' : [2,5, 3],

    'slow_drivetrain_whilst_climbing' :   [2.5, 3] # about how long it takes to climb from start of climb position

    
}

key_actions = [ #button actions
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
    'left_l1_base', 'right_l1_base',
    'zeroe_gyro', codes_for_actions_dict.get('zeroe_gyro'),
    'zeroe_arm', codes_for_actions_dict.get('zeroe_arm'),
    'left_pyramid_l1', 'right_pyramid_l1',

    'score_left_l4_and_intake_algea', codes_for_actions_dict.get("score_left_l4_and_intake_algea"),
    'score_right_l4_and_intake_algea',
    'score_left_l2_and_intake_algea',
    'score_right_l2_and_intake_algea'
]

absolute_actions = [ #trigger/joystick/dpad actions
    'climb', codes_for_actions_dict.get("climb"),
    'exit_climb', 
    'slow_drivetrain_whilst_climbing', 
    "prematch_check", codes_for_actions_dict.get('prematch_check'),
    'left_l3', 'right_l3', 'intake_coral_from_ground_straight', 'intake_algea_from_reef', "go_to_processor_position", codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3"), "score_in_processor"]

non_holding_actions = [ # actions on robot that are instant press 
    'switch_auto_scoring_method', codes_for_actions_dict.get("switch_auto_scoring_method"),
    'exit_climb', codes_for_actions_dict.get('exit_climb'),
    'zeroe_gyro', codes_for_actions_dict.get('zeroe_gyro'),
    'zeroe_arm', codes_for_actions_dict.get('zeroe_arm'),
    'climb', codes_for_actions_dict.get('climb')
]

trigger_actions = [
    'left_l3', 'right_l3', "go_to_processor_position", 'intake_coral_from_ground_straight', 'intake_algea_from_reef', 'score_in_processor', codes_for_actions_dict.get("left_l3"), codes_for_actions_dict.get("right_l3"),
    'slow_drivetrain_whilst_climbing',
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
