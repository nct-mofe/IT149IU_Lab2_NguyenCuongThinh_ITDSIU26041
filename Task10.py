def collatz(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence


# Print the sequence and number of steps
n = 6
sequence = collatz(n)
steps = len(sequence) - 1

print(f"n = {n}:", *sequence, end="")
print(f"  ({steps} steps)")

# Find the longest sequence for starting values below 1000
longest_start = 1
longest_steps = 0

for start in range(1, 1000):
    sequence = collatz(start)
    steps = len(sequence) - 1

    if steps > longest_steps:
        longest_start = start
        longest_steps = steps

print(
    f"Longest below 1000: n = {longest_start} "
    f"with {longest_steps} steps"
)