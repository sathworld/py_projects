# Converts a Roman Numeral to an integer
def roman_to_int(roman_number):
    # Dictionary for transcoding each value
    conversion_dictionary = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Setting additional variables to NULL
    int_number = 0
    old_character = ''

    # Going through every character in reverse
    for character in roman_number[::-1]:
        # Assigning transcoded values to variables in order to reduce calls to dictionary
        val_char = conversion_dictionary[character]
        var_old_char = conversion_dictionary[old_character]
        # Comparing the current character to the old one
        if val_char >= var_old_char:
            int_number += val_char
        else:
            int_number -= val_char
        # Updating the old character
        old_character = character
    return int_number

# Converts an integer between 0 and 3999 to a Roman Numeral
def int_to_roman(int_number):
    # Dictionary for transcoding each value
    conversion_dictionary = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                             400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    # Setting additional variables to NULL
    roman_number = ""

    # Going through all keys in reverse (1000 -> 900 -> ... ->4 -> 1)
    for value in sorted(list(conversion_dictionary))[::-1]:
        # Appending the correct number of numerals to the roman_number string
        roman_number += int_number // value * conversion_dictionary[value]
        # Subtracting (or using mod) from the number
        int_number %= value

    return roman_number
