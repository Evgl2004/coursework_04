import pytest
from src.vacancy import Vacancy


@pytest.fixture
def call_test_vacancy():
    return Vacancy({
        "api": "SuperJob",
        "id_vacancy": 38140998,
        "employer": "ГБОУ \"Лицей №126\" Калининского района Санкт-Петербурга",
        "title": "Методист по программированию на Python (в центр цифрового образования)",
        "url": "https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html",
        "salary_from": 30000,
        "salary_to": 0
    })

@pytest.fixture
def call_test_vacancy_any():
    return Vacancy({
        "api": "SuperJob",
        "id_vacancy": 46804114,
        "employer": "Ozon",
        "title": "Сборщик-упаковщик заказов (г. Тюмень)",
        "url": "https://tyumen.superjob.ru/vakansii/sborschik-upakovschik-zakazov-46804114.html",
        "salary_from": 55000,
        "salary_to": 0
    })

def test_vacancy_init(call_test_vacancy):
    assert call_test_vacancy.api == "SuperJob"
    assert call_test_vacancy.id_vacancy == 38140998
    assert call_test_vacancy.employer == "ГБОУ \"Лицей №126\" Калининского района Санкт-Петербурга"
    assert call_test_vacancy.title == "Методист по программированию на Python (в центр цифрового образования)"
    assert call_test_vacancy.url == "https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html"
    assert call_test_vacancy.salary_from == 30000
    assert call_test_vacancy.salary_to == 0


def test_vacancy_access_properties(call_test_vacancy):
    with pytest.raises(AttributeError):
        print(call_test_vacancy.__api)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__id_vacancy)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__employer)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__title)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__url)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__salary_from)

    with pytest.raises(AttributeError):
        print(call_test_vacancy.__salary_to)


def test_vacancy_property_setting(call_test_vacancy):
    with pytest.raises(AttributeError):
        call_test_vacancy.api = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.id_vacancy = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.employer = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.title = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.url = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.salary_from = "test"

    with pytest.raises(AttributeError):
        call_test_vacancy.salary_to = "test"


def test_vacancy_str(call_test_vacancy):
    assert str(call_test_vacancy) == ('ID = 38140998\n'
                                      'Вакансия = Методист по программированию на Python (в центр цифрового образования)\n'
                                      'Работодатель = ГБОУ "Лицей №126" Калининского района Санкт-Петербурга\n'
                                      'Зарплата = 30000\n'
                                      'Ссылка = https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html\n')


def test_vacancy_repr(call_test_vacancy):
    assert call_test_vacancy.__repr__() == ("Vacancy('SuperJob', '38140998', "
                                               "'ГБОУ \"Лицей №126\" Калининского района Санкт-Петербурга', "
                                               "'Методист по программированию на Python (в центр цифрового образования)', "
                                               "'https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html', "
                                               "'30000', '0')")


def test_vacancy_return_dict(call_test_vacancy):
    vacancy_dict = {
        "api": "SuperJob",
        "id_vacancy": 38140998,
        "employer": "ГБОУ \"Лицей №126\" Калининского района Санкт-Петербурга",
        "title": "Методист по программированию на Python (в центр цифрового образования)",
        "url": "https://spb.superjob.ru/vakansii/metodist-po-programmirovaniyu-na-python-38140998.html",
        "salary_from": 30000,
        "salary_to": 0
    }

    assert call_test_vacancy.return_dict() == vacancy_dict


def test_vacancy_gt(call_test_vacancy, call_test_vacancy_any):
    assert (call_test_vacancy > call_test_vacancy_any) == False


def test_vacancy_gt_digit(call_test_vacancy):
    assert (call_test_vacancy > 25000) == True


def test_vacancy_ge(call_test_vacancy, call_test_vacancy_any):
    assert (call_test_vacancy >= call_test_vacancy_any) == False


def test_vacancy_ge_digit(call_test_vacancy):
    assert (call_test_vacancy >= 25000) == True


def test_vacancy_lt(call_test_vacancy, call_test_vacancy_any):
    assert (call_test_vacancy < call_test_vacancy_any) == True


def test_vacancy_lt_digit(call_test_vacancy):
    assert (call_test_vacancy < 25000) == False


def test_vacancy_le(call_test_vacancy, call_test_vacancy_any):
    assert (call_test_vacancy <= call_test_vacancy_any) == True


def test_vacancy_le_digit(call_test_vacancy):
    assert (call_test_vacancy <= 25000) == False


def test_vacancy_eq(call_test_vacancy, call_test_vacancy_any):
    assert (call_test_vacancy == call_test_vacancy_any) == False


def test_vacancy_eq_digit(call_test_vacancy):
    assert (call_test_vacancy == 25000) == False
