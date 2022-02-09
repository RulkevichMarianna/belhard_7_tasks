"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname: str, name: str, group: int, average_score: float):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __repr__(self):
        return f'<Student {self.average_score}>'


student_1 = Student("Иванов", "Иван", 1, 7.4)
student_2 = Student("Петров", "Петр", 3, 4.8)
student_3 = Student("Сидоров", "Семен", 1, 5.5)
student_4 = Student("Зуй", "Евгений", 2, 8.0)
student_5 = Student("Струков", "Дмитрий", 2, 6.4)

student_list = [student_1, student_2, student_3, student_4, student_5]

print(sorted(student_list))
print(sorted(student_list, reverse=True))
