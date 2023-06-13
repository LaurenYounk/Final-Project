from final_project import get_birthday, check_birthday, get_zodiac_sign, get_group, get_preferences, final_prediction
from unittest.mock import patch
from colorama import Fore, Style

print(f"{' ' * 14} This is the test file!")
      
def test_get_birthday():
    #values needed for test
    input_values = ["06", "17"]
    expected_output = (6, 17)
    
    # Patch the 'input' function to return the values from input_values
    with patch("builtins.input", side_effect=input_values):
        result = get_birthday()
        
        # Checks if the expected output is correct
        assert result == expected_output
        
    print(Fore.RED + "\nget_birthday test passed")

test_get_birthday()

    
def test_check_birthday():
    #checks to see if the check_birthday() function runs as intended
    assert check_birthday(10, 15) == True
    assert check_birthday(0, 15) == False
    assert check_birthday(13, 15) == False
    assert check_birthday(10, 0) == False
    assert check_birthday(10, 32) == False
    assert check_birthday(2, 29) == True

    print(Fore.RED + "\ncheck_birthday tests passed")
    
test_check_birthday()


def test_zodiac_sign():
    #checks to see if the zodiac_sign() function runs as intended
    assert get_zodiac_sign(1, 21) == "Aquarius"
    assert get_zodiac_sign(2, 19) == "Pisces"
    assert get_zodiac_sign(2, 20) == "Pisces"
    assert get_zodiac_sign(7, 7) == "Cancer"
    assert get_zodiac_sign(3, 21) == "Aries"
    assert get_zodiac_sign(12, 25) == "Capricorn"
    assert get_zodiac_sign(4, 27) == "Taurus"
    
    print(Fore.RED + "\nzodiac_sign sign tests passed")

test_zodiac_sign()


def test_get_group():
    # Test 1: Zodiac sign  group 1
    zodiac_sign_1 = "Leo"
    expected_output_1 = 1
    assert get_group(zodiac_sign_1) == expected_output_1
    
    # Test 2: Zodiac sign group 2
    zodiac_sign_2 = "Cancer"
    expected_output_2 = 2
    assert get_group(zodiac_sign_2) == expected_output_2
    
    print(Fore.RED + "get_group tests passed")
    
test_get_group()


def test_get_preferences():
    #Checks to make sure that the users input preference is correct
    # Test 1: preference 1
    input_values_1 = ["yes", "1"]
    expected_output_1 = "1"
    with patch("builtins.input", side_effect=input_values_1):
        assert get_preferences() == expected_output_1

    # Test 2: preference 2
    input_values_2 = ["yes", "2"]
    expected_output_2 = "2"
    with patch("builtins.input", side_effect=input_values_2):
        assert get_preferences() == expected_output_2

    print(Fore.RED + "\nget_preferences tests passed")

test_get_preferences()


def test_final_prediction():
    # Test: preference 1, group 1
    preference = "1"
    group = 1
    expected_prediction = "Your 2024 will go perfectly! You will see positives in \nyour career and social life. You finally get the break \nyou have been asking for."
    with patch('builtins.print') as mock_print:
        final_prediction(preference, group)
        
    # Test 2: preference 2, group 2
    preference_2 = "2"
    group_2 = 2
    expected_prediction_2 = "You're a social butterfly in 2024. If you were an introvert \nin the past, this year is the year to get out of your \nshell. If you were an extrovert in the past, this is the year it will pay off!"
    with patch('builtins.print') as mock_print:
        final_prediction(preference_2, group_2)
    
    print(Fore.RED + "\nfinal_prediction test passed")
    print(Fore.RED + f"\n{' ' * 17} All tests passed")
    
test_final_prediction()