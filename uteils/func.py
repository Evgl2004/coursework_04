def sort_by_salary_from(vacancy_list: list):
    for i in range(1, len(vacancy_list)):
        key = vacancy_list[i]
        j = i - 1
        while vacancy_list[j] > key and j >= 0:
            vacancy_list[j + 1] = vacancy_list[j]
            j -= 1
        vacancy_list[j + 1] = key
    return vacancy_list


def vacancy_object_to_dict(vacancies_list: list):
    return [item.return_dict() for item in vacancies_list]
