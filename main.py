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

rows = ['CORPORATE_IDENTIFICATION_NUMBER', 
        'Company_Name', 
        'Company_status', 'Company_class',
        'Company_Category', 'Company_sub_category', 'DATE_OF_REGISTRATION',
        'REGISTERED_STATE', 'AUTHORIZED_CAP', 
        'PAIDUP_CAPITAL', 'Industrial_Class',
        'PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN', 
        'Registered_Office_Address', 'REGISTRAR_OF_COMPANIES', 
        'EMAIL_ADDR', 'Latest_Year_AR', 'Latest_Year_BS']

