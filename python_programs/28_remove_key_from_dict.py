"""
Program to remove key from dictionary.
"""
def remove_key_dict(my_dict,key_remove):
    if key_remove in my_dict:
        del my_dict[key_remove]
        print(f"key removed successfully: {key_remove}")
    else:
        print(f"key not found{key_remove}") 

my_dict={'a':1,'b':2,'c':3,'d':4,'e':5}
key_to_remove='b'
updated_dict=remove_key_dict(my_dict,key_to_remove)
print(updated_dict)  