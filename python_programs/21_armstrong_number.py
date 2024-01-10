"""
Check the number whether its a armstrong or not.
"""
def check_armstrong(num):
    str_num=str(num)
    n=len(str_num)
    armstrong_sum=0

    for digit in str_num:
        armstrong_sum += int(digit) ** n
        if armstrong_sum == num:
            return True
        else: False

num=153
check=check_armstrong(num)
print(check)