class Student:
    def __init__(self,student_id,name,age,marks):
        self.id=student_id
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("\nStudent ID     :",self.id)
        print("Name     :",self.name)
        print("AGE      :",self.age)
        print("Marks    :",self.marks)

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        id=int(input("Enter student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks =float(input("Enter Marks: "))

        student =Student(id, name, age, marks)
        self.students.append(student)
        print("Student Added Successfully !")
    
    def view_students(self):
        if len(self.students) ==0:
            print("No Students Found")
        else:
            for i in self.students:
                i.display()
    