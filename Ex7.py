import matplotlib.pyplot as plt

# Basic binary-to-decimal function
def bin_to_dec(bits):
    val = 0

    for ch in bits:
        val = val * 2 + (1 if ch == "1" else 0)

    return val


# 1 and 4. Input and validate the binary string
while True:
    bits = input("Binary string: ")

    if bits and all(ch in "01" for ch in bits):
        break

    print("Invalid input. Enter only 0 and 1, with at least one digit.")

# 2. Compare the result with int(bits, 2)
decimal = bin_to_dec(bits)
builtin_decimal = int(bits, 2)

print("Manual conversion:", decimal)
print("int(bits, 2):", builtin_decimal)


# 3. Implement decimal-to-binary conversion
def dec_to_bin(number):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        result = str(number % 2) + result
        number //= 2

    return result


number = int(input("Decimal number (non-negative integer): "))
print("Binary:", dec_to_bin(number))

# 5. Plot bit positions and their powers of 2
positions = list(range(len(bits)))
powers = [2 ** position for position in positions]

plt.bar(positions, powers)
plt.xticks(positions)
plt.xlabel("Bit position (rightmost = 0)")
plt.ylabel("Power of 2")
plt.title("Binary positional weights")
plt.show()