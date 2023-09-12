import pytest
from src.api import SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
import os.path


@pytest.fixture
def call_test_json_saver():
    return JSONSaver('Test')


def test_json_saver_init(call_test_json_saver):
    assert call_test_json_saver.filename == "Test.json"


def test_json_saver_access_properties(call_test_json_saver):
    with pytest.raises(AttributeError):
        print(call_test_json_saver.__filename)


def test_json_saver_property_setting(call_test_json_saver):
    with pytest.raises(AttributeError):
        call_test_json_saver.filename = "test"


def test_json_saver_str(call_test_json_saver):
    assert str(call_test_json_saver) == "filename = Test.json"


def test_json_saver_repr(call_test_json_saver):
    assert call_test_json_saver.__repr__() == "JSONSaver('Test.json')"


def test_json_saver_write_vacancy(call_test_json_saver):
    sj_api = SuperJobAPI("python", 2)
    sj_api.get_vacancies(1)
    call_test_json_saver.write_vacancy(sj_api.formatted_vacancy())

    assert os.path.exists(call_test_json_saver.filename) == True


def test_json_saver_read_vacancy(call_test_json_saver):
    sj_api = SuperJobAPI("python", 2)
    sj_api.get_vacancies(1)
    call_test_json_saver.write_vacancy(sj_api.formatted_vacancy())

    vacancies_list = call_test_json_saver.read_vacancy()

    assert isinstance(vacancies_list, list)
    assert isinstance(vacancies_list[0], Vacancy)
    assert vacancies_list[0].api == "SuperJob"


def test_json_saver_del_vacancy(call_test_json_saver):
    vacancy_json = call_test_json_saver.del_vacancy(38140998)

    result_test = True

    for item in vacancy_json:
        if item['id_vacancy'] == 38140998:
            result_test = False
            break

    assert result_test == True


def test_json_saver_filter_vacancy(call_test_json_saver):
    vacancy_json = call_test_json_saver.filter_vacancy(['Лицей'])

    result_test = True

    for item in vacancy_json:
        if 'Лицей' in item['employer']:
            result_test = False
            break

    assert result_test == True
