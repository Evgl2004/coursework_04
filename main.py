from src.api import SuperJobAPI, HeadHunterAPI
from src.json_saver import JSONSaver

if __name__ == "__main__":

    api_hh = HeadHunterAPI("Python")
    api_sj = SuperJobAPI("Python")

    formatted_vacancy = []

    for current_api in (api_hh, api_sj):
        current_api.get_vacancies(1)
        formatted_vacancy.extend(current_api.formatted_vacancy())

    json_saver = JSONSaver("Python")
    json_saver.write_vacancy(formatted_vacancy)

    vacancies = json_saver.read_vacancy()
    for vacancy in vacancies:
        print(vacancy)
