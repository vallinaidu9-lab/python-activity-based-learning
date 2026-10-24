
# Hospital Ward Occupancy Monitoring

wards = ["General", "ICU", "Emergency"]

beds = [100, 20, 30]

occupancy = [
    [60, 80, 90],
    [10, 15, 22],
    [20, 25, 28]
]

peak = 0

for i in range(len(wards)):
    print("Ward:", wards[i])

    for j in range(3):
        patients = occupancy[i][j]

        percentage = (patients / beds[i]) * 100

        print("Day", j + 1, "Utilization:", percentage, "%")

        if patients > beds[i]:
            print("Capacity exceeded!")

        if patients > peak:
            peak = patients
            peak_ward = wards[i]
            peak_day = j + 1

    print()

print("Peak occupancy:", peak)
print("Peak ward:", peak_ward)
print("Peak demand day:", peak_day)
