import requests
import copy
import os
import common
from dotenv import load_dotenv
from data import programmers_languages

load_dotenv()

SUPERJOB_SECRET_KEY = os.environ['SUPERJOB_SECRET_KEY']
SUPERJOB_API_VERSION = os.environ['SUPERJOB_API_VERSION']
TOWN = 4
CATALOGUES = [48]
BASE_PAYLOAD = {'town': TOWN, 'catalogues': CATALOGUES, 'keyword': ''}
BASE_HEADERS = {'X-Api-App-Id': SUPERJOB_SECRET_KEY}
API_URL = 'https://api.superjob.ru/{}/vacancies'.format(SUPERJOB_API_VERSION)


def get_data():
    requested_data = request_data()
    return common.process_data(requested_data, get_rub_salary)


def request_data():
    data = []

    for language in programmers_languages:
        payload = copy.copy(BASE_PAYLOAD)
        payload['keyword'] = 'Программист {}'.format(language)

        page = 0
        get_next_results = True

        vacancies = []

        while get_next_results:
            payload['page'] = page
            response = requests.get(API_URL, params=payload, headers=BASE_HEADERS)
            get_next_results = response.json()['more']
            page += 1

            for item in response.json()['objects']:
                vacancies.append(item)

        data.append({'name': language, 'vacancies': vacancies})

    return data


def get_rub_salary(vacancy):
    if vacancy is None or vacancy['currency'] != 'rub':
        return None
    else:
        return common.predict_salary(vacancy['payment_from'], vacancy['payment_to'])