import pytest
from os import getenv
from src.api import JobSearchPortalAPI, HeadHunterAPI, SuperJobAPI
from src.err import ParsingError


@pytest.fixture
def call_test_portal_api():
    url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
    headers = {
        'X-Api-App-Id': getenv('API_KEY_SUPERJOB')
    }

    params = {
        'count': 1,
        'page': 1,
        'keyword': "Python",
        'archived': False
    }
    return JobSearchPortalAPI(url_vacancies, headers, params, "objects")


def test_portal_api_init(call_test_portal_api):
    assert call_test_portal_api.url_vacancies == "https://api.superjob.ru/2.0/vacancies"
    assert call_test_portal_api.params["keyword"] == "Python"
    assert call_test_portal_api.name_parent_group_json == "objects"
    assert call_test_portal_api.vacancies_list == []


def test_portal_api_access_properties(call_test_portal_api):
    with pytest.raises(AttributeError):
        print(call_test_portal_api.__url_vacancies)

    with pytest.raises(AttributeError):
        print(call_test_portal_api.__headers)

    with pytest.raises(AttributeError):
        print(call_test_portal_api.__params)

    with pytest.raises(AttributeError):
        print(call_test_portal_api.__name_parent_group_json)

    with pytest.raises(AttributeError):
        print(call_test_portal_api.__vacancies_list)


def test_portal_api_property_setting(call_test_portal_api):
    with pytest.raises(AttributeError):
        call_test_portal_api.url_vacancies = "test"

    with pytest.raises(AttributeError):
        call_test_portal_api.headers = "test"

    with pytest.raises(AttributeError):
        call_test_portal_api.params = "test"

    with pytest.raises(AttributeError):
        call_test_portal_api.name_parent_group_json = "test"

    with pytest.raises(AttributeError):
        call_test_portal_api.vacancies_list = "test"


def test_portal_api_str(call_test_portal_api):
    assert str(call_test_portal_api) == "url_vacancies = https://api.superjob.ru/2.0/vacancies"


def test_portal_api_repr(call_test_portal_api):
    assert call_test_portal_api.__repr__() == ("JobSearchPortalAPI('https://api.superjob.ru/2.0/vacancies', "
                                               "'{'count': 1, 'page': 1, 'keyword': 'Python', 'archived': False}', "
                                               "'[]', 'objects')")


def test_portal_api_get_requests(call_test_portal_api):
    answer = call_test_portal_api.get_requests()

    assert isinstance(answer, list)
    assert len(answer) == 1
    assert isinstance(answer[0], dict)
    assert 'id' in answer[0]
    assert isinstance(answer[0]['id'], int)


def test_portal_api_get_requests_err():
    url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
    test_portal_api = JobSearchPortalAPI(url_vacancies, {}, {'salary': 'qwe'}, "items")

    with pytest.raises(ParsingError):
        test_portal_api.get_requests()


def test_portal_api_get_vacancies(call_test_portal_api):
    call_test_portal_api.get_vacancies(1)

    answer_get_vacancies = call_test_portal_api.vacancies_list

    assert isinstance(answer_get_vacancies, list)
    assert len(answer_get_vacancies) == 1
    assert isinstance(answer_get_vacancies[0], dict)
    assert 'id' in answer_get_vacancies[0]
    assert isinstance(answer_get_vacancies[0]['id'], int)


def test_portal_api_get_vacancies_err(call_test_portal_api):
    url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
    test_portal_api = JobSearchPortalAPI(url_vacancies, {}, {'salary': 'qwe'}, "items")

    assert (test_portal_api.get_vacancies(1)) == print("Ошибка получения данных по API. Код ошибки = 403")


def test_hh_api_init():
    hh_api = HeadHunterAPI("python", 2)
    assert hh_api.url_vacancies == "https://api.hh.ru/vacancies"
    assert hh_api.params["text"] == "python"
    assert hh_api.name_parent_group_json == "items"
    assert hh_api.vacancies_list == []


def test_hh_api_formatted_vacancy():
    hh_api = HeadHunterAPI("python", 2)
    hh_api.get_vacancies(1)
    formatted_vacancy_list = hh_api.formatted_vacancy()

    assert isinstance(formatted_vacancy_list, list)
    assert len(formatted_vacancy_list) == 1
    assert isinstance(formatted_vacancy_list[0], dict)
    assert 'id_vacancy' in formatted_vacancy_list[0]
    assert isinstance(formatted_vacancy_list[0]['id_vacancy'], str)
    assert 'api' in formatted_vacancy_list[0]
    assert formatted_vacancy_list[0]['api'] == "HeadHunter"


def test_sj_api_init():
    sj_api = SuperJobAPI("python", 2)
    assert sj_api.url_vacancies == "https://api.superjob.ru/2.0/vacancies"
    assert sj_api.params["keyword"] == "python"
    assert sj_api.name_parent_group_json == "objects"
    assert sj_api.vacancies_list == []


def test_sj_api_formatted_vacancy():
    sj_api = SuperJobAPI("python", 2)
    sj_api.get_vacancies(1)
    formatted_vacancy_list = sj_api.formatted_vacancy()

    assert isinstance(formatted_vacancy_list, list)
    assert len(formatted_vacancy_list) == 1
    assert isinstance(formatted_vacancy_list[0], dict)
    assert 'id_vacancy' in formatted_vacancy_list[0]
    assert isinstance(formatted_vacancy_list[0]['id_vacancy'], int)
    assert 'api' in formatted_vacancy_list[0]
    assert formatted_vacancy_list[0]['api'] == "SuperJob"
