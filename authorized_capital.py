""" find the number of companies invested captial between specific ranges """
import matplotlib.pylab as plt
import main

def authorized_capital():
    """ find the number of companies invested captial between specific ranges """
    lables = ["<= 1L",  "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
    capital_data = {
        "<= 1L" : 0,
        "1L to 10L" : 0,
        "10L to 1Cr" : 0,
        "1Cr to 10Cr":  0 ,
        "> 10 cr" : 0   
    }
    maharashtra = main.load_csv('Maharashtra.csv')
    for company in maharashtra:
        curr = float(company['AUTHORIZED_CAP'])
        if curr <= 100000:
            capital_data["<= 1L"] += 1
        elif curr <= 1000000:
            capital_data["1L to 10L"] += 1
        elif curr <= 10000000:
            capital_data["10L to 1Cr"] += 1
        elif curr <= 100000000:
            capital_data["1Cr to 10Cr"] += 1
        else:
            capital_data["> 10 cr"] += 1
    weight = list(capital_data.values())
    plt.hist(lables,bins=5,weights=weight)
    plt.xlabel("Capital range")
    plt.ylabel("number of company captial falls in range ")
    plt.title("Histogram of captial amount ")
    plt.show()

authorized_capital()
