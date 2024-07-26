"""
Split Camel Case
"""
def splitCamelCase(sequence):
    for i in range(len(sequence)):
        if sequence[i].isupper():
            p = i
            return " ".join((sequence[:p], sequence[p:]))
    return sequence

a1 = "camelCasing"
a2 = "identifier"
a3 = "aliHamza"
a4 = "AliHamza"
print(splitCamelCase(a1))
print(splitCamelCase(a2))
print(splitCamelCase(a3))
print(splitCamelCase(a4))
