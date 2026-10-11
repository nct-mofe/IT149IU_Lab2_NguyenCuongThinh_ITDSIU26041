def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


# Collect all primes below 100
primes = []

for n in range(2, 100):
    if is_prime(n):
        primes.append(n)

# Print ten numbers per line, right-aligned in width 4
for i in range(len(primes)):
    print(f"{primes[i]:4d}", end="")

    if (i + 1) % 10 == 0:
        print()

if len(primes) % 10 != 0:
    print()

print(f"{len(primes)} primes below 100")