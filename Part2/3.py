from typing import Dict, List
from enum import Enum

class Subject(Enum):
    """
    This class contains school subjects as enums for class Student
    There are four subjects: math, english, biology and litereture.
    """
    Math = "Math"
    English = "English"
    Biology = "Biology"
    Litereture = "Litereture"

class Student:
    """
    This class describes student.
    Single instance contains name, surname, record book number and grades of student.
    Grades is a dictionary that has a Subject as key and a list of ints as value.
    """
    def __init__(self, name: str, surname: str, record_book: int, grades: Dict[Subject, List[int]] = {}):
        self._name = name
        self._surname = surname
        self._record_book = record_book
        self._grades = grades

    def get_full_name(self) -> str:
        return f"{self._name} {self._surname}"

    def get_record_book(self) -> int:
        return self._record_book

    def get_grades(self) -> Dict[Subject, List[int]]:
        return self._grades.copy()

    def add_grade(self, subject: Subject, grade: int):
        if grade < 1 or grade > 12:
            raise ValueError("grade can not be less than 1 and more than 12")

        try:
            self._grades[subject].append(grade)
        except KeyError:
            self._grades[subject] = [grade]

    def everage_grade(self, subject: Subject) -> float:
        grades = self._grades[subject]

        summ = 0
        for grade in grades:
            summ += grade

        return summ / len(grades)

    def average_score(self):
        summ = 0

        for key in self._grades:
            summ += self.everage_grade(key)

        return summ / len(self._grades)


class Group:
    """
    This class describes school group.
    Single instance containes not more than 20 students.
    """
    def __init__(self, group_name: str):
        self._name = group_name
        self._group: Dict[str, Student] = {}
        self._num_of_students = 0

    MAX_NUM_OF_STUDENTS = 20

    def get_group_name(self):
        return self._name

    def add_student(self, student: Student):
        key = student.get_full_name()

        if key in self._group:
            raise ValueError(f"Student {key} is already in group {self._name}")

        if self._num_of_students == Group.MAX_NUM_OF_STUDENTS:
            raise RuntimeError(f"Can not add strudent {key} in group {self._name}: in this group already {self._num_of_students} students")

        self._group[key] = student
        self._num_of_students += 1

    def students_with_scores(self) -> Dict[Student, int]:
        student_score: Dict[Student, int] = {}

        for student in self._group.values():
            student_score[student] = student.average_score()

        return dict(sorted(student_score.items(), key=lambda item: item[1], reverse=True))

    def five_best_students(self) -> List[Student]:
        students_score_sorted = self.students_with_scores()

        # response = dict(list(students_score_sorted)[:5])
        response = list(students_score_sorted.keys())[:5]
        return response


students = [
    Student(
        "Ivan",
        "Budko",
        12345678,
        {
            Subject.Math: [10, 8, 9, 11, 8],
            Subject.Biology: [8, 7, 9, 7, 7],
            Subject.English: [5, 7, 7, 5, 6]
        }
    ),
    Student(
        "Mary",
        "Vidonsk",
        1235215,
        {
            Subject.Math: [8, 9, 12, 11],
            Subject.Biology: [8, 8, 8, 8],
            Subject.Litereture: [11, 12, 11, 8]
        }
    ),
    Student(
        "Egor",
        "Krut",
        1235123,
        {
            Subject.Math: [4, 5, 4, 4],
            Subject.Biology: [5, 5, 6, 8],
            Subject.Litereture: [7, 8, 11, 9]

        }
    ),
    Student(
        "Oleg",
        "Tarelov",
        54521453,
        {
            Subject.Math: [6,2,6,2],
            Subject.Biology: [8, 9, 2, 4],
            Subject.Litereture: [8, 2, 6, 1]

        }
    ),
    Student(
        "Ivan",
        "Hudoi",
        27912823,
        {
            Subject.Math: [9, 8, 5, 5],
            Subject.Biology: [6, 2, 6, 4],
            Subject.Litereture: [9, 9, 9, 9]

        }
    ),
    Student(
        "Vitalii",
        "Hudoi",
        8902801,
        {
            Subject.Math: [8, 8, 11, 12],
            Subject.Biology: [9, 9 ,10, 12],
            Subject.Litereture: [10, 10 ,11, 12]

        }
    )
]

group = Group("1A")

for student in students:
    group.add_student(student)

best_students = group.five_best_students()

for student in best_students:
    print(student.get_full_name())







