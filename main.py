import random, time, math
import keyboard
from methods.config import actions_list, testing_list, codes_for_actions_dict, show_correct, show_false, show_wait_longer, second_combo_code_dict, hold_time_for_actions_dict, non_holding_actions, trigger_actions, moving_action_codes, succeding_actions_dict
from methods.config import joystick_dead_band_used, trigger_dead_band_used
from inputs import get_gamepad

from methods.text_to_control import text_to_control
from methods.voice_to_control import voice_to_control
from methods.photo_to_control import show_photo

time_list = []
correct_counter = 0
incorrect_counter = 0

correct_actions_dict = {}
incorrect_actions_dict = {}
time_per_action_dict = {}

def main(hold_time_range, wait_time_range):

    global time_list, correct_counter, incorrect_counter, correct_actions_dict, incorrect_actions_dict
    running = True
    while running:
        # action = (random.choice(actions_list)).lower()
        action = 'climb'
        

        if random.randint(0,5) >= 3:
            l = show_photo(action)
            if l:
                action_done = l[0]
                time_before = l[1]
                show_photo("reset") # prob don't do anything
            else:
                continue

        else:
            if random.randint(0, 1) == 0:
                text_to_control(action)

            else:
                voice_to_control(action)

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
                                action_done = event.code
                                
                                events = [] # hopefully to clear of old events but that is not how gamepad works anyway so....

                                break

                    
        

                    
        events = []
        time_spent = time.time() - time_before
        print("time_spent:", time_spent)       

        # for _ in range(10):
        #     get_gamepad()  # flush any queued input
        #     time.sleep(0.01)
            

        if action_done.lower() == codes_for_actions_dict.get(action):

            if ((action not in non_holding_actions) and action not in second_combo_code_dict.keys()) or action == 'climb':  # I hate this logic so much a;jqre;j;qgi

                if action != 'climb':
                    specialized_wait_range = hold_time_for_actions_dict.get(action, [0, 0])
                    time.sleep(random.uniform(specialized_wait_range[0], specialized_wait_range[1]))    
                
                show_correct()

                if action in succeding_actions_dict.keys():
                    print("\033[1;34mWAITING FOR KEY PRESS THAT COMPLETES ACTION\033[0m")  

                    time_before = time.time()
                    action_done = None
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
                                    if event_code in moving_action_codes:
                                        print("you moved joystick to far whilst going for another action")
                                        time.sleep(0.1)

                                    elif not (event_code == 'abs_rz') or action == 'climb':   # because trigger amount fluctuates when at half-press mode so you don't want to accidentally trigger wrong tirgger
                                        print(f"Suceeding event detected: {event.ev_type} - {event_code} - {event.state}")
                                        action_done = event.code
                                        
                                        events = [] # hopefully to clear of old events but that is not how gamepad works anyway so....

                                        break
                    
                    time_spent = time.time() - time_before
                    print("time_spent:", time_spent)       

                    succeding_action = succeding_actions_dict.get(action)
                    if action_done.lower() == codes_for_actions_dict.get(succeding_action):
                        specialized_wait_range = hold_time_for_actions_dict.get(succeding_action, [0, 0])
                        time.sleep(random.uniform(specialized_wait_range[0], specialized_wait_range[1]))
                        print("\033[1;34mCORRECT SUCCEDING ACTION\033[0m")
                        correct_counter += 1
                        correct_actions_dict[succeding_action] = correct_actions_dict.get(succeding_action, 0) + 1  # second value in .get is the default
                        time_per_action_dict[succeding_action] = time_per_action_dict.get(succeding_action, 0) + time_spent
                        time_list.append(time_spent)
                    
                    else:
                        print("\033[31mINCORRECT SUCCEDING ACTION BUT CORRECT PRECEEDING ACTION\033[0m")
                        print(f"Correct action for {succeding_action} was:", codes_for_actions_dict.get(succeding_action))
                        incorrect_counter += 1
                        incorrect_actions_dict[succeding_action] = incorrect_actions_dict.get(succeding_action, 0) + 1

                
                else:
                    correct_counter += 1
                    correct_actions_dict[action] = correct_actions_dict.get(action, 0) + 1  # second value in .get is the default
                    time_per_action_dict[action] = time_per_action_dict.get(action, 0) + time_spent
                    time_list.append(time_spent)
                
                print("\033[1;34mLET GO OF THE KEY NOW\033[0m", '\n\n-------------------------------------------------------------------\n') 

            elif action in second_combo_code_dict:
                try:
                    events = get_gamepad()  # listner function, but not in background?

                except Exception:
                    print("game pad disconnected")
                    return
                
                action_done = None

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

                                elif event_code != "btn_thumbr": # specifically to not include the combos which in this case use thumbr
                                    print(f"Event detected: {event.ev_type} - {event_code} - {event.state}")
                                    action_done = event_code
                                    
                                    events = [] # hopefully to clear of old events but that is not how gamepad works anyway so....

                                    break
                

                if action_done == second_combo_code_dict.get(action):
                    specialized_wait_range = hold_time_for_actions_dict.get(action, [0, 0])
                    time.sleep(random.uniform(specialized_wait_range[0], specialized_wait_range[1]))    
                    show_correct()
                    print("\033[1;34mLET GO OF THE KEY NOW\033[0m", '\n\n-------------------------------------------------------------------\n')

                else:
                    print(f"Correct action for {action} was:", second_combo_code_dict.get(action))
                    show_false()
                    print('\n-------------------------------------------------------------------\n')
                    incorrect_counter += 1
                    incorrect_actions_dict[action] = incorrect_actions_dict.get(action, 0) + 1

                    
                    
            else:
                show_correct()
                print('\n-------------------------------------------------------------------\n')
                correct_counter += 1
                correct_actions_dict[action] = correct_actions_dict.get(action, 0) + 1  # second value in .get is the default
                time_per_action_dict[action] = time_per_action_dict.get(action, 0) + time_spent
                time_list.append(time_spent)

        else:
            print(f"Correct action for {action} was:", codes_for_actions_dict.get(action))
            show_false()
            print('\n-------------------------------------------------------------------\n')
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

        file.write("Average time per correct action dict: \n")
        print("time per action:")
        action_avg_times = [
            (action, time_per_action_dict.get(action, 0) / correct_actions_dict.get(action))
            for action in time_per_action_dict
        ]

        # Sort the list in descending order by average time
        action_avg_times.sort(key=lambda x: x[1], reverse=True)

        # Write the sorted values
        for action, time_per_action in action_avg_times:
            file.write(f"{action} = {' ' * (35 - len(action))} {time_per_action} \n")

        file.write("\n")

        file.write("Sucess rate for actions dict:\n")
        print("success rate for actions dict:")
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
            spaces = " " * (35 - len(action[0]))
            print(action[0], "=", spaces, action[1])
            file.write(f"{action[0]} = {spaces} {action[1]}\n")
    
        file.write("SESSION END \n\n\n\n\n")


if __name__ == "__main__":
    while True:
        # gamepad_you_there_question_mark()

        filename = input("Enter the filename to save stats (default: session_stats.txt): ")
        if not filename:
            filename = "session_stats.txt"
        elif filename.lower() == "g" or filename.lower() == "guest":
            filename = "guest_stats.txt"

        main([1, 1.7], [0.75, 1.5]) # defualt time randge for holdign button and waiting for action respectively (holding derived from sudhir practice match coral)
        
        # if input("wanna save stats?").lower() == "y":
        stats(filename)

        if input("Do you want to run again? (y/n): ").lower() != 'y':
            print("Exiting the program.")
            break    