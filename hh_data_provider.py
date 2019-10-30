import requests
import copy
import common
from data import programmers_languages

API_URL = 'https://api.hh.ru/vacancies'
BASE_PAYLOAD = {'area': 1, 'period': 30, 'text': ''}


def get_salaries():
    return common.process_salaries(request_salaries(), get_rub_salary)


def request_salaries():
    salaries = []

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
            vacancies.extend(response.json()['items'])

        salaries.append({'name': language, 'vacancies': vacancies})

    return salaries


def get_rub_salary(salary):
    if salary is None or salary['salary'] is None or salary['salary']['currency'] != 'RUR':
        return None
    else:
        return common.predict_salary(salary['salary']['from'], salary['salary']['to'])
