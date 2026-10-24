
# Examination Performance Analysis

answer_key = ["A", "B", "C", "D", "A"]

students = [
    ["A", "B", "C", "A", "B"],
    ["A", "C", "C", "D", "A"],
    ["B", "B", "A", "D", "C"]
]

success = [0, 0, 0, 0, 0]

for student in students:
    for i in range(5):
        if student[i] == answer_key[i]:
            success[i] = success[i] + 1

for i in range(5):
    rate = (success[i] / len(students)) * 100

    print("Question", i + 1)
    print("Success rate:", rate, "%")

    if rate >= 70:
        print("Performance: Easy")
    elif rate >= 40:
        print("Performance: Moderate")
    else:
        print("Performance: Difficult")

    print()

# Find the most frequently missed question
missed = success[0]
question = 1

for i in range(5):
    if success[i] < missed:
        missed = success[i]
        question = i + 1

print("Most frequently missed question:", question)
