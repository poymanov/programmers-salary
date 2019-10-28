import requests
import copy
import common
from data import programmers_languages

API_URL = 'https://api.hh.ru/vacancies'
BASE_PAYLOAD = {'area': 1, 'period': 30, 'text': ''}


def get_data():
    requested_data = request_data()
    return common.process_data(requested_data, get_rub_salary)


def request_data():
    data = []

    for language in programmers_languages:
        payload = copy.copy(BASE_PAYLOAD)
        payload['text'] = 'Программист {}'.format(language)

        page = 0
        page_numbers = 1

        vacancies = []

        while page < page_numbers:
            payload['page'] = page
            response = requests.get(API_URL, payload)
            page_numbers = response.json()['pages']
            page += 1

            for item in response.json()['items']:
                vacancies.append(item)

        data.append({'name': language, 'vacancies': vacancies})

    return data


def get_rub_salary(salary):
    if salary is None or salary['salary'] is None or salary['salary']['currency'] != 'RUR':
        return None
    else:
        return common.predict_salary(salary['salary']['from'], salary['salary']['to'])
