
# Environmental Monitoring Data Analyzer

readings = [
    [40, 50, 60],
    [70, 80, 90],
    [30, 45, 55]
]

total = 0
count = 0
highest = readings[0][0]
lowest = readings[0][0]

for i in range(len(readings)):
    for j in range(len(readings[i])):
        value = readings[i][j]

        total = total + value
        count = count + 1

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

        if value <= 50:
            print(value, "- Good")
        elif value <= 75:
            print(value, "- Moderate")
        else:
            print(value, "- Poor")

average = total / count

print("Average reading:", average)
print("Highest reading:", highest)
print("Lowest reading:", lowest)
