from config import reef_locations_list, show_false, show_correct, training_list
from photo_of_reef_pole_to_letter import display_photo, display_photo_false
import random, time, math, os, sys, keyboard


time_list = []
correct_counter = 0
incorrect_counter = 0

correct_dict = {}
incorrect_dict = {}
time_per_action_dict = {}

def main(wait_time_range):
    global time_list, correct_counter, incorrect_counter, correct_dict, incorrect_dict

    running = True
    while running:
        reef_location_picked = random.choice(reef_locations_list)
        
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
        
        time.sleep(random.uniform(wait_time_range[0], wait_time_range[1]))

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

    main([0.25, 0.5])
    stats(filename)
