import hh_data_provider
import superjob_data_provider
import common


if __name__ == '__main__':
    hh_data = hh_data_provider.get_data()
    common.print_table('HeadHunter Moscow', hh_data)

    superjob_data = superjob_data_provider.get_data()
    common.print_table('SuperJob Moscow', superjob_data)
