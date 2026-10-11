import matplotlib.pyplot as plt

# 4. Add an iteration counter to the basic function
def is_perfect(n, show_iterations=False):
    if n < 2:
        if show_iterations:
            print("Divisors checked:", 0)
        return False

    s = 1
    i = 2
    iterations = 0

    while i * i <= n:
        iterations += 1

        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i

        i += 1

    if show_iterations:
        print("Divisors checked:", iterations)

    return s == n


# 1. Input a number and test it using is_perfect()
number = int(input("Number to test: "))
result = is_perfect(number, show_iterations=True)
print(number, result)

# 2. List all perfect numbers between 1 and 10000
perfect_numbers = []

for n in range(1, 10001):
    if is_perfect(n):
        perfect_numbers.append(n)

print("Perfect numbers:", perfect_numbers)

# 3. Count perfect numbers in a given inclusive range
start = int(input("Range start: "))
end = int(input("Range end: "))
count = 0

for n in range(start, end + 1):
    if is_perfect(n):
        count += 1

print("Count:", count)

# 5. Plot the distribution of perfect numbers
plt.hist(perfect_numbers, bins=20, range=(1, 10000), edgecolor="black")
plt.xlabel("Number")
plt.ylabel("Number of perfect numbers")
plt.title("Distribution of perfect numbers from 1 to 10000")
plt.show()