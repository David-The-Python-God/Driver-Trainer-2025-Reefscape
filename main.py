import random, time, math
import keyboard
from methods.config import actions_list, codes_for_actions_dict, show_correct, show_false, key_actions, absolute_actions, non_holding_actions, trigger_actions, moving_action_codes
from inputs import get_gamepad

from methods.text_to_control import text_to_control
from methods.image_to_control import show_image
from methods.voice_to_control import voice_to_control


time_list = []
correct_counter = 0
incorrect_counter = 0

correct_actions_dict = {}
incorrect_actions_dict = {}

logitech_trigger_deadband = 255 # this is completely maxed out
logitech_joystick_deadband = 1000 # just below 10% of full trigger

xbox_trigger_deadband = 175  # this is because the trigger is set to not go all the way down (full down is 255 like logitech)
xbox_joystick_deadband = 2000   #around 6% deadband: xbox range is about 3x logitech 32k and very sensitive

joystick_dead_band_used = logitech_joystick_deadband
trigger_dead_band_used = logitech_trigger_deadband

def main(hold_time_range, wait_time_range):
    global time_list, correct_counter, incorrect_counter, correct_actions_dict, incorrect_actions_dict
    running = True
    while running:
        action = (random.choice(actions_list)).lower()
        

        if random.randint(0,2) == 0:
            l = show_image(action)
            action_done = l[0]
            time_before = l[1]
            show_image("reset") # prob don't do anything

        else:
            if random.randint(0, 1) == 0:

                text_to_control(action)

            else:
                voice_to_control(action)


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
                                action_done = event.code
                                break
                    

        time_spent = time.time() - time_before
        print("time_spent:", time_spent)       
            

        if action_done.lower() == codes_for_actions_dict.get(action):

            if action not in non_holding_actions:
                time.sleep(random.uniform(hold_time_range[0], hold_time_range[1]))
                
                print("\033[1;34mLET GO OF THE KEY NOW\033[0m")     

        
            show_correct()
            correct_counter += 1
            correct_actions_dict[action] = correct_actions_dict.get(action, 0) + 1  # second value in .get is the default
            time_list.append(time_spent)

        else:
            print("Correct action was:", codes_for_actions_dict.get(action))
            show_false()
            incorrect_counter += 1
            incorrect_actions_dict[action] = incorrect_actions_dict.get(action, 0) + 1
        

        time.sleep(random.uniform(wait_time_range[0], wait_time_range[1]))

        if keyboard.is_pressed('esc'):
             running = False



def stats(filename = "session_stats.txt"):
    print("\n")

    with open(filename, "a") as file:

        file.write(input("Name?") + "\n")

        if len (time_list) > 0:   
            sum = 0
            for time_amount in (time_list):
                sum += time_amount
            print("Average time spent on correct decision =", sum/(len(time_list)))
            file.write("Average time spent on correct decision = " + str(sum/(len(time_list))) + "\n")
        else: 
            print("No correct actions were taken, so no average time can be calculated.")
            file.write("No correct actions were taken, so no average time can be calculated.\n")

        print("\n")

        print("Percentage of actions correct =", correct_counter/(correct_counter+incorrect_counter))
        file.write("Percentage of actions correct = " + str(correct_counter/(correct_counter+incorrect_counter)) + "\n")

        print("\n")
        
        print("Correct actions dict:")
        file.write("\nCorrect actions dict:\n")
        # Sort by values descending
        for key in sorted(correct_actions_dict, key=correct_actions_dict.get, reverse=True):
            print(key, " " * (35 - len(key)), correct_actions_dict[key])
            file.write(f"{key} {' ' * (35 - len(key))} {correct_actions_dict[key]}\n")

        print("\n")

        print(" Incorrect actions dict:")
        file.write("\nIncorrect actions dict:\n")
        # Sort by values descending
        for key in sorted(incorrect_actions_dict, key=incorrect_actions_dict.get, reverse=True):
            print(key, " " * (35 - len(key)), incorrect_actions_dict[key])
            file.write(f"{key} {' ' * (35 - len(key))} {incorrect_actions_dict[key]}\n")
        
        file.write("\n")


        success_rate_dict = {}
        # Get a union of all actions
        all_actions = set(correct_actions_dict.keys()) | set(incorrect_actions_dict.keys())

        for action in all_actions:
            correct = correct_actions_dict.get(action, 0)
            incorrect = incorrect_actions_dict.get(action, 0)
            total = correct + incorrect

            if total > 0:
                success_rate = correct / total
            else:
                success_rate = None  # No attempts made for this action

            success_rate_dict[action] = success_rate

        sorted_actions = sorted(
            success_rate_dict.items(), 
            key=lambda x: (x[1] is not None, x[1]), 
            reverse=True
        )
        
        for action in sorted_actions:
            spaces = " " * (26 - len(action[0]))
            print("success rate for", action[0], "=", spaces, action[1])
            file.write(f"success rate for {action[0]} = {spaces} {action[1]}\n")
    
        file.write("SESSION END \n\n\n\n\n")


if __name__ == "__main__":
    while True:

        filename = input("Enter the filename to save stats (default: session_stats.txt): ")
        if not filename:
            filename = "session_stats.txt"
        elif filename.lower() == "g" or filename.lower() == "guest":
            filename = "guest_stats.txt"

        main([1, 2.6], [0.75, 1.5]) # time randge for holdign button and witing for action respectively
        
        # if input("wanna save stats?").lower() == "y":
        stats(filename)

        if input("Do you want to run again? (y/n): ").lower() != 'y':
            print("Exiting the program.")
            break    