def mean(list: list) -> float:
    total = 0
    for i in range(len(list)):
        total += list[i]
        i+=1
    return total / len(list)
    
def main():
    while True:

        print("Welcome to the average class grades calculator!")
        student_count = int(input("Enter the number of students within your class: "))
        students = []
        grades = []
        student_grades = {}

        for i in range(student_count):
            name = input(f"Enter Student's Name {i+1}: ")
            students.append(name)
            i+=1

        print("Enter grades for each student. (Keep grades in percent form: i.e. 85, not 0.85)")

        for i in range(student_count):
            grade = float(input(f"Enter grade for {students[i]}: "))
            grades.append(grade)
            i+=1

        for i in range(student_count):
            student_grades.update({students[i]: grades[i]})

        print(student_grades)

        conf = int(input("Is the following information correct? 1: Yes, 2: No"))

        if conf == 1:
            print(f"The class average grade is approximately {mean(grades)}%")
            break
            
        elif conf == 2:
            print("Reloading program...")
            continue
        else:
            print(f"Invalid Response: {conf}, program killed.")
            continue 

main()
