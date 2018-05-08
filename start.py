# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print(self.name, self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print()
lisa.print()
