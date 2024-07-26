"""
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k
consecutive strings taken in the array.
"""

def longestString(arr: list[str], k: int):
    joined_str_arr = []
    length_of_joined_str = []

    for i in range(len(arr)):
        new_string = "".join(arr[i:i+k])
        joined_str_arr.append(new_string)
        length_of_joined_str.append(len(new_string))

    max_length = max(length_of_joined_str)
    first_index = length_of_joined_str.index(max_length) 
    return joined_str_arr[first_index]

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2
print(longestString(strarr, k))