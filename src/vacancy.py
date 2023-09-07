class Vacancy:
    __slots__ = ('__name', '__url', '__description', '__salary')

    def __init__(self, name: str, url: str, description: str, salary: int):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.url}', {self.salary})"

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __eq__(self, other):
        return self.salary == other.salary
