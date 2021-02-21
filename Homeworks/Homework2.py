studentsInfo = {}
for s in range(1, 6):
    name = input(str(s)+". Öğrencinin Adını Giriniz: ")
    surname = input(str(s)+". Öğrencinin Soyadını Giriniz: ")
    midterm = int(input(str(s)+". Öğrencinin Vize Notunu Giriniz: "))
    final = int(input(str(s) + ". Öğrencinin Final Notunu Giriniz: "))
    homework = int(input(str(s) + ". Öğrencinin Ödev Notunu Giriniz: "))
    studentNames = []
    studentGrades = []
    student = []
    total = 0
    studentNames.append(name)
    studentNames.append(surname)
    studentGrades.append(midterm)
    studentGrades.append(final)
    studentGrades.append(homework)
    student.append(studentNames)
    student.append(studentGrades)
    for g in studentGrades:
        total = total+g
    total = total/3
    student.append(total)
    studentsInfo[s] = student
temp = []
for i in range(1, 6):
    for j in range(1, 6):
        if studentsInfo[i][2] > studentsInfo[j][2]:
            studentsInfo[i], studentsInfo[j] = studentsInfo[j], studentsInfo[i]

print(studentsInfo[1][0][0], studentsInfo[1][0][1], "Tebrikler! Ortalamanız:", studentsInfo[1][2])






