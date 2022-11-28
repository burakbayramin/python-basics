def calc_grade(line):
    line = line[:-1]
    list = line.split(",")
    name = list[0]
    exam1 = int(list[1])
    exam2 = int(list[2])
    exam3 = int(list[3])
    grade = exam1 * (3/10) + exam2 * (3/10) + exam3 * (4/10)
    if(grade > 65):
        status = "PASS"
    else:
        status = "FAIL"
    return name, "--->", status, "\n"

with open("exams.txt", "r", encoding="utf-8") as file:
    grade_list = []
    
    for i in file:
        grade_list.append(calc_grade(i))
    
    with open("grades.txt", "w", encoding="utf-8") as file2:
        for i in grade_list:
            file2.write(i)