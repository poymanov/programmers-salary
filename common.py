COEF_FROM = 1.2
COEF_TO = 0.8


def predict_salary(salary_from, salary_to):
    if salary_from == 0:
        salary_from = None

    if salary_to == 0:
        salary_to = None

    if salary_from is not None and salary_to is not None:
        return (salary_from + salary_to) / 2
    elif salary_from is not None:
        return salary_from * COEF_FROM
    elif salary_to is not None:
        return salary_to * COEF_TO
    else:
        return None


def process_data(data, rub_salary_func):
    result = []

    for language in data:
        processed = 0
        found = 0
        salary = 0

        for vacancy in language['vacancies']:
            processed_salary = rub_salary_func(vacancy)
            found += 1

            if processed_salary is not None:
                salary += processed_salary
                processed += 1

        if processed == 0:
            average_salary = 0
        else:
            average_salary = int(salary/processed)

        result.append({language['name']: {
             'vacancies_found': found,
             'vacancies_processed': processed,
             'average_salary': average_salary
        }})

    return result