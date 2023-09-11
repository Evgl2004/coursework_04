from abc import ABC, abstractmethod
from src.err import ParsingError
from os import getenv

import requests


class API(ABC):
    """
    Абстрактный класс.
    Общие методы для всех потомков:
    1. Получить список вакансий с веб-портала по API
    2. Получить ответ на запрос к веб-порталу по API.
    3. Получить отформатированные данные в единой структуре.
    """
    __slots__ = ('__url_vacancies', '__vacancies_list', '__headers', '__params', '__name_parent_group_json')

    @abstractmethod
    def get_requests(self):
        """
        Получить ответ на запрос к веб-порталу по API.
        :return: Возвращает данные в формате JSON.
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        Получить список вакансий с веб-портала по API.
        Полученные данные хранятся в экземпляре классе.
        :return:
        """
        pass

    @abstractmethod
    def formatted_vacancy(self):
        """
        Получить отформатированные данные в единой структуре.
        :return: Возвращается словарь с данными представленными в заданной структуре хранения.
        """
        pass


class JobSearchPortalAPI(API):
    """
    Класс описывающий работу API веб-порталов.
    Общие методы и свойства.
    Имеет предопределенный перечень свойств, закрытых для пользовательского использования.
    """
    __slots__ = ('__url_vacancies', '__headers', '__params', '__vacancies_list', '__name_parent_group_json')

    def __init__(self, url_vacancies: str, headers: dict, params: dict, name_parent_group_json: str):
        """
        Метод инициализации экземпляров класса РаботаПоискаВебПорта из входящих данных.
        :param url_vacancies: Ссылка на API по поиску вакансий.
        :param headers: Заголовок с передаваемыми на портал параметрами.
        :param params: Параметры запроса.
        :param name_parent_group_json: Первый ключевой элемент возвращаемого JSON.
        """
        self.__url_vacancies = url_vacancies
        self.__headers = headers
        self.__params = params
        self.__vacancies_list = []
        self.__name_parent_group_json = name_parent_group_json

    @property
    def url_vacancies(self):
        return self.__url_vacancies

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    @property
    def vacancies_list(self):
        return self.__vacancies_list

    @property
    def name_parent_group_json(self):
        return self.__name_parent_group_json

    def __str__(self):
        """
        Переопределённое представление строкового значения экземпляра класса.
        :return: Строка с данными экземпляра класса.
        """
        return f'url_vacancies = {self.__url_vacancies}'

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__url_vacancies}', '{self.__params}', "
                f"'{self.__vacancies_list}', '{self.__name_parent_group_json}')")

    def get_requests(self):
        """
        Получить ответ на запрос к веб-порталу по API.
        :return: Возвращает данные в формате JSON.
        """

        # В запросе используем параметры, которые были получены при инициализации экземпляра класса
        response = requests.get(self.url_vacancies, headers=self.headers, params=self.params)

        # Если ошибки отсутствуют возвращаем данные в формате JSON.
        # Иначе возвращаем Исключение с описанием ошибки.
        if response.status_code == 200:
            return response.json()[self.name_parent_group_json]
        else:
            raise ParsingError(f"Ошибка получения данных по API. Код ошибки = {response.status_code}")

    def get_vacancies(self, pages_count=2):
        """
        Получить список вакансий с веб-портала по API.
        Полученные данные хранятся в экземпляре классе.
        :param pages_count: Количество запрашиваемых с веб-портала страниц.
        :return:
        """
        self.__vacancies_list = []

        # В запросе направляемом по API указываем количество страниц, которое хотим получить в ответ.
        # Затем обходим каждую страницу.
        for page_number in range(pages_count):
            self.__params['page'] = page_number

            # В обработчике исключений производим запрос через API к веб-порталу.
            # Если возникает Исключение обрабатываем.
            try:
                vacancies_page = self.get_requests()
            except ParsingError as error:
                print(error)
            else:
                self.__vacancies_list.extend(vacancies_page)

    def formatted_vacancy(self):
        """
        Получить отформатированные данные в единой структуре.
        :return: Возвращается словарь с данными представленными в заданной структуре хранения.
        """
        pass


class HeadHunterAPI(JobSearchPortalAPI):
    """
    Класс описывающий работу API веб-порталов HeadHunter.
    """
    def __init__(self, keyword: str, number_records: int):
        """
        Инициализация конкретными параметрами для работы API с веб-порталом HeadHunter.
        :param keyword: Одно ключевое слова для запроса.
        :param number_records: Количество записей запрашиваемых с веб-портала.
        """
        url_vacancies = 'https://api.hh.ru/vacancies'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {getenv("API_KEY_HH")}'
        }

        params = {
            'per_page': number_records//2,
            'page': 1,
            'text': keyword,
            'only_with_salary': True,
            'currency': 'RUR'
        }
        super().__init__(url_vacancies, headers, params, "items")

    def formatted_vacancy(self):
        """
        Получить отформатированные данные в единой структуре.
        :return: Возвращается словарь с данными представленными в заданной структуре хранения.
        """

        formatted_vacancy_list = []

        for vacancy in self.vacancies_list:
            formatted_vacancy_dict = {
                'api': 'HeadHunter',
                'id_vacancy': vacancy['id'],
                'employer': vacancy['employer']['name'] if vacancy["employer"] is not None else "",
                'title': vacancy['name'],
                'url': vacancy['alternate_url'],
                'salary_from': vacancy["salary"]['from'] if vacancy["salary"] is not None
                                                            and vacancy["salary"]['from'] is not None else 0,
                'salary_to': vacancy["salary"]['to'] if vacancy["salary"] is not None
                                                        and vacancy["salary"]['to'] is not None else 0
            }

            formatted_vacancy_list.append(formatted_vacancy_dict)

        return formatted_vacancy_list


class SuperJobAPI(JobSearchPortalAPI):
    """
    Класс описывающий работу API веб-порталов HeadHunter.
    """
    def __init__(self, keyword: str, number_records: int):
        """
        Инициализация конкретными параметрами для работы API с веб-порталом SuperJob.
        :param keyword: Одно ключевое слова для запроса.
        :param number_records: Количество записей запрашиваемых с веб-портала.
        """
        url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
        headers = {
            'X-Api-App-Id': getenv('API_KEY_SUPERJOB')
        }

        params = {
            'count': number_records//2,
            'page': 1,
            'keyword': keyword,
            'archived': False
        }
        super().__init__(url_vacancies, headers, params, "objects")

    def formatted_vacancy(self):
        """
        Получить отформатированные данные в единой структуре.
        :return: Возвращается словарь с данными представленными в заданной структуре хранения.
        """

        formatted_vacancy_list = []

        for vacancy in self.vacancies_list:
            formatted_vacancy_dict = {
                'api': 'SuperJob',
                'id_vacancy': vacancy['id'],
                'employer': vacancy['firm_name'],
                'title': vacancy['profession'],
                'url': vacancy['link'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to']
            }

            formatted_vacancy_list.append(formatted_vacancy_dict)

        return formatted_vacancy_list
