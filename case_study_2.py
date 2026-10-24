
capacity = 100
water = 50
threshold = 80

inflow = [20, 30, 10, 5, 25]
outflow = [10, 15, 20, 10, 15]

for day in range(5):
    water = water + inflow[day] - outflow[day]

    if water > capacity:
        print("Day", day + 1, ": Overflow!")
        water = capacity

    if water < 0:
        print("Day", day + 1, ": Water shortage!")
        water = 0

    print("Day", day + 1, "- Water level:", water)

    if water >= threshold:
        print("Threshold reached on day", day + 1)
        threshold = capacity + 1
