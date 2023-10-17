from main import maharashtra
import matplotlib.pyplot as plt
import datetime

def number_of_registrations_per_year():
    data_dict = {}
    for row in maharashtra:
        try:
            year = datetime.datetime.strptime(row['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + year[2:] #  correcting the data which went wrong while getting the datetime obj into year
            if year in data_dict:
                data_dict[year] += 1
            else:
                data_dict[year] = 1
        except:
            pass
    
    sorted_data_dict = dict(sorted(data_dict.items(),key=lambda x : x[0]))
    year , values = sorted_data_dict.keys() , sorted_data_dict.values()
    
    plt.bar(year,values)
    plt.show()
    
number_of_registrations_per_year()
    