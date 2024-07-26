"""
Problem  18
"""
def valid_parentheses(s):
    result = []
    
    for char in s:
        if char == '(':
            result.append(char)
        elif char == ')':
            if not result:
                return False
            result.pop()
    
    return not result

# Example usage:
print(valid_parentheses("()"))              #=> True
print(valid_parentheses(")(()))"))          #=> False
print(valid_parentheses("("))               #=> False
print(valid_parentheses("(())((()())())"))  #=> True
