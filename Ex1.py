import pandas as pd
import matplotlib.pyplot as plt
import csv

counts = [19, 22, 25, 18, 20, 24, 21]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 1. Convert the list into a Series and call describe() 
series = pd.Series(counts, index=days)
summary = series.describe()
print(summary)

# 2. Plot the 3-day rolling mean
rolling_mean = series.rolling(3).mean()

plt.plot(days[2:], rolling_mean.iloc[2:], marker="o")
plt.xlabel("Day")
plt.ylabel("3-day rolling mean")
plt.show()

# 3. Detect anomalies where case differ from the mean by more than 2x standard diviation
anomaly_mask = abs(series - series.mean()) > 2 * series.std()
print("Anomalies:", series[anomaly_mask].to_dict())

# 4.  Compare the total number of cases with the previous week
previous_counts = []

for day in days:
    cases = int(input(f"Previous week, {day}: "))
    previous_counts.append(cases)

current_total = sum(counts)
previous_total = sum(previous_counts)

if previous_total == 0:
    percent_change = None
    print("Percent change: undefined (previous total is 0)")
else:
    percent_change = (
        (current_total - previous_total) / previous_total * 100
    )
    print(f"Percent change: {percent_change:.2f}%")

# 5. Save the results using csv.writer()
with open("task1_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Day", "Cases", "Previous week",
        "3-day rolling mean", "Anomaly"
    ])

    for i, day in enumerate(days):
        if i < 2:
            mean = ""
        else:
            mean = rolling_mean.iloc[i]

        writer.writerow([
            day,
            counts[i],
            previous_counts[i],
            mean,
            bool(anomaly_mask.iloc[i])
        ])

    writer.writerow([])
    writer.writerow(["Statistic", "Value"])

    for statistic, value in summary.items():
        writer.writerow([statistic, value])

    writer.writerow(["This week's total", current_total])
    writer.writerow(["Previous week's total", previous_total])
    writer.writerow([
        "Percent change",
        "Undefined" if percent_change is None else percent_change
    ])