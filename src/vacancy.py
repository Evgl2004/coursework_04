class Vacancy:
    __slots__ = ('__api', '__id_vacancy', '__employer', '__title', '__url', '__salary_from', '__salary_to')

    def __init__(self, data_dict: dict):
        self.__api = data_dict['api']
        self.__id_vacancy = data_dict['id_vacancy']
        self.__employer = data_dict['employer']
        self.__title = data_dict['title']
        self.__url = data_dict['url']
        self.__salary_from = data_dict['salary_from']
        self.__salary_to = data_dict['salary_to']

    @property
    def api(self):
        return self.__api

    @property
    def id_vacancy(self):
        return self.__id_vacancy

    @property
    def employer(self):
        return self.__employer

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', '{self.url}', {self.salary_from})"

    # def __gt__(self, other):
    #     return self.salary > other.salary
    #
    # def __ge__(self, other):
    #     return self.salary >= other.salary
    #
    # def __lt__(self, other):
    #     return self.salary < other.salary
    #
    # def __le__(self, other):
    #     return self.salary <= other.salary
    #
    # def __eq__(self, other):
    #     return self.salary == other.salary
