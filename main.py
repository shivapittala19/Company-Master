import csv

def load_csv(file_name):
    file = open(file_name,'r',encoding='latin-1')
    lines = csv.DictReader(file)
    
    return lines

def csv_reader(file_name):
    file = open(file_name,'r',encoding='latin-1')
    lines = csv.DictReader(file)
    result_dict = {}
    for row in lines:
        pin_code = row['Pin Code']
        district = row['District']
        result_dict[pin_code] = district
        
    return result_dict

maharashtra = load_csv('Maharashtra.csv')
pin_code_to_district = csv_reader('pincode.csv')

