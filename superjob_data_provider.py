import requests
import copy
import os
import common
from data import programmers_languages

TOWN = 4
CATALOGUES = [48]
BASE_PAYLOAD = {'town': TOWN, 'catalogues': CATALOGUES, 'keyword': ''}
BASE_HEADERS = {'X-Api-App-Id': ''}
BASE_API_URL = 'https://api.superjob.ru/{}/vacancies'


def get_salaries():
    return common.process_salaries(request_salaries(), get_rub_salary)


def request_salaries():
    salaries = []
    api_url = BASE_API_URL.format(os.environ['SUPERJOB_API_VERSION'])
    headers = copy.copy(BASE_HEADERS)
    headers['X-Api-App-Id'] = os.environ['SUPERJOB_SECRET_KEY']

    for language in programmers_languages:
        payload = copy.copy(BASE_PAYLOAD)
        payload['keyword'] = 'Программист {}'.format(language)

        page = 0
        get_next_results = True

        vacancies = []

        while get_next_results:
            payload['page'] = page
            response = requests.get(api_url, params=payload, headers=headers)
            get_next_results = response.json()['more']
            page += 1
            vacancies.extend(response.json()['objects'])

        salaries.append({'name': language, 'vacancies': vacancies})

    return salaries


def get_rub_salary(vacancy):
    if vacancy is None or vacancy['currency'] != 'rub':
        return None
    else:
        return common.predict_salary(vacancy['payment_from'], vacancy['payment_to'])