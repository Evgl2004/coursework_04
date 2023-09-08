from src.api import SuperJobAPI, HeadHunterAPI
from src.json_saver import JSONSaver
from uteils.func import sort_by_salary_from, vacancy_object_to_dict

if __name__ == "__main__":

    list_api = []

    input_keyword = input(
        "Укажите ключевое слово для поиска:\n")

    input_data = input(
        "Выберите портал для поиска:\n"
        "1 - HeadHunter\n"
        "2 - SuperJob\n"
        "3 - HeadHunter + SuperJob\n"
        "exit - завершить работу.\n")

    if input_data == '1':
        list_api.append(HeadHunterAPI(input_keyword.lower()))
    elif input_data == '2':
        list_api.append(SuperJobAPI(input_keyword.lower()))
    elif input_data == '3':
        list_api.append(HeadHunterAPI(input_keyword.lower()))
        list_api.append(SuperJobAPI(input_keyword.lower()))

    while input_data.lower() != 'exit':

        json_saver = JSONSaver('Vacancy')
        vacancies_list = []

        input_data = input(
            "Выберите пункт:\n"
            "1 - Вывести список вакансий\n"
            "2 - Поиск по ключевому слову\n"
            "3 - Отсортировать по минимальной зарплате\n"
            "4 - Удалить вакансию по ID\n"
            "exit - завершить работу.\n")

        if input_data == '1':

            formatted_vacancy = []

            for current_api in list_api:
                current_api.get_vacancies(1)
                formatted_vacancy.extend(current_api.formatted_vacancy())

            json_saver.write_vacancy(formatted_vacancy)

        elif input_data == '2':

            input_id = int(input("Введите ключевые слова для фильтрации вакансий:\n"))

        elif input_data == '3':
            json_saver.write_vacancy(vacancy_object_to_dict(sort_by_salary_from(json_saver.read_vacancy())))

        elif input_data == '4':
            input_id = int(input("Укажите ID для удаления из файла:\n"))

            json_saver.del_vacancy(input_id)

        if input_data.lower() != 'exit':
            vacancies_list = json_saver.read_vacancy()
            if len(vacancies_list) != 0:
                for vacancy in vacancies_list:
                    print(vacancy)
            else:
                print("Нет вакансий, соответствующих заданным критериям.")

