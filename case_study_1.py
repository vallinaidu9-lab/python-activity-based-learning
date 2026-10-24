#15

vehicle = input("Enter vehicle type (bike/car): ")
entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")

else:
    if exit < entry:
        hours = (24 - entry) + exit
    else:
        hours = exit - entry

    if vehicle == "bike":
        fee = hours * 10
    elif vehicle == "car":
        fee = hours * 20
    else:
        fee = 0
        print("Invalid vehicle type")

    if vehicle == "bike" or vehicle == "car":
        if fee > 100:
            fee = 100

        print("Parking hours:", hours)
        print("Parking fee: Rs.", fee)
