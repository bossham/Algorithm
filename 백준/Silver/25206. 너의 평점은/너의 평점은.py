grade_points = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

total_grade_points = 0
total_credits = 0

for _ in range(20):
    subject, credit, grade = input().split()
    if grade != 'P':
        total_grade_points += float(credit) * grade_points[grade]
        total_credits += float(credit)

if total_credits == 0:
    gpa = 0.0
else:
    gpa = total_grade_points / total_credits

print(f'{gpa:.6f}')
