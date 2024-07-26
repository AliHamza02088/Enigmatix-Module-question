"""
Valid pin
"""

def valid_pin(pin):
    pin = str(pin)
    try:
        s = int(pin)
        if len(pin) == 4 or len(pin) == 6:
            return True
        return False
    except:
        return False

s1 = "1234"
s2 = "12345"
s3 = "a234"

print(valid_pin(s1))
print(valid_pin(s2))
print(valid_pin(s3))