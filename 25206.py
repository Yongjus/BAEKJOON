import sys

grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

GPA = 0
total_credit = 0
for i in range(20):
    name, credit, grade = sys.stdin.readline().split()
    if grade != "P":
        credit = float(credit)
        GPA = GPA + credit * grades[grade]
        total_credit += credit
print(GPA / total_credit)
