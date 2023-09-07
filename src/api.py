from abc import ABC, abstractmethod

from src.vacancy import Vacancy
from src.err import ParsingError
from os import getenv

import requests


class API(ABC):
    __slots__ = ('__url_vacancies', '__vacancies_list', '__headers', '__params')

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_requests(self):
        pass


class JobSearchPortalAPI(API):
    def __init__(self, url_vacancies: str, headers: dict, params: dict):
        self.__url_vacancies = url_vacancies
        self.__headers = headers
        self.__params = params
        self.__vacancies_list = []

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

    def get_requests(self):

        response = requests.get(self.url_vacancies, headers=self.headers, params=self.params)

        if response.status_code == 200:
            return response.json()["items"]
        else:
            raise ParsingError(f"Ошибка получения данных по API. Код ошибки = {response.status_code}")

    def get_vacancies(self, pages_count=2):

        self.__vacancies_list = []

        for page_number in range(pages_count):
            self.__params['page'] = page_number

            try:
                vacancies_page = self.get_requests()
            except ParsingError as error:
                print(error)
            else:
                self.__vacancies_list.extend(vacancies_page)


class HeadHunterAPI(JobSearchPortalAPI):
    def __init__(self, keyword: str):
        url_vacancies = 'https://api.hh.ru/vacancies'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer APPLL5M4FRR13V89VQ85UBT1BIRQA2GIF5AOLI15IE1D1L872PFNQFN0VN99LNA1'
        }

        params = {
            'per_page': 20,
            'page': 1,
            'text': keyword,
            'archived': False
        }
        super().__init__(url_vacancies, headers, params)


class SuperJobAPI(JobSearchPortalAPI):
    def __init__(self, keyword: str):
        url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
        headers = {
            'X-Api-App-Id': getenv('API_KEY_SUPERJOB')
        }

        params = {
            'count': 20,
            'page': 1,
            'keyword': keyword,
            'archived': False
        }
        super().__init__(url_vacancies, headers, params)
