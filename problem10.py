"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.
"""
def mid(word: str):
    n = len(word)
    if n%2 == 0:
        mid1 = n // 2
        mid2 = round(n/2)
        return(word[mid1-1:mid2+1])
    else:
        middle = n // 2
        return(word[middle])

even_str = "test"
odd_str = "testing"

print(mid(even_str)) # es
print(mid(odd_str)) # t