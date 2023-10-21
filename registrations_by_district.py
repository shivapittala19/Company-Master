"""numbe of registration in each  district"""
import datetime
import matplotlib.pyplot as plt
from main import maharashtra , pin_code_to_district

def registrations_by_district():
    """ numbe of registration in each  district """
    data_dict = {}
    for row in maharashtra:
        try:
            year = datetime.datetime.strptime(row['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + str(year)[2:]
        except ValueError:
            pass
        if year == 2015:
            key = row['Registered_Office_Address'].split(" ")[-1]
            if key in pin_code_to_district:
                if pin_code_to_district[key] in data_dict:
                    data_dict[pin_code_to_district[key]] += 1
                else:
                    data_dict[pin_code_to_district[key]] = 1
    plt.bar(data_dict.keys(),data_dict.values())
    plt.show()

registrations_by_district()
