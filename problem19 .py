"""
String Fight
"""

def alphabet_war(sequence: str) -> str:
    left_side: dict = {"w": 4, "p": 3, "b": 2, "s": 1, "t": 0}
    right_side: dict = {"m": 4, "q": 3, "d": 2, "z": 1, "j": 0,}

    l_score: int = 0
    r_score: int = 0

    for char in sequence:
        if char == "t": # Left Side Pretty word
            return "Left Side Wins!"
        elif char == "j": # Right Side Pretty word
            return "Right Side Wins!" 
        elif char in left_side:
            l_score += left_side[char]
        elif char in right_side:
            r_score += right_side[char]

    # Let's see who wins!!!! 
    if l_score > r_score:
        return "Left Side Wins!"
    elif l_score == r_score:
        return "Draw"
    else:
        return "Right Side Wins!"

print(alphabet_war("z"))
print(alphabet_war("tz"))