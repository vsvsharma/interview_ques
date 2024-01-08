"""
Program to replace the given character from string without using replace function.
replace(old_char,new_char)
"""
def replace_string(str,old_char,new_char):
    modified_str=""
    for char in str:
        if char==old_char:
            modified_str += new_char
        else:
            modified_str += char
    return modified_str

str="varun"
old_char="v"
new_char="t"
new_str=replace_string(str,old_char,new_char)
print(f"Old String was {str}")
print(f"New modified string is {new_str}")
