class Maksym:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_course(self):
        if self.birth_year is None:
            return None
        return min(2025 - 2023, 4)

    def get_name_list(self):
        return [self.first_name, self.last_name]


class MaksymChild(Maksym):
    def __init__(self, first_name=None, last_name=None, birth_year=None, email=None, phone=None, hobby=None):
        super().__init__(first_name, last_name, birth_year)
        self.email = email
        self.phone = phone
        self.hobby = hobby

    def get_full_info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_year": self.birth_year,
            "email": self.email,
            "phone": self.phone,
            "hobby": self.hobby,
            "course": self.get_course()
        }

    def _calculate_age(self):
        if self.birth_year is None:
            return None
        return 2025 - self.birth_year

    def get_student_status(self):
        age = self._calculate_age()
        course = self.get_course()

        if age is None or course is None:
            return "Недостатньо інформації"

        if age < 18:
            return "Неповнолітній студент"
        elif course == 4:
            return "Випускний курс"
        return f"Студент {course} курсу"


maksym = Maksym("Максим", "Лебезун", 2008)
print(maksym.get_course())
print(maksym.get_name_list())

student = MaksymChild("Максим", "Лебезун", 2008, "maksym@example.com", "+380123456789", "програмування")
print(student.get_course())
print(student.get_name_list())
print(student.get_full_info())
print(student.get_student_status())