import hh_data_provider
import superjob_data_provider
import common
import os

if __name__ == '__main__':
    hh_data = hh_data_provider.get_salaries()
    common.print_table('HeadHunter Moscow', hh_data)

    superjob_api_version = os.environ['SUPERJOB_API_VERSION']
    superjob_secret_key = os.environ['SUPERJOB_SECRET_KEY']
    superjob_data = superjob_data_provider.get_salaries(superjob_api_version, superjob_secret_key)
    common.print_table('SuperJob Moscow', superjob_data)
