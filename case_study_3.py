
subjects = ["Maths", "Python", "English"]

exam1 = [40, 60, 50]
exam2 = [55, 70, 45]

total1 = 0
total2 = 0

for i in range(3):
    print(subjects[i])

    change = exam2[i] - exam1[i]

    if change > 0:
        print("Improved by:", change)
    elif change < 0:
        print("Declined by:", -change)
    else:
        print("No change")

    if exam1[i] < 40 and exam2[i] < 40:
        print("Weak subject")

    total1 = total1 + exam1[i]
    total2 = total2 + exam2[i]

print("Exam 1 Total:", total1)
print("Exam 2 Total:", total2)

average = total2 / 3
print("Exam 2 Average:", average)

if average >= 75:
    print("Student Grade: Excellent")
elif average >= 50:
    print("Student Grade: Average")
else:
    print("Student Grade: Needs Improvement")
