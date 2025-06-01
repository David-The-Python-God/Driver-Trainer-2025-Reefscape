from inputs import get_gamepad

print("Waiting for controller input... (Press any button)")

try:
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key" or event.ev_type == "Absolute":
                print(f"Event detected: {event.ev_type} - {event.code} - {event.state}")

                
except KeyboardInterrupt:
    print("Program terminated by user.")