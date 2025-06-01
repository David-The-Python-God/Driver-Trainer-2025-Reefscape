
def text_to_control(act):
    print(f"\033[1;34m{act.upper()}\033[0m") # blue text (this is like regex magic bullshit but it do be working ish)


if __name__ == "__main__" : 
    text_to_control("TEST")


# def text_to_control():
#     running = True
#     while running:
#         action = (random.choice(actions_list)).lower()
#         time_before = time.time()
#         print(f"\033[1;34m{action.upper()}\033[0m") # blue text (this is like regex magic bullshit but it do be working ish)

#         action_done = None

#         while action_done == None:  # wait for the user to press the button
#             events = []
#             events = get_gamepad()  # listner function, but not in background?
#             for event in events:    # goes through ALL events recorded

#                 if action in key_actions:  # so pressing joystick isn't disrupted by mooving joystick
#                     if (event.ev_type == "Key") and event.state != 0: # other types are relitive and sync changes which are not user inputs
#                         print(f"Event detected: {event.ev_type} - {event.code} - {event.state}")
#                         action_done = event.code
#                         break
#                 else:
#                     if (event.ev_type == "Absolute") and event.state != 0: # other types are relitive and sync changes which are not user inputs

#                         # so that triggers must be fully pressed and don't get cofused with slight joystick drift except when user heavily moves joystick
#                         if ((action in trigger_actions) and event.state >= 240) or (action not in trigger_actions and event.state >= 1000):
#                             print(f"Event detected: {event.ev_type} - {event.code} - {event.state}")
#                             action_done = event.code
#                             break
                    

#         time_spent = time.time() - time_before
#         print("time_spent:", time_spent)       
            


#         #  add waiting time and check before and after time to encourage holding of the button like on real bot scoring


#         # display correct/false for the button    # add to correct and incorrect counter  # add to dict of correct/incorrect # if correct ad time_spent to time_list
#         if action_done.lower() == codes_for_actions_dict.get(action):

#             if action not in non_holding_actions:
#                 time.sleep(1)
                
#                 print("\033[1;34mLET GO NOW\033[0m")
                
        
#             show_correct()
#             correct_counter += 1
#             correct_actions_dict[action] = correct_actions_dict.get(action, 0) + 1  # second value in .get is the default
#             time_list.append(time_spent)
#         else:
#             print("Correct action was:", codes_for_actions_dict.get(action))
#             show_false()
#             incorrect_counter += 1
#             incorrect_actions_dict[action] = incorrect_actions_dict.get(action, 0) + 1
        

#         time.sleep(random.randint(1,3))

#         if keyboard.is_pressed('esc'):
#              running = False

             

# def local_stats():
#     print("\n")

#     if len (time_list) > 0:   
#         sum = 0
#         for time_amount in (time_list):
#             sum += time_amount
#         print("Average time spent on correct decision =", sum/(len(time_list)))
#     else: 
#         print("No correct actions were taken, so no average time can be calculated.")

#     print("\n")

#     print("Percentage of actions correct =", correct_counter/(correct_counter+incorrect_counter))

#     print("\n")
    
#     print("Correct actions dict:")
#     # Sort by values descending
#     for key in sorted(correct_actions_dict, key=correct_actions_dict.get, reverse=True):
#         print(key, " " * (35 - len(key)), correct_actions_dict[key])

#     print("\n")

#     print("Incorrect actions dict:")
#     # Sort by values descending
#     for key in sorted(incorrect_actions_dict, key=incorrect_actions_dict.get, reverse=True):
#         print(key, " " * (35 - len(key)), incorrect_actions_dict[key])


