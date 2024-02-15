class student:
    def open(self):
        print("School open")

class teacher:
    def open(self):
        print("Closed")
class school(teacher):
    def start(self):
        print("Hi students and teachers")

obj=school()
obj.open()






