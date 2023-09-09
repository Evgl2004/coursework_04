import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileSaver(ABC):
    """
    Абстрактный класс.
    Общие методы для всех потомков:
    1. Записать полученный список всех вакансий в файл.
    2. Считать из файла все вакансии и преобразовать их в экземпляры класса Вакансии.
    3. Удалить найденную вакансию в файле по номеру идентификатора.
    """
    __slots__ = '__filename'

    @abstractmethod
    def write_vacancy(self, vacancy_json):
        """
        Записать полученный список всех вакансий в файл.
        :param vacancy_json: Список вакансий в формате JSON.
        :return:
        """
        pass

    @abstractmethod
    def read_vacancy(self):
        """
        Считать из файла все вакансии и преобразовать их в экземпляры класса Вакансии.
        :return: Возвращает список экземпляров класса Вакансии.
        """

        pass

    @abstractmethod
    def del_vacancy(self, id_vacancy):
        """
        Удалить найденную вакансию в файле по номеру идентификатора.
        :param id_vacancy: Идентификатор вакансии, которую нужно удалить.
        :return: Возвращает данные в формате JSON.
        """
        pass


class JSONSaver(FileSaver):
    """
    Класс для работы с файлом формата JSON
    """
    def __init__(self, keyword: str):
        """
        Инициализация экземпляра класса.
        :param keyword: Ключевое слово, по которому задано имя файла.
        """
        self.__filename = f'{keyword}.json'

    @property
    def filename(self):
        return self.__filename

    def __str__(self):
        """
        Переопределённое представление строкового значения экземпляра класса.
        :return: Строка с данными экземпляра класса.
        """
        return f'filename = {self.__filename}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__filename}')"

    def write_vacancy(self, vacancy_json):
        """
        Записать полученный список всех вакансий в файл.
        :param vacancy_json: Список вакансий в формате JSON.
        :return:
        """
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(vacancy_json, file, indent=4,  ensure_ascii=False)

    def read_vacancy(self):
        """
        Считать из файла все вакансии и преобразовать их в экземпляры класса Вакансии.
        :return: Возвращает список экземпляров класса Вакансии.
        """
        with open(self.filename, "r", encoding='utf-8') as file:
            vacancy_json = json.load(file)

        return [Vacancy(data_dict) for data_dict in vacancy_json]

    def del_vacancy(self, id_vacancy):
        """
        Удаляет найденную вакансию в файле по номеру идентификатора.
        :param id_vacancy: Идентификатор вакансии, которую нужно удалить.
        :return: Возвращает данные в формате JSON.
        """
        with open(self.filename, "r", encoding='utf-8') as file:
            vacancy_json = json.load(file)

            for item in vacancy_json:
                if item['id_vacancy'] == id_vacancy:
                    vacancy_json.remove(item)
                    break

            return vacancy_json
