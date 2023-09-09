class Vacancy:
    """
    Класс Вакансии.
    Имеет предопределенный перечень свойств, закрытых для пользовательского использования.
    """
    __slots__ = ('__api', '__id_vacancy', '__employer', '__title', '__url', '__salary_from', '__salary_to')

    def __init__(self, data_dict: dict):
        """
        Метод инициализации экземпляров класса Вакансии из данных полученных во входящего словаре.
        :param data_dict: Словарь, из него берём данные для инициализации.
        """
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
        """
        Так как класс имеет жестко определённый перечень свойств, типовой метод получения словаря не действует.
        Получаем тип данных словарь из значений свойств экземпляра класса.
        :return: Возвращаем словарь с данными экземпляра класса Вакансии.
        """
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
        """
        Переопределённое представление строкового значения экземпляра класса Вакансии.
        :return: Строка с данными экземпляра класса Вакансии.
        """
        return (f'ID = {self.__id_vacancy}\n'
                f'Вакансия = {self.__title}\n'
                f'Работодатель = {self.__employer}\n'
                f'Зарплата = {self.__salary_from}\n'
                f'Ссылка = {self.__url}\n')

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__api}', '{self.__id_vacancy}', '{self.__employer}', "
                f"'{self.__title}', '{self.__url}', '{self.__salary_from}', '{self.__salary_to}')")

    def __gt__(self, other):
        """
        Переопределённое метод сравнения экземпляров класса Вакансии.
        :param other: Объект с которым происходит сравнение.
        :return: Результат сравнения Истина/Ложь.
        """
        if isinstance(other, self.__class__):
            return self.salary_from > other.salary_from
        else:
            return self.salary_from > other

    def __ge__(self, other):
        """
        Переопределённое метод сравнения экземпляров класса Вакансии.
        :param other: Объект с которым происходит сравнение.
        :return: Результат сравнения Истина/Ложь.
        """
        if isinstance(other, self.__class__):
            return self.salary_from >= other.salary_from
        else:
            return self.salary_from >= other

    def __lt__(self, other):
        """
        Переопределённое метод сравнения экземпляров класса Вакансии.
        :param other: Объект с которым происходит сравнение.
        :return: Результат сравнения Истина/Ложь.
        """
        if isinstance(other, self.__class__):
            return self.salary_from < other.salary_from
        else:
            return self.salary_from < other

    def __le__(self, other):
        """
        Переопределённое метод сравнения экземпляров класса Вакансии.
        :param other: Объект с которым происходит сравнение.
        :return: Результат сравнения Истина/Ложь.
        """
        if isinstance(other, self.__class__):
            return self.salary_from <= other.salary_from
        else:
            return self.salary_from <= other

    def __eq__(self, other):
        """
        Переопределённое метод сравнения экземпляров класса Вакансии.
        :param other: Объект с которым происходит сравнение.
        :return: Результат сравнения Истина/Ложь.
        """
        if isinstance(other, self.__class__):
            return self.salary_from == other.salary_from
        else:
            return self.salary_from == other
