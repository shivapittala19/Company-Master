""" to find the number registrations in each year """
import datetime
import matplotlib.pyplot as plt
from main import maharashtra

def number_of_registrations_per_year():
    """number registrations in each year"""
    data_dict = {}
    for row in maharashtra:
        try:
            year = datetime.datetime.strptime(row['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + str(year)[2:]
            if year in data_dict:
                data_dict[str(year)] += 1
            else:
                data_dict[str(year)] = 1
        except ValueError:
            pass
    sorted_data_dict = dict(sorted(data_dict.items(),key=lambda x : x[0]))
    year , values = sorted_data_dict.keys() , sorted_data_dict.values()
    plt.bar(year,values)
    plt.show()

number_of_registrations_per_year()
