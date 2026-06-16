class student:
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