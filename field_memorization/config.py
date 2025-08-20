reef_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
training_list = [] #its whichever ones i was struggling on


left_letters_list = ["A", "C", "E", "G", "I", "K"] # if in left then go to left levels to score, othewise irght levels to score
reef_levels_list = ["1 base", "1 pyramid", "2", "3", "4"]
left_reef_levels_to_score_dict = {"1 base" : "btn_south", "1 pyramid" : "btn_tl", "2" : "btn_south","3" : "abs_z","4" : "btn_tl"}
right_reef_levels_to_score_dict = {"1 base" : "btn_east", "1 pyramid" : "btn_tr", "2" : "btn_east","3" : "abs_rz","4" : "btn_tr"}

hold_time_for_levels_dict = {
    "1 base" : [1.35, 1.5], 
    "1 pyramid" : [1.5, 1.75],
    "2" : [1.2, 1.6],
    "3" : [1.3, 1.6],
    "4" : [1.4, 1.65]
}



import pyfiglet
from colorama import Fore, Style, init


def show_false():
        # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("FALSE")

    # Print in red
    print(Fore.RED + ascii_text + Style.RESET_ALL)

def show_correct():
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("CORRECT")

    # Print in green
    print(Fore.GREEN + ascii_text + Style.RESET_ALL)

def show_custom(text, color = Fore.WHITE):
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format(text)

    # Print in green
    print(color + ascii_text + Style.RESET_ALL)

def show_wait_longer():
    # Initialize colorama
    init()

    # Create big ASCII text
    ascii_text = pyfiglet.figlet_format("WAIT")

    # Print in green
    print(Fore.YELLOW + ascii_text + Style.RESET_ALL)


if __name__ ==  "__main__" :
    show_false()
    show_correct()
    show_custom("IF YOUR SEEING THIS, it is too late, I am already dead and you are reading my code thinking \"this bitch\"")


