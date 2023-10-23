""" to find the number registrations in each year """
import datetime
import matplotlib.pyplot as plt
import main

def number_of_registrations_per_year():
    """number registrations in each year"""
    registration = {}
    maharashtra = main.load_csv('Maharashtra.csv')
    for company in maharashtra:
        try:
            year = datetime.datetime.strptime(company['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + str(year)[2:]
            if year in registration:
                registration[str(year)] += 1
            else:
                registration[str(year)] = 1
        except ValueError:
            pass
    sorted_registration = dict(sorted(registration.items(),key=lambda x : x[0]))
    year , values = sorted_registration.keys() , sorted_registration.values()
    plt.bar(year,values)
    plt.xlabel("Year")
    plt.ylabel("Number of registrations")
    plt.title("Number of registrations per year")
    plt.xticks(rotation=90)
    plt.show()

number_of_registrations_per_year()
