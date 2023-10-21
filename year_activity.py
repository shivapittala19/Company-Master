""" top business activities in each year"""
import datetime
import matplotlib.pyplot as plt
from main import maharashtra

def year_vs_principal_business():
    """ top business activities in each year"""
    business_activities = {}
    # creating a dictinary for business principle activities for each year
    # {
    #     'year' : {
    #         'activity1' : 'number_of_reg', 'activity2':'number_of_reg'
    #     }
    # }
    for row in maharashtra:
        try:
            year = datetime.datetime.strptime(row['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + str(year)[2:]
            if  int(year) >= 2012:
                activity = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
                if year in business_activities and activity != 'Unclassified':
                    if activity in business_activities[year]:
                        business_activities[year][activity] += 1
                    else:
                        business_activities[year][activity] = 1
                else:
                    business_activities[year] = {activity: 1}
        except ValueError:
            pass
    # for every year soting the business activities based on its value
    sorted_business_activity = {
        year : dict(sorted(activity.items(),key=lambda x : x[1],reverse=True))
        for year,activity in business_activities.items()
    }
    # sorting by year , for display the plot ordered by year
    sorted_business_activity_year = dict(
        sorted(sorted_business_activity.items(),key = lambda x : x [0])
    )
    # get the list of top 5 activities
    top_five_activities = list(sorted_business_activity_year[2012].keys())[:5]
    # Create the grouped bar plot
    years = list(sorted_business_activity_year.keys())
    width = 0.1  # Width of each bar
    x = range(len(years))
    color_codes = [
        "#FF5733",  # Red
        "#33FF57",  # Green
        "#FFFF33",  # Yellow
        "#FF33FF",  # Pink
        "#33FFFF",  # Cyan
    ]
    for index , value in enumerate(top_five_activities):
        # for every year get the list of values of top 5 activities
        values = [data.get(value) for data in list(sorted_business_activity_year.values())]
        plt.bar(
            [pos + index * width for pos in x],
            values,
            width=width,
            label = value,
            color = color_codes[index]
        )
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Grouped Bar Plot for Business Activities')
    plt.xticks([pos + width * (len(top_five_activities)) for pos in x], years)
    plt.legend()
    plt.show()

year_vs_principal_business()
