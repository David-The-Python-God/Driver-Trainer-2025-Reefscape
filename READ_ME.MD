Setup:
    Meant to run using xbox elite 1/2 or standard logitech. Adjust variables labeled "joystick_deadband_used" and "trigger_deadband_used" to "logitech_joystick/trigger_deadband" in methods/config.py for logitech. 

    Meant to run on windows 11 (probably fine on windows 10). To run on other os, at the very least image display would have to be deleted/altered

    Just "pip install" any libraries that say "cannot be accessed" in the terminal of the project. No special instalizations should be needed (unless you don'y have pip which is sad)
    
    You can adjust controls via config if you have programming knowledge. (but even I find it tedious)

    When adding new controls, make sure to put them in all categories they belong in in methods/config.py. (although there are edge cases accounted for in main.py that might mess it up). Look in controls.txt for full control list.

    

Running:
    Run   "main.py" for controller controls

    Run   "field_memorization/main.py" for field memorization (just reef pole locations for now)

    You may have to re-run programs if they are not running the first time.

    Images may not appear in the front at first, split screen IDE to the right or put image displayed to the front of the screen manually.

    Statistics about your actions will be printed to terminal and saved by default in "sessions_stats.txt" for practicing controller or "memorization_stats.txt" for field memorization practice.

    Modules that main.py calls on are mostly not independently runnable yet.



Created by David Schwarzburg from FRC Team 2910 "Jack In The Bot" to prep for driver practice on 2910 robot "SPECTRE" for offseason 2025 reefscape competition.
    Pls follow me on github, I have to brag to the other programmers on my team: https://github.com/David-The-Python-God. 
   
Thanks to Sudhir Chebiyam (former driver, cheif engineer, lead programmer, GOAT) for explaining me the nuances of the keybindings for SPECTRE and thanks to Monishk Illango (subsytem programmer, trogdor programmer) for tediously explaning
    structure of controls when I did not understand anything


PS: I know the code is very messy and slow. It was a quick 1-day prototype meant to help me get driver, it was not meant to be: cross-compatible, maintainable, scalable, clean, optomized, or made in a better programming langauge.
