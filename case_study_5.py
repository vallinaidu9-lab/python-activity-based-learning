
# Courier Charge Optimization

weight = float(input("Enter parcel weight in kg: "))
distance = int(input("Enter distance in km: "))
urgent = input("Urgent delivery? (yes/no): ")
restricted = input("Is parcel restricted? (yes/no): ")

if weight <= 0 or distance <= 0:
    print("Invalid weight or distance")

elif restricted == "yes":
    print("No service available for restricted parcel")

else:
    normal_charge = weight * 20 + distance * 2

    if urgent == "yes":
        express_charge = normal_charge + 100
    else:
        express_charge = normal_charge + 50

    print("Normal delivery charge: Rs.", normal_charge)
    print("Express delivery charge: Rs.", express_charge)

    if normal_charge <= express_charge:
        print("Selected service: Normal Delivery")
    else:
        print("Selected service: Express Delivery")
