"""
You are given a string. Suppose a character c
 occurs 4 times in the string. Replace these consecutive 
 occurrences of the character 'c' with (4, c) in the string.
"""

text = "0222311"
a = text[0]
count = 0
for i in text:
    if i == a:
        count +=1
    else:
        print((count , a), end=" ")
        a = i
        count = 1

else:
    print((count , a))