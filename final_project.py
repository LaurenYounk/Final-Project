import time
from colorama import Fore, Style


def project_intro():
    """ Displays the introduction of the Fortune Teller prject and takes user input to determine if they want to continue
    
    Parameters
    ---------
    N/A
    
    Returns
    -------
    None
    
    Notes
    -----
    - Takes user input
    - There is no specific output since it calls and interacts with other functions but doesn not return specifics
    
    """
    #Fortune Teller introduction
    print( "˖⁺‧₊‧⁺˖˖⁺‧₊˚♡˚₊‧⁺˖ The Fortune Teller ˖⁺‧₊˚♡˚₊‧⁺˖˖⁺‧₊‧⁺˖")
    print(Fore.MAGENTA + f"\n{' ' * 9}Hello, welcome to the Fortune Teller!!")
    print(Style.RESET_ALL + f"\n{'☆' * 56}")
    
    # Asks for the users input to determine to continue or not
    answer = input(Style.RESET_ALL + f"\n Would You Like To Continue? ")
    
    if answer.lower() == "yes":
        print(Fore.BLUE + f"\n{' ' * 13} Good choice ˖ ࣪‧₊˚⋆✩٩(ˊᗜˋ*)و ✩")
        print(Style.RESET_ALL + f"\n{'☆' * 56}")
        
        #calls other functions
        birth_month, birth_day = get_birthday()
        preference = get_preferences() 
        
        if preference is not None:
            zodiac_sign = get_zodiac_sign(birth_month, birth_day)
            perform_action(preference)
            print(f"\n{'☆' * 56}")
            # Asking the user if they want to see their fortune
            final_answer = input("\n Would You Like To See Your Fortune? ")

            if final_answer.lower() == "yes":
                print(Fore.GREEN + f"\n{' ' * 15} Last check ᕙ( •̀ ᗜ •́ )ᕗ")
                # initiates the last portions of this code
                final_prediction(preference, get_group(zodiac_sign))
            else:
                print(f"\n{' ' * 16}Okay, have a great day!!")
    
    else:
        print(f"\n{' ' * 16}Okay, have a great day!!")
           
        
def get_birthday():
    """Prompt user to enter birth month and day to figure out the zodiac sign
    
    Parameters
    ----------
    N/a
    
    Returns
    -------
    None
    
    Examples
    --------
        Enter your birth month (MM): 06
        Enter your birth day (DD): 17
        Your Zodiac Sign is: Gemini
        
        Enter your birth month (MM): 07
        Enter your birth day (DD): 07
        Your Zodiac Sign is: Cancer
        
    Notes
    -----
    - User input
    - There is no specific output since it calls and interacts with other functions but doesn not return specifics
    
    """
    
    while True:
        birth_month_input = input("\nEnter your birth month (MM): ")
        # Prompts user to input their birth month
        if not birth_month_input.isdigit():
            print(f"\n{' ' * 21}Try again")
            continue
            
        birth_month = int(birth_month_input)
        
        # Prompts user to input their birth day
        birth_day_input = input("\nEnter your birth day (DD): ")
        if not birth_day_input.isdigit():
            print(f"\n{' ' * 21}Try again")
            continue
            
        birth_day = int(birth_day_input)
        
        # Ensures the birth month and day are valid
        if not check_birthday(birth_month, birth_day):
            print(f"\n{' ' * 21}Try again")
            continue

        # Determines users zodiac signs
        zodiac_sign = get_zodiac_sign(birth_month, birth_day)
        print(Fore.CYAN + f"\n{' ' * 15}Your Zodiac Sign is:", zodiac_sign)
        return birth_month, birth_day
        
    
def check_birthday(birth_month, birth_day):
    """Determines if the birth month and day are in valid ranges
    
    Parameters
    ----------
    birth_month: integer 
        birth month as an integer
    birth_day: integer
        birth day as an integer
        
    Returns
    -------
    True or False: bool
        True if birth month and day are valid or false if invalid
        
    Examples
    --------
    Enter your birth month (MM): 06
    Enter your birth day (DD): 17
    return True 
    
    Enter your birth month (MM): 14
    Enter your birth day (DD): 17
    return False 
    
    """
    # Ensures the user input is a valid birth month and day   
    if 1 <= birth_month <= 12 and 1 <= birth_day <= 31:
        return True
    else:
        return False
     
        
def get_zodiac_sign(birth_month, birth_day):
    """Determines the zodiac sign based on the birth month and day.

    Parameters
    ----------
    birth_month : int
        The birth month (1-12).
    birth_day : int
        The birth day (1-31).

    Returns
    -------
    zodiac_sign: str
        The zodiac sign corresponding to the birth month and day.
        
    Notes
    -----
    There are two sets of numbers for each sign indicating the range 
    
    i.e. Aries is from march 21 - April 20
    """
    month = birth_month
    day = birth_day

    #ranges of zodiac signs
    if (month == 1 and day >= 21) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 20):
        return "Aries"
    elif (month == 4 and day >= 21) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Gemini"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 23):
        return "Leo"
    elif (month == 8 and day >= 24) or (month == 9 and day <= 23):
        return "Virgo"
    elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        return "Libra"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "Scorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
        return "Capricorn"
    else:
        return "Invalid date" 
    
    return zodiac_sign 


