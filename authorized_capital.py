""" find the number of companies invested captial between specific ranges """
import matplotlib.pylab as plt
from main import maharashtra

def authorized_capital():
    """ find the number of companies invested captial between specific ranges """
    lables = ["<= 1L",  "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
    data_dict = {
        "<= 1L" : 0,
        "1L to 10L" : 0,
        "10L to 1Cr" : 0,
        "1Cr to 10Cr":  0 ,
        "> 10 cr" : 0   
    }
    for row in maharashtra:
        curr = float(row['AUTHORIZED_CAP'])
        if curr <= 100000:
            data_dict["<= 1L"] += 1
        elif curr <= 1000000:
            data_dict["1L to 10L"] += 1
        elif curr <= 10000000:
            data_dict["10L to 1Cr"] += 1
        elif curr <= 100000000:
            data_dict["1Cr to 10Cr"] += 1
        else:
            data_dict["> 10 cr"] += 1
    weight = list(data_dict.values())
    plt.hist(lables,bins=5,weights=weight)
    plt.show()

authorized_capital()
