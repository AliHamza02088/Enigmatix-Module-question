"""
Given a positive integer n written as abcd... (a, b, c, d... being digits)
 and a positive integer p. we want to find a positive integer k, 
 if it exists, such that the sum of the digits of n taken to the successive 
 powers of p is equal to k * n.

"""

def dig_pow(p: int|str, k: int|str) -> int:
    p = str(p)
    k = str(k)
    sum = 0
    for i in range(len(p)):
        sum += int(p[i]) ** (int(k)+i)
    return sum // int(p)

print(dig_pow(695, 2))
print(dig_pow(46288, 3))