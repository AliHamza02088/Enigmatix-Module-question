"""
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the
 string should be retained.
"""

def reverseString(sequence: str) -> str:
    sequence += " "
    seq_lst = []
    s_seq = ""
    for char in sequence:
        if char.isalnum():
            s_seq += char
        elif char.isspace():
            s_seq += " "
            seq_lst.append(s_seq[::-1])
            s_seq = ""
    reversed = "".join(seq_lst)
    return reversed[1:]

print(reverseString("This is an example"))
print(reverseString("double  spaces"))


