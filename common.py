COEF_FROM = 1.2
COEF_TO = 0.8


def predict_salary(salary_from, salary_to):
    if salary_from is not None and salary_to is not None:
        return (salary_from + salary_to) / 2
    elif salary_from is not None:
        return salary_from * COEF_FROM
    elif salary_to is not None:
        return salary_to * COEF_TO
    else:
        return None
