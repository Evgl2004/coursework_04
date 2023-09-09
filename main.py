from src.api import SuperJobAPI, HeadHunterAPI
from src.json_saver import JSONSaver
from uteils.func import sort_by_salary_from, vacancy_object_to_dict


def user_interaction():
    """
    Функция для взаимодействия с пользователем (консольный интерфейс взаимодействия)
    :return:
    """

    # инициируем список в котором будут помещены экземпляры классов взаимодействия с API
    list_api = []

    # инициируем переменные в которые поместим ответы пользователя,
    # будут использоваться как часть параметров запросов API
    input_number_records = input_data = ""

    # запрашиваем ключевое слово по которому будет происходить запрос по API
    input_keyword = input(
        "Укажите ключевое слово для поиска:\n")

    # запрашиваем количество записей, которые будут выводиться после запроса по API
    # цикл до тех по пока не будет введена цифра не равная 0
    while (not input_number_records.isdecimal()
           or input_number_records == '0'):

        input_number_records = input(
            "Укажите количество выводимых вакансий:\n")

        if (not input_number_records.isdecimal()
                or input_number_records == '0'):
            print("Введите число.")

    # запрашиваем информацию, где необходимо производить запрос по API (HH или SuperJob)
    # цикл до тех по пока не будет введена цифра
    while not input_data.isdecimal():

        input_data = input(
            "Выберите портал для поиска:\n"
            "1 - HeadHunter\n"
            "2 - SuperJob\n"
            "3 - HeadHunter + SuperJob\n")

        # после получения ответа инициализируем тот или иной экземпляр класса
        # и добавляем его в список для последующего обхода.
        if input_data == '1':
            list_api.append(HeadHunterAPI(input_keyword.lower(), int(input_number_records)))
        elif input_data == '2':
            list_api.append(SuperJobAPI(input_keyword.lower(), int(input_number_records)))
        elif input_data == '3':
            list_api.append(HeadHunterAPI(input_keyword.lower(), int(input_number_records)))
            list_api.append(SuperJobAPI(input_keyword.lower(), int(input_number_records)))
        else:
            input_data = ""
            print("Введите число от 1 до 3.")

    # основное меню выбора команд взаимодействия с полученными данными по API
    # цикл до тех пор, пока не будет введено ключевое слово выхода
    while input_data.lower() != 'exit':

        # инициализируем экземпляр класса по работе с файлом, для последующего сохранения полученного результата по API
        json_saver = JSONSaver('Vacancy')

        input_data = input(
            "Выберите пункт:\n"
            "1 - Вывести список вакансий\n"
            "2 - Поиск по ключевому слову\n"
            "3 - Отсортировать по минимальной зарплате\n"
            "4 - Удалить вакансию по ID\n"
            "exit - завершить работу.\n")

        if input_data == '1':

            # инициализируем список в который будет получен отформатированный результат запроса по API
            formatted_vacancy = []

            # обходим все добавленные в список экземпляры класса API
            # для каждого экземпляры выполняется один и тот же реализованный метод.
            for current_api in list_api:
                # получаем вакансии по набору параметров, которые были при инициализации экземпляра
                current_api.get_vacancies(1)
                # полученный набор данных приводим к единому виду
                formatted_vacancy.extend(current_api.formatted_vacancy())

            # отформатированные данные сохраняем в файл.
            json_saver.write_vacancy(formatted_vacancy)

        elif input_data == '2':

            input_keyword_filter = int(input(
                "Введите ключевые слова для фильтрации вакансий:\n"))

        elif input_data == '3':
            # последовательно выполняем следующие действия:
            # считываем сохраненные ранее вакансии с файла,
            # при считывании, данные преобразуются в экземпляры класса Вакансии
            # затем производим сортировку вакансий по нижней границе заработной платы
            # затем преобразуем вакансии из экземпляров класса Вакансии обратно в тип JSON
            # затем записываем данные в файл.
            json_saver.write_vacancy(vacancy_object_to_dict(sort_by_salary_from(json_saver.read_vacancy())))

        elif input_data == '4':

            input_id = ""
            # бесконечно ожидаем ввода цифры
            while not input_data.isdecimal():
                input_id = int(input(
                    "Укажите ID для удаления из файла:\n"))

                if not input_number_records.isdecimal():
                    print("Введите число.")

            # производим поиск по введённому идентификатору
            # получаем считанные вакансии из файла с удалённым элементом (если был найден)
            # полученный результат записываем результат в файл.
            json_saver.write_vacancy(json_saver.del_vacancy(input_id))

        else:
            print("Введите число от 1 до 4.")

        # если выбил выбраны цифры элементов меню, значит был выполнен некоторый алгоритм
        # выводим значения считанные из файла после выполненных алгоритмов меню
        if (input_data.lower() != 'exit'
                and input_data.isdecimal()
                and int(input_data) in range(4)):
            vacancies_list = json_saver.read_vacancy()
            if len(vacancies_list) != 0:
                for vacancy in vacancies_list:
                    print(vacancy)
            else:
                print("Нет вакансий, соответствующих заданным критериям.")


if __name__ == "__main__":
    # вызываем основную процедуру консольного взаимодействия через меню.
    user_interaction()
