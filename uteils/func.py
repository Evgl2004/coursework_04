def sort_by_salary_from(vacancy_list: list):
    """
    Сортировка экземпляров класса Вакансии, которые находятся в списке.
    Сортировка происходит методом Вставок.
    :param vacancy_list: Список с вакансиями, который необходимо отсортировать.
    :return: Возвращает отсортированный список с вакансиями.
    """
    for i in range(1, len(vacancy_list)):
        key = vacancy_list[i]
        j = i - 1
        while vacancy_list[j] > key and j >= 0:
            vacancy_list[j + 1] = vacancy_list[j]
            j -= 1
        vacancy_list[j + 1] = key
    return vacancy_list


def vacancy_object_to_dict(vacancies_list: list):
    """
    Преобразование списка с экземплярами класса Вакансии в данные формата JSON.
    :param vacancies_list: Список с экземплярами класса Вакансии.
    :return: Возвращает данные в формате JSON.
    """
    return [item.return_dict() for item in vacancies_list]
