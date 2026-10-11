import math

def gcd(a, b):
    while b != 0:
        remainder = a % b
        print(f"{a} % {b} = {remainder}")
        a, b = b, remainder

    return a


a, b = 84, 36
print(f"a = {a}, b = {b}")

result = gcd(a, b)
lcm = a * b // result

print(f"gcd = {result}, lcm = {lcm}")

# Check the result using math.gcd()
assert result == math.gcd(a, b)