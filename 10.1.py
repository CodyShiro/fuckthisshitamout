class Student:
    def __init__(self, ten, math, physics, chem ):
        self.ten = ten
        self.math = math
        self.physics = physics
        self.chem = chem

    def print_finalscore(self):
        final_score = (self.math + self.physics + self.chem) / 3
        final_score = round(final_score, 2)
        print("The average mark of {} is {}".format(self.ten, final_score))

if __name__ == "__main__":
    student = Student("Jelly", 8.54, 9.32, 7.32)
    student.print_finalscore()