def get_group(zodiac_sign):
    """Determines the group an individual is in based on zodiac sign
    
    Parameters
    ----------
    zodiac_sign: str
        Zodiac sign 
        
    Returns
    -------
    1 or 2: int
        Group number corresponding to given zodiac sign
        
    Examples
    --------
    zodiac_sign: Gemini 
    Group: 1
    
    zodiac_sign: Taurus
    Group: 2
    
    """
    group_one = ["Aries", "Sagittarius", "Leo", "Gemini", "Libra", "Aquarius"]
    
    #Creates the distinct zodiac sign groups
    if zodiac_sign in group_one:
        return 1
    else:
        #if not in group 1 must be in group 2
        return 2
    
    
def get_preferences():
    """Asks for users input for their preferences and returns choice
    
    Parameters
    ----------
    N/a
    
    Returns
    -------
    choice: int 
        The preference an individual picked, 1 or 2
    get_preferences(): str
        user's input preference as a string
        
    Notes
    -----
    - focuses on user input
        
    """
    #Asks users if they want to continue
    print(Style.RESET_ALL + f"\n{'☆' * 56}")
    answer = input(f"\n Would You Like To Continue? ")

    if answer.lower() == "yes":
        print(Fore.YELLOW + f"\n{' ' * 15} Just Checking (ㅅ´ ˘ `)")
        
        # Prompts the user to choose their vacation preference
        while True:
            print(Style.RESET_ALL + f"\n{'☆' * 56}")
            print(Fore.GREEN + f"\n {' ' * 16} Would you rather:")
            print(Style.RESET_ALL + "\n1. Go on vacation on a tropical island with a pet dog")
            print("2. Go on vacation to a big city with a pet cat")

            choice = input(Style.RESET_ALL + "\n Enter your preference (1 or 2): ")

            # Ensures the answer is within the valid outputs
            if choice not in ["1", "2"]:
                print(f"\n{' ' * 21}Try again")
                continue

            return choice

    elif answer.lower() == "no":
        print(f"\n{' ' * 16}Okay, have a great day!!")
        return None
    else:
        print(f"\n{' ' * 21}Try again")
        return get_preferences()

    
def perform_action(preference):
    """Performs an action due to a user's preference
    
    Parameters
    ----------
    preference: str
        users preference, either 1 or 2
        
    Returns
    -------
    None
    
    Notes
    -----
    There is no specific output since it calls and interacts with other functions but doesn not return specifics
    """
    print(Style.RESET_ALL + f"\n{'☆' * 56}")

    # If choice is 1 the following action is preformed 
    if preference == "1":
        print(f"\n{' ' * 2}You chose vacation on a tropical island with a dog!")
        print(Fore.MAGENTA + f"\n{' ' * 22}૮⍝• ᴥ •⍝ა")
        moving_waiting_code()

    # If choice is 2 the following action is preformed 
    elif preference == "2":
        print(f"\n{' ' * 5}You chose vacation to a big city with a cat!")
        print(Fore.MAGENTA + f"\n{' ' * 23} ∧,,,∧")
        print(Fore.MAGENTA + f"{' ' * 23}( ̳•·• ̳)")
        print(Fore.MAGENTA + f"{' ' * 23}/    づ♡")
        moving_waiting_code()
    

def moving_waiting_code():
    """
    Prints a moving waiting code animation
    
    Parameters
    ----------
    n/a
    
    Returns
    -------
    none
    
    Notes
    -----
    uses the time library! range deems how many, sleep is the time delay
    """
    print(Style.RESET_ALL + f"\n{' ' * 17}Getting prediction")
    
    # Utilizes the time library to create a moving thought (...)
    for _ in range(5):
        time.sleep(0.5) 
        print(f"\n{' ' * 25}.", end = "\n", flush = True)  
    
    print(f"\n{' ' * 23}Done!")
    

def final_prediction(preference, get_group):
    """Provides final prediction based on zodiac sign and preferences
    
    Parameters
    ----------
    preference: str 
        User's preference, 1 or 2
    get_group: int
        Users zodiac sign or group, 1 or 2
        
    Returns
    -------
    None 
    
    """
    prediction = ""
    
    if preference == "1":
        if get_group == 1:
            # The fortune if an individual is in group 1 for the zodiac sign and chose option 1
            prediction = "Your 2024 will go perfectly! You will see positives in \nyour career and social life. You finally get the break \nyou have been asking for."
        elif get_group == 2:
            # The fortune if an individual is in group 2 for the zodiac sign and chose option 1
            prediction = "Your 2024 will start out a little rocky in your social \nlife. Look out for individuals who have been testing \nyour friendship, and tell them your concerns."

    elif preference == "2":
        if get_group == 1:
            # The fortune if an individual is in group 1 for the zodiac sign and chose option 2
            prediction = "Your 2024 will be full of positive career events. Plan \nto make more money and negotiate raises. If there is \nroom to go up in your field, you will be climbing the ladder this year."
        elif get_group == 2:
            # The fortune if an individual is in group 2 for the zodiac sign and chose option 2
            prediction = "You're a social butterfly in 2024. If you were an introvert \nin the past, this year is the year to get out of your \nshell. If you were an extrovert in the past, this is the year it will pay off!"

    print(Style.RESET_ALL + f"\n{'☆' *56}")
    print(Fore.BLUE + f"\n {' ' * 6}˚♡˚₊‧⁺˖ Here is your Prediction!˖⁺‧₊˚♡˚")
    # prints out the prediction
    print(Style.RESET_ALL + f"\n{prediction}")
    
    
#Calling the main function   
project_intro()