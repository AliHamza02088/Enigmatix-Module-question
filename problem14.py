"""
Unique in order
"""

def unique_in_order(sequence: str | list[str | int]):
    char: str = ""
    new_list: list[str] = []
    for i in sequence:
        if i != char:
            char = i
            new_list.append(char)
    return new_list

s1 = "AAAABBBCCDAABBB"
s2 = "ABBCcAD"
s3 = [1, 2, 2, 3, 3]


print(unique_in_order(s1))
print(unique_in_order(s2))
print(unique_in_order(s3))
