"""
Program to find the sum of sum of integers in a string.
"""
def sum_of_int(str):
    int_sum=0
    for i in str:
        if i.isdigit():
            int_sum += int(i)
    return int_sum
    
str="varun0111"
final_sum=sum_of_int(str)
print(f"Sum of integers present in given string is {final_sum}")