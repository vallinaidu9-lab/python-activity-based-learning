
# Traffic Flow and Congestion Analysis

roads = ["Road A", "Road B", "Road C"]

traffic = [
    [40, 60, 90],
    [30, 80, 110],
    [20, 40, 50]
]

capacity = 100
peak = 0

for i in range(len(roads)):
    print(roads[i])

    for j in range(3):
        vehicles = traffic[i][j]

        if vehicles > peak:
            peak = vehicles
            peak_road = roads[i]
            peak_time = j + 1

        if vehicles > capacity:
            print("High Congestion:", vehicles)
        elif vehicles >= 60:
            print("Medium Congestion:", vehicles)
        else:
            print("Low Congestion:", vehicles)

    if max(traffic[i]) > capacity:
        print("Road exceeds capacity")

    print()

print("Peak traffic:", peak)
print("Peak road:", peak_road)
print("Peak time interval:", peak_time)
