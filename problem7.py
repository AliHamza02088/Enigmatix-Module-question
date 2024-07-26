"""
Sum all the numbers of a given array ( cq. list ), except the highest 
and the lowest element ( by value, not by index! ). You can not use the
 if statement.
"""
def sumArr(arr):
    arr.sort()
    return sum(arr[1:-1])

print(sumArr([6,2,1,8,10]))
print(sumArr([1,1,11,2,3]))

