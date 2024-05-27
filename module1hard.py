def calculate_average_grades(grades, students):
    students_list = list(students)
    student_grades = {}
    for student in students_list:
        student_index = students_list.index(student)
        student_scores = grades[student_index]
        average_grade = sum(student_scores) / len(student_scores)
        student_grades[student] = average_grade
    return student_grades
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(calculate_average_grades(grades, students))