def roman_to_int(roman_number):
    conversion_dictionary = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_number = 0
    old_character = ''

    for character in roman_number[::-1]:
        val_char = conversion_dictionary[character]
        var_old_char = conversion_dictionary[old_character]
        if val_char >= var_old_char:
            int_number += val_char
        else:
            int_number -= val_char
        old_character = character
    return(int_number)
