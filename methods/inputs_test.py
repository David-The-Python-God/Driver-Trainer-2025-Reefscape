from inputs import get_gamepad, UnpluggedError

if __name__ == "__main__" :
    from config import show_custom  
else:
    from methods.config import show_custom

def gamepad_you_there_question_mark():
    try:
        events = get_gamepad()
        for event in events:
            return "bean"

    except UnpluggedError:
        show_custom("NO GAMEPAD")
        

def inputs_test():
    print("Waiting for controller input... (Press any button)")

    try:
        while True:
            events = get_gamepad()
            for event in events:
                if event.ev_type == "Key" or event.ev_type == "Absolute":
                    print(f"Event detected: {event.ev_type} - {event.code} - {event.state}")

                    
    except KeyboardInterrupt:
        print("Program terminated by user.")
    
    except UnpluggedError:
        show_custom("NO GAMEPAD")

if __name__ == "__main__":
    inputs_test()