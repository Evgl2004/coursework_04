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

    def return_dict(self):
        return {
            'api': self.__api,
            'id_vacancy': self.__id_vacancy,
            'employer': self.__employer,
            'title': self.__title,
            'url': self.__url,
            'salary_from': self.__salary_from,
            'salary_to': self.__salary_to
        }

    def __str__(self):
        return (f'ID = {self.id_vacancy}\n'
                f'Вакансия = {self.title}\n'
                f'Работодатель = {self.employer}\n'
                f'Зарплата = {self.salary_from}\n'
                f'Ссылка = {self.url}\n')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', '{self.url}', {self.salary_from})"

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from > other.salary_from
        else:
            return self.salary_from > other

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from >= other.salary_from
        else:
            return self.salary_from >= other

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from < other.salary_from
        else:
            return self.salary_from < other

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from <= other.salary_from
        else:
            return self.salary_from <= other

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from == other.salary_from
        else:
            return self.salary_from == other
