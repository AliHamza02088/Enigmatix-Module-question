"""

Write a function which will take an integer as input and print each digit in a separate line. 
You are not allowed to use str or any other method will convert the integer into string.

"""

def ints(nums):
    a = 0
    while nums>0:
        digits= nums%10
        a = digits
        nums = nums//10
        print(a)

ints(1101)





