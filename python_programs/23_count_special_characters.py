"""
Program to calculate digits,special character,alphabets.
"""
def count_characters(input_string):
    
    alphabet_count = 0
    digit_count = 0
    special_char_count = 0

    for char in input_string:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_char_count += 1

    
    return alphabet_count, digit_count, special_char_count


input_str = "varunsharma0111@gmail.com"
alpha_count, digit_count, special_count = count_characters(input_str)

print(f"Alphabets: {alpha_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_count}")
