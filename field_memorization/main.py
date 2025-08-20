import sys
from config import reef_letters_list, show_false, show_correct, training_list, hold_time_for_levels_dict
from photo_of_reef_pole_to_letter import display_photo, display_photo_false
import random, time, math, os, sys, keyboard
from location_to_keybind import generate_location_to_keybind
from inputs import get_gamepad
from voice_to_keybind import voice_to_control

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # for the methods.config that is in a seperate sub-folder
from methods.config import moving_action_codes,trigger_actions,trigger_dead_band_used,joystick_dead_band_used



time_list = []
correct_counter = 0
incorrect_counter = 0

correct_dict = {}
incorrect_dict = {}
time_per_action_dict = {}

def main(keyboard_wait_time_range, controller_wait_time_range):
    global time_list, correct_counter, incorrect_counter, correct_dict, incorrect_dict

    using_controller = True if input("default: using controller methods") != "n" else False #only 1 method in each controller and keyboard

    running = True
    while running:
        if using_controller: 
            
            l = generate_location_to_keybind() # generate reef location and correct keybind
            reef_location = l[0]
            correct_keybind = l[1]
            reef_level = l[2]

            r = random.randint(0,2) 
            if r == 0:
                print(f"\033[1;34m{reef_location}\033[0m")  # change to custom asci?
            elif r >= 1:                                                      #TEMPORARY, change ==1 later once photo is done
                voice_to_control(reef_location)
            else:
                pass #photo


            action_done = None

            time_before = time.time()

            events = []
            while action_done == None:  # wait for the user to press the button
                events = []
                try:
                    events = get_gamepad()  # listner function, but not in background?

                except Exception:
                    print("game pad disconnected")
                    return

                # for event in events:    # goes through ALL events recorded

                event = events[-1] # saves on latency but doesn't actually remove prior thngs
                if (event.ev_type == "Absolute" or event.ev_type == "Key") and event.state !=0:
                    
                    event_code = event.code.lower()
                    if not (event_code in moving_action_codes and event.state <= joystick_dead_band_used):  # filter out minor joystick movements
                        
                        if not (event_code in trigger_actions and event.state <= trigger_dead_band_used):
                            if event_code in moving_action_codes :
                                print("you moved joystick to far whilst going for another action")
                                time.sleep(0.1)

                            else:  
                                print(f"Event detected: {event.ev_type} - {event_code} - {event.state}")
                                action_done = event.code.lower() 
                                
                                events = [] # hopefully to clear of old events but that is not how gamepad works anyway so....

                                break
            

            reef_location = reef_location[0] # just getting the first letter of the reef location to not clutter stats

            if action_done == correct_keybind:
                time_spent = time.time() - time_before
    

                specialized_wait_range = hold_time_for_levels_dict.get(reef_level, [0, 0])
                time.sleep(random.uniform(specialized_wait_range[0], specialized_wait_range[1]))      # all actions with reef location are hold

                print(time_spent)
                show_correct()
                print('\n-------------------------------------------------------------------\n')
                correct_counter += 1
                correct_dict[reef_location] = correct_dict.get(reef_location, 0) + 1  # second value in .get is the default
                time_per_action_dict[reef_location] = time_per_action_dict.get(reef_location, 0) + time_spent
                time_list.append(time_spent)
                
            else:
                print("Correct keybind was:", correct_keybind)
                show_false()
                print('\n-------------------------------------------------------------------\n')
                incorrect_counter += 1
                incorrect_dict[reef_location] = incorrect_dict.get(reef_location, 0) + 1
            
            time.sleep(random.uniform(controller_wait_time_range[0], controller_wait_time_range[1]))


        else:
                
            reef_location_picked = random.choice(reef_letters_list)
            
            data = display_photo(reef_location_picked)
            reef_letter_inputed = data[0]
            time_spent = data[1]
            print(time_spent)

            if reef_letter_inputed.upper() == reef_location_picked:
                show_correct()
                print('\n-------------------------------------------------------------------\n')
                correct_counter += 1
                correct_dict[reef_location_picked] = correct_dict.get(reef_location_picked, 0) + 1  # second value in .get is the default
                time_per_action_dict[reef_location_picked] = time_per_action_dict.get(reef_location_picked, 0) + time_spent
                time_list.append(time_spent)
            else:
                print("Correct letter was:", reef_location_picked)
                show_false()
                display_photo_false()
                print('\n-------------------------------------------------------------------\n')
                incorrect_counter += 1
                incorrect_dict[reef_location_picked] = incorrect_dict.get(reef_location_picked, 0) + 1
            
            time.sleep(random.uniform(keyboard_wait_time_range[0], keyboard_wait_time_range[1]))




        if keyboard.is_pressed('esc'):
             running = False



def stats(filename):
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
            print("No correct decisions were taken, so no average time can be calculated.")
            file.write("No correct decisions were taken, so no average time can be calculated.\n")

        print("\n")

        print("Percentage of decisions correct =", correct_counter/(correct_counter+incorrect_counter))
        file.write("Percentage of decisions correct = " + str(correct_counter/(correct_counter+incorrect_counter)) + "\n")

        print("\n")
        
        print("Correct decisions dict:")
        file.write("\nCorrect decisions dict:\n")
        # Sort by values descending
        for key in sorted(correct_dict, key= correct_dict.get, reverse=True):
            print(key, " " * (35 - len(key)), correct_dict[key])
            file.write(f"{key} {' ' * (35 - len(key))} {correct_dict[key]}\n")

        print("\n")

        print(" Incorrect actions dict:")
        file.write("\nIncorrect actions dict:\n")
        # Sort by values descending
        for key in sorted(incorrect_dict, key=incorrect_dict.get, reverse=True):
            print(key, " " * (35 - len(key)), incorrect_dict[key])
            file.write(f"{key} {' ' * (35 - len(key))} {incorrect_dict[key]}\n")
        
        file.write("\n")

        file.write("Average time per correct action dict: \n")
        print("time per action:")
        action_avg_times = [
            (action, time_per_action_dict.get(action, 0) / correct_dict.get(action))
            for action in time_per_action_dict
        ]

        # Sort the list in descending order by average time
        action_avg_times.sort(key=lambda x: x[1], reverse=True)

        # Write the sorted values
        for action, time_per_action in action_avg_times:
            file.write(f"{action} = {' ' * (35 - len(action))} {time_per_action} \n")

        file.write("\n")

        file.write("Sucess rate for decisions dict:\n")
        print("success rate for decisions dict:")
        success_rate_dict = {}
        # Get a union of all actions
        all_actions = set(correct_dict.keys()) | set(incorrect_dict.keys())
        

        for action in all_actions:
            correct = correct_dict.get(action, 0)
            incorrect = incorrect_dict.get(action, 0)
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
            spaces = " " * (35 - len(action[0]))
            print(action[0], "=", spaces, action[1])
            file.write(f"{action[0]} = {spaces} {action[1]}\n")
    
        file.write("SESSION END \n\n\n\n\n")

if __name__ == "__main__":
    filename = input("Enter the filename to save stats (default: memorization_stats.txt): ")
    if not filename:
        filename = "field_memorization/memorization_stats.txt"

    main([0.25, 0.5],  [0.75, 1.5])
    stats(filename)

