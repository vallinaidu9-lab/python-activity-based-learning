
# Progressive Water Tariff Analysis

usage = [50, 120, 180, 250]
fixed_fee = 50

for i in range(len(usage)):
    units = usage[i]

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = bill + fixed_fee

    if units > 200:
        bill = bill + 100
        print("Household", i + 1, "- Excessive usage!")

    print("Household", i + 1)
    print("Water used:", units, "units")
    print("Total bill: Rs.", bill)
    print()
