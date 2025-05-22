from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    @abstractmethod
    def get_course(self):
        pass

    @abstractmethod
    def get_name_list(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_year})"


class Maksym(Person):
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        super().__init__(first_name, last_name, birth_year)

    def get_course(self):
        if self.birth_year is None:
            return None
        age = 2025 - self.birth_year
        course = age - 17
        return min(max(course, 1), 4)

    def get_name_list(self):
        return [self.first_name, self.last_name]


class MaksymChild(Maksym):
    def __init__(self, first_name: str, last_name: str, birth_year: int,
                 email: str, phone: str, hobby: str):
        super().__init__(first_name, last_name, birth_year)
        self.email = email
        self.phone = phone
        self.hobby = hobby
        self.__status = None

    def get_full_info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_year": self.birth_year,
            "email": self.email,
            "phone": self.phone,
            "hobby": self.hobby,
            "course": self.get_course(),
            "status": self.get_student_status()
        }

    def get_student_status(self):
        age = self._calculate_age()
        course = self.get_course()

        if age is None or course is None:
            self.__status = "Недостатньо інформації"
        elif age < 18:
            self.__status = "Неповнолітній студент"
        elif course == 4:
            self.__status = "Випускний курс"
        else:
            self.__status = f"Студент {course} курсу"

        return self.__status

    def _calculate_age(self):
        if self.birth_year is None:
            return None
        return 2025 - self.birth_year

    def get_hobby_hashtag(self):
        return f"#{self.hobby.replace(' ', '').lower()}"

    def is_long_name(self):
        return len(self.first_name) > 6


maksym = Maksym("Максим", "Лебезун", 2008)
print(maksym.get_course())
print(maksym.get_name_list())
print(maksym)

student = MaksymChild("Максим", "Лебезун", 2008, "maksym@example.com", "+380123456789", "програмування")
print(student.get_course())
print(student.get_name_list())
print(student.get_full_info())
print(student.get_student_status())
print(student.get_hobby_hashtag())
print(student.is_long_name())
