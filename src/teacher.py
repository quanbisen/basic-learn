from src.people import People


class Teacher(People):

    def __init__(self, name, sex):
        super().__init__(name, sex)

    def teach(self):
        print("My name is " + self.name + "." + "I'm teaching Math now.")
