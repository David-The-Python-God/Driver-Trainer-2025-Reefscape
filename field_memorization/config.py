reef_locations_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
training_list = ['F', 'G', 'H', 'I', 'J', 'K', 'L']



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


