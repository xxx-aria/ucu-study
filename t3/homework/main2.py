prog_grade = int(input())
calc_grade = int(input())
disc_grade = int(input())
problem_grade = int(input())
hist_grade = int(input())

for grade in (prog_grade, calc_grade, disc_grade, problem_grade, hist_grade):
    if not 0 <= grade <= 100:
        print('None')
        break
else:
    total_grade = prog_grade + calc_grade + disc_grade + problem_grade + hist_grade
    percent_grade = round( total_grade / 5, 1)

    match percent_grade:
        case value if value >= 90:
            letter_grade = 'A'
        case value if value >= 80:
            letter_grade = 'B'
        case value if value >= 75:
            letter_grade = 'C'
        case value if value >= 65:
            letter_grade = 'D'
        case value if value >= 60:
            letter_grade = 'E'
        case _:
            letter_grade = 'F'

    print(f'Average grade = {percent_grade:.1f} -> {letter_grade}')
