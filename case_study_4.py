
# Student Timetable Conflict Detection

schedule = [
    ("Maths", 9, 10, "Room1"),
    ("Python", 10, 11, "Room2"),
    ("English", 11, 12, "Room1")
]

valid = True

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        course1, start1, end1, room1 = schedule[i]
        course2, start2, end2, room2 = schedule[j]

        # Check overlapping times
        if start1 < end2 and start2 < end1:
            print(course1, "and", course2, "have a time conflict")
            valid = False

        # Check same room at the same time
        if room1 == room2 and start1 < end2 and start2 < end1:
            print("Room conflict:", room1)
            valid = False

if valid:
    print("Timetable is valid")
else:
    print("Timetable has conflicts")
