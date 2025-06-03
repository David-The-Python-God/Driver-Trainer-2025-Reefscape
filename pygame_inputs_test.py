import pygame  


""" This test is for upcoming test for after holding. should measure inputs regardless of change of them"""
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick name: {joystick.get_name()}")
print(f"Buttons: {joystick.get_numbuttons()}, Hats: {joystick.get_numhats()}, Axes: {joystick.get_numaxes()}")

detected_input = None

# Define trigger axis indices (you may need to adjust these for your controller)
trigger_axes = [2, 5]  # Common for Xbox: 2 = LT, 5 = RT

# Loop until input is detected
while True:
    pygame.event.pump()

    # Check buttons
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            detected_input = f"button_{i}"
            break

    # Check D-pad (hat)
    if detected_input is None:
        for i in range(joystick.get_numhats()):
            hat_value = joystick.get_hat(i)
            if hat_value != (0, 0):
                detected_input = f"hat_{i}_{hat_value}"
                break

    # Check triggers only (not joysticks)
    if detected_input is None:
        for i in trigger_axes:
            if i < joystick.get_numaxes():
                value = joystick.get_axis(i)
                if abs(value) > 0.5:  # Adjust threshold if needed
                    detected_input = f"trigger_axis_{i}_{value:.2f}"
                    break

    if detected_input:
        print(f"Input detected: {detected_input}")
        break

    time.sleep(0.01)\


