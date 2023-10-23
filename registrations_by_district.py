"""numbe of registration in each  district"""
import datetime
import matplotlib.pyplot as plt
import main

def registrations_by_district():
    """ numbe of registration in each  district """
    maharashtra = main.load_csv('Maharashtra.csv')
    pin_code_to_district = main.csv_reader('pincode.csv')
    registrations = {}
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
                district = pin_code_to_district[key]
                if district in registrations:
                    registrations[district] += 1
                else:
                    registrations[district] = 1
    plt.bar(registrations.keys(),registrations.values())
    plt.show()

registrations_by_district()
