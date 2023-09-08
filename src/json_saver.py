import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileSaver(ABC):
    __slots__ = '__filename'

    @abstractmethod
    def write_vacancy(self, vacancy_json):
        pass

    @abstractmethod
    def read_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self, id_vacancy):
        pass


class JSONSaver(FileSaver):
    def __init__(self, keyword: str):
        self.__filename = f'{keyword}.json'

    @property
    def filename(self):
        return self.__filename

    def write_vacancy(self, vacancy_json):
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(vacancy_json, file, indent=4,  ensure_ascii=False)

    def read_vacancy(self):
        with open(self.filename, "r", encoding='utf-8') as file:
            vacancy_json = json.load(file)

        return [Vacancy(data_dict) for data_dict in vacancy_json]

    def del_vacancy(self, id_vacancy):
        with open(self.filename, "r", encoding='utf-8') as file:
            vacancy_json = json.load(file)

            for item in vacancy_json:
                if item['id_vacancy'] == id_vacancy:
                    vacancy_json.remove(item)
                    break

            self.write_vacancy(vacancy_json)
