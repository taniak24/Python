class Student:
    
    def __init__(self, name, major, grade):
        self.name = name
        self.major = major
        self.grade = grade

    def passed_test(self):
        if self.grade >= 4.50:
            return True
        else:
            return False