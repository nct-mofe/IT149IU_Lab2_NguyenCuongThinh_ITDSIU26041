total_ms = int(input("Total milliseconds: "))

# Convert all time units using one loop
units = [
    ("day", 86400000),
    ("hour", 3600000),
    ("minute", 60000),
    ("second", 1000),
    ("millisecond", 1)
]

rem = total_ms
values = []
parts = []

for unit, size in units:
    value = rem // size
    rem = rem % size

    values.append(value)
    suffix = "" if value == 1 else "s"
    parts.append(f"{value} {unit}{suffix}")

d, h, m, s, ms = values

# Format as HH:MM:SS.milliseconds
total_hours = d * 24 + h
print(f"{total_hours:02d}:{m:02d}:{s:02d}.{ms:03d}")

# Convert back to milliseconds to verify
total_check = (
    d * 86400000 + h * 3600000
    + m * 60000 + s * 1000 + ms
)
print("Verification:", total_check == total_ms)

# Display all time units
print(" ".join(parts))