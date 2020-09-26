class student:
    def __init__(self,student_id,marks,age):
        self.student_id = student_id
        self.marks = marks
        self.age = age

    def set_student_mark(self, mark):
        self.mark = mark

    def set_student_age(self, age):
        self.age = age

    def get_student_id(self):
        return self.student_id

    def get_student_mark(self):
        return self.mark

    def get_student_age(self):
        return self.age

    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return "Eligible"
        else:
            return "Not Eligible"
    
    def validate_age(self):
        if self.age>20:
            return "Eligible"
        else:
            return "Not Eligible"
    
    def check_qualification(self):
        if self.age>20 and (self.marks>=0 and self.age<=100) :
            if self.marks>=65:
                return "Eligible"
            else :
                return "Not Eligible"
        else:
            return "Not Eligible"

roll = int(input("Enter Id: "))
mark = int(input("Enter mark: "))
age = int(input("Enter age: "))
obj = student(roll,mark,age)
print("Mark: "+obj.validate_marks())
print("Age: "+obj.validate_age())
print("Qualification: "+obj.check_qualification())
