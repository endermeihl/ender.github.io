# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score, name2):
        self.__name = name
        self.__score = score
        self._Student__name = name2

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_score(self, score):
        self.__score = score

    def get_name(self):
        return self.__name


lisa = Student('Lisa', 99,'e')
bart = Student('Bart', 59, 't')
print(lisa._Student__name, lisa.get_name())
print(bart._Student__name, bart.get_name())