import requests
import copy
import common
from data import programmers_languages

API_URL = 'https://api.hh.ru/vacancies'
BASE_PAYLOAD = {'area': 1, 'period': 30, 'text': ''}


def get_data():
    requested_data = request_data()
    return process_data(requested_data)


def get_rub_salary(salary):
    if salary is None or salary['currency'] != 'RUR':
        return None
    else:
        return common.predict_salary(salary['from'], salary['to'])


def process_data(data):
    result = []

    for language in data:
        processed = 0
        found = 0
        salary = 0

        for vacancy in language['vacancies']:
            processed_salary = get_rub_salary(vacancy['salary'])
            found += 1

            if processed_salary is not None:
                salary += processed_salary
                processed += 1

        result.append({language['name']: {
             'vacancies_found': found,
             'vacancies_processed': processed,
             'average_salary': int(salary / processed)
        }})

    return result


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
