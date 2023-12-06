def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        if char not in roman_values:
            return 0
        
        value = roman_values[char]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    # Additional checks for invalid combinations
    invalid_combinations = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]
    for combo in invalid_combinations:
        if combo in roman_string:
            return 0

    return result if 0 < result < 4000 else 0

# Test cases
if __name__ == "__main__":
    roman_numbers = [
        "X", "VII", "IX", "LXXXVII", "DCCVII"
    ]

    for roman_number in roman_numbers:
        print("{} = {}".format(roman_number, roman_to_int(roman_number)))

