import hh_data_provider
import superjob_data_provider

if __name__ == '__main__':
    superjob_data = superjob_data_provider.get_data()
    print(superjob_data)
    hh_data = hh_data_provider.get_data()
    print(hh_data)
