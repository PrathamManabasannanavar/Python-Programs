class Student:    
    def __init__(self, name, rollno, passed, cgpa):
        self.name = name
        self.rollno = rollno
        self.passed = passed
        self.cgpa = cgpa

    def getDetails(self):
        print(self.name)
        print(self.rollno)
        print(self.passed)
        print(self.cgpa)


st = Student("Rahul", 23, True, 9.99)
st.getDetails()