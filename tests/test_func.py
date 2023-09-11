import pytest
import uteils.func as func
from src.vacancy import Vacancy


def test_sort_by_salary_from():
    assert func.sort_by_salary_from([6, 3, 1]) == [1, 3, 6]
    assert func.sort_by_salary_from([4, 13, 31, 1]) == [1, 4, 13, 31]


def test_vacancy_object_to_dict():
    vacancy_dict = {
        "api": "SuperJob",
        "id_vacancy": 38140998,
        "employer": "ГБОУ \"Лицей №126\" Калининского района Санкт-Петербурга",
        "title": "Методист по программированию на Python (в центр цифрового образования)",
        "url": "https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html",
        "salary_from": 30000,
        "salary_to": 0
    }
    test_vacancy = [Vacancy(vacancy_dict)]

    assert func.vacancy_object_to_dict(test_vacancy) == [vacancy_dict]
