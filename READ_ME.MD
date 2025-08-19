IF something is not working, you want to adjust something, or you do not know how to operate: read these (sorry):


    Setup:
        Meant to run using xbox elite 1 or 2 or standard logitech. Adjust variables labeled "joystick_deadband_used" and "trigger_deadband_used" to "logitech_joystick/trigger_deadband" in methods/config.py for logitech.  (if neigther of these, find deadband by taking 10 percent of your max range from joystick by using input test)

        The triggers on xbox controller elite 1 or 2 should be set to max out half way. (otherwise you will have to customze trigger dead band)

        Meant to run on windows 11 (probably fine on windows 10). To run on other os, at the very least the image display would have to be deleted/altered

        Just "pip install" any libraries that say "cannot be accessed" in the terminal of the project. No special instalizations should be needed (unless you don't have pip which is sad)
        
        You can adjust controls via config if you have programming knowledge. (but even I find it tedious)

        IMPORTANT When adding new controls, make sure to put them in all categories they belong in in methods/config.py. (although there are edge cases accounted for in main.py that will probably mess it up). DPAD IS ABSOLUTE INPUT Look in controls.txt for full control list.

        

    Running:
        Run   "main.py" for controller controls

        Run   "field_memorization/main.py" for field memorization (might just be reef pole locations)

        You may have to re-run programs if they are not running the first time.

        Images may not appear in the front at first, split screen IDE to the right or put image displayed to the front of the screen manually. (if you split screen, you might have to run again)

        Statistics about your actions will be printed to terminal and saved by default in "sessions_stats.txt" for main or "memorization_stats.txt" for field memorization practice.

        Modules that main.py calls on are mostly not independently runnable yet.


    Operation:
        Press enter in terminal after running main to accept default file saving

        if running main.py, press enter again to not do all actions first, otherwise press y and enter

        Make terminal fully visible as it is crucial to the simulator

        Press and HOLD escape on the keyboard right after finishing an action and in the terminal a question will popup: "name?". Awnser it, and results will be saved. Don't awnser and results won't be saved or printed.

        The triggers on xbox controller should be set to max out half way. Although this may cause you to have to push hard or push them multiple times if they do not reach large deadband for triggers

        Most of the actions can be performed in multiple keybinds, but only 1 is choosen to be correcv to give the user a rigid and more simple control.

        Instructions will come in 3 differnet media: text, images, voice

        Actions that need to be held on the robot have holding times (you wont lose points if you don't hold, but the holding times are realistic to real matches so wait until "LET GO" to let go of a certain keybind)

        A dotted line being printed in the terminal signifies the end of a action so you should definitely let go of keybinds by the to not get it wrong for the next action

        Joystick movements won't lose you points but you do get notified int eh terminal if you move them very far

        Succeding actions have two keybinds for two actions one after the other that each have a waiting time (like scoring in net is first getting into position (wait) and then press shoot (wait) )

        Combo actions have two keybinds for one action that need to be performed simultaneously/near-simlutaneously (without wait time in between keybinds like score l4 and intake off of reef where first press right stick then l4 but almost simultaneously)

        The start button with the two squares on it to the left of the xbox-logo is the "HOME gyro" button. the other button in the middle (to the right) is the home-arm button. 

        



Created by David Schwarzburg from FRC Team 2910 "Jack In The Bot" to prep for driver practice on 2910 robot "SPECTRE" for offseason 2025 reefscape competition (did get me driver).
    PLS FOLLOW ME ON GITHUB, I have to brag to the other programmers on my team: https://github.com/David-The-Python-God. 
   
Thanks to Sudhir Chebiyam (driver, chief engineer, lead programmer, ABSOLUTE INSPIRATIONAL GOAT) for explaining me the nuances of the keybindings for SPECTRE and thanks to Monishk Illango (subsytem programmer, trogdor programmer) for tediously explaning structure of control code when I did not understand anything about it at the time.


PS: I know the code is very messy, slow, not-customizable enough, not-scalable...  . It was a quick couple-day prototype meant to help me get driver, it was not meant to be: cross-compatible, maintainable, scalable, clean, optomized, or made in a better programming langauge. Look at todo.txt for just some of the broken dreams


https://www.google.com/imgres?q=borat%20very%20nice&imgurl=https%3A%2F%2Fwww.clker.com%2Fcliparts%2F7%2F8%2Fa%2F0%2F1498553633398980412very-nice-borat.hi.png&imgrefurl=https%3A%2F%2Fwww.clker.com%2Fclipart-421295.html&docid=JKkTZwPeiqK_sM&tbnid=_NofTcZftFaQnM&vet=12ahUKEwiqqvyzoOuNAxW-CTQIHWI-FsEQM3oECGEQAA..i&w=521&h=600&hcb=2&ved=2ahUKEwiqqvyzoOuNAxW-CTQIHWI-FsEQM3oECGEQAA