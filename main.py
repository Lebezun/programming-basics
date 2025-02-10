class Maksym:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name if first_name is not None else None
        self.last_name = last_name if last_name is not None else None
        self.birth_year = birth_year if birth_year is not None else None

    def get_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        start_year = 2023
        course = current_year - start_year
        return min(course, 4)  

    def get_name_list(self):
        return [self.first_name, self.last_name]


maksym = Maksym("Максим", "Лебезун", 2008)

print(maksym.get_course())
print(maksym.get_name_list())