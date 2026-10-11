import matplotlib.pyplot as plt
from time import perf_counter

# Basic iterative Fibonacci function
def fib(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


# 1. Input n and print F(n)
n = int(input("n (non-negative integer): "))
print(f"F({n}) = {fib(n)}")

seq = [fib(i) for i in range(n + 1)]

# 2. Display ratios, starting at n = 2 to avoid division by F(0)
print(f"{'n':<6}{'F(n)/F(n-1)':>16}")

for i in range(2, n + 1):
    ratio = seq[i] / seq[i - 1]
    print(f"{i:<6}{ratio:>16.6f}")

# 3. Plot Fibonacci growth
plt.plot(range(n + 1), seq, marker="o")
plt.xlabel("n")
plt.ylabel("F(n)")
plt.title("Fibonacci growth")
plt.show()


# 4. Compare iterative and recursive implementations
def fib_recursive(n):
    if n < 2:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Measure both methods on the first ten terms from the basic example
start_time = perf_counter()
iterative_seq = [fib(i) for i in range(10)]
iterative_time = perf_counter() - start_time

start_time = perf_counter()
recursive_seq = [fib_recursive(i) for i in range(10)]
recursive_time = perf_counter() - start_time

print("Iterative:", iterative_seq)
print(f"Iterative time: {iterative_time:.9f} seconds")

print("Recursive:", recursive_seq)
print(f"Recursive time: {recursive_time:.9f} seconds")

# 5. Apply modulo operations to generate a Fibonacci pattern
modulus = int(input("Modulo base (> 0): "))

while modulus <= 0:
    modulus = int(input("Modulo base (> 0): "))

pattern = [value % modulus for value in seq]
print(f"Fibonacci modulo {modulus}:", pattern)