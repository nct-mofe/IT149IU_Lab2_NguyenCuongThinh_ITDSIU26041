import matplotlib.pyplot as plt

# 1. Input the starting wage, annual raise rate and number of years
o = float(input("Starting wage ($/hr): "))
p = float(input("Annual raise rate (e.g. 0.03 for 3%): "))
number_of_years = int(input("Number of years: "))

years = list(range(number_of_years + 1))
wages = [o]
previous_wage = o

# 2. Show the increase from the previous year
# 5. Calculate the real wage by subtracting a 2% annual inflation rate
print(f"{'Year':<6}{'Wage':>12}{'Increase':>12}{'Real wage':>12}")

for n in range(1, number_of_years + 1):
    w = o * (1 + p) ** n
    increase = w - previous_wage
    real_wage = o * (1 + p - 0.02) ** n

    print(f"{n:<6}{w:>12.2f}{increase:>12.2f}{real_wage:>12.2f}")

    wages.append(w)
    previous_wage = w

# 3. Plot the wage growth curve
plt.plot(years, wages, marker="o")
plt.xlabel("Year")
plt.ylabel("Wage ($/hr)")
plt.title("Wage growth")
plt.show()

# 4. Compare annual raise rates of 2%, 5% and 8%
for rate in [0.02, 0.05, 0.08]:
    rate_wages = []

    for n in years:
        rate_wages.append(o * (1 + rate) ** n)

    plt.plot(years, rate_wages, label=f"{rate:.0%}")

plt.xlabel("Year")
plt.ylabel("Wage ($/hr)")
plt.title("Wage growth at different rates")
plt.legend()
plt.show()