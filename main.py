import hh_data_provider
import superjob_data_provider
import common

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    hh_data = hh_data_provider.get_salaries()
    common.print_table('HeadHunter Moscow', hh_data)

    superjob_data = superjob_data_provider.get_salaries()
    common.print_table('SuperJob Moscow', superjob_data)
