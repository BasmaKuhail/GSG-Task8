class Student:
    # creating a constructor
    def __init__(self, name, age, city):
        self.marks = []
        self.name = name
        self.age = age
        self.city = city

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        for mark in self.marks:
            print(f"mark: {mark}")

    def Calc_average(self):
        sum = 0
        if len(self.marks) == 0:
            print("no marks!")
        for mark in self.marks:
            sum += mark

        return sum/len(self.marks)


