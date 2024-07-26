"""

You get an array of numbers, and return the sum of all of the positive ones.
Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0.
You can not use the if statement.
"""



def sum_of_positive(numbers):
    positive_number = [max(0,num) for num in numbers]

    return sum(positive_number)

present_numbers = [1,-4,7,12]
result = sum_of_positive(present_numbers)
print(result)
