import math
import matplotlib.pyplot as plt

# Basic Leibniz function
def pi_leibniz(k_terms):
    acc = 0.0
    sgn = 1.0

    for k in range(k_terms):
        acc += sgn / (2 * k + 1)
        sgn *= -1

    return 4 * acc


# 1. Input an error threshold and stop when the error is below it
epsilon = float(input("Error threshold epsilon (> 0): "))

while epsilon <= 0:
    epsilon = float(input("Error threshold epsilon (> 0): "))

acc = 0.0
sgn = 1.0
k = 0
errors = []

while abs(math.pi - 4 * acc) >= epsilon:
    acc += sgn / (2 * k + 1)
    sgn *= -1
    k += 1
    errors.append(abs(math.pi - 4 * acc))

print("Terms:", k)
print("Pi approximation:", 4 * acc)
print("Absolute error:", abs(math.pi - 4 * acc))

# 2. Plot the convergence curve using a logarithmic error scale
plt.plot(range(1, k + 1), errors)
plt.yscale("log")
plt.xlabel("Number of terms")
plt.ylabel("Absolute error")
plt.title("Leibniz convergence")
plt.show()


# 3. Compare Leibniz with Nilakantha and Ramanujan
def pi_nilakantha(k_terms):
    acc = 3.0
    sgn = 1.0

    # Count the leading 3 as the first term
    for k in range(1, k_terms):
        a = 2 * k
        acc += sgn * 4 / (a * (a + 1) * (a + 2))
        sgn *= -1

    return acc


def pi_ramanujan(k_terms):
    acc = 0.0

    for k in range(k_terms):
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = math.factorial(k) ** 4 * 396 ** (4 * k)
        acc += numerator / denominator

    return 1 / (2 * math.sqrt(2) / 9801 * acc)


print(
    f"{'Terms':<8}{'Leibniz error':>18}"
    f"{'Nilakantha error':>20}{'Ramanujan error':>20}"
)

for terms in range(1, 6):
    leibniz_error = abs(math.pi - pi_leibniz(terms))
    nilakantha_error = abs(math.pi - pi_nilakantha(terms))
    ramanujan_error = abs(math.pi - pi_ramanujan(terms))

    print(
        f"{terms:<8}{leibniz_error:>18.10g}"
        f"{nilakantha_error:>20.10g}{ramanujan_error:>20.10g}"
    )

# 4. Visualize the first ten alternating terms with a bar chart
values = []
labels = []

for k in range(10):
    sign = 1 if k % 2 == 0 else -1
    denominator = 2 * k + 1

    values.append(sign / denominator)
    labels.append(f"{'+' if sign == 1 else '-'}1/{denominator}")

plt.bar(labels, values)
plt.axhline(0, color="black", linewidth=0.8)
plt.xlabel("Term")
plt.ylabel("Signed term value")
plt.title("Alternating terms of the Leibniz series")
plt.show()