"""
You are given words. Some words may repeat.
 For each word, output its number of occurrences. 
 The output order should correspond with the input order 
 of appearance of the word.

"""

a = ["bcdef", "abcdefg", "bcde", "bcdef"]
s = set(a)
print(len(s))
for i in s:
    count = 0
    for j in a:
         if i == j:
            count+=1
    
    print(count,end=" ")
    

