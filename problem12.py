"""
Sort given string
"""
def sortString(s: str):
    if s == "":
        return ""
    arr = s.split()
    new_arr = arr.copy()

    for word in arr:
        for char in word:
            if char.isdigit():
                new_arr[int(char)-1] = word
    return " ".join(new_arr)

print(sortString("is2 Thi1s T4est 3a"))
print(sortString("4of Fo1r pe6ople g3ood th5e the2"))
print(sortString(""))