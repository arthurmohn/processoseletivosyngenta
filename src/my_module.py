import sys

days_of_week = ['mon', 'tues', 'wed', 'thur', 'fri']
weekend = ['sat', 'sun']
fidelity = ['Rewards', 'Regular']

hotel_values_rewards = {"Lakewood": [80, 80], "Bridgewood": [110, 50], "Ridgewood": [100, 40]}
hotel_values_regular = {"Lakewood": [110, 90], "Bridgewood": [160, 60], "Ridgewood": [220, 150]}

def get_cheapest_hotel_names(values):     # function to determine the cheapeast hotel
    cheapest_hotel_name = []
    min_value = float("inf")
    for name, value in values.items():
        if value == min_value:
            cheapest_hotel_name.append(name)
        if value < min_value:
            min_value = value
            cheapest_hotel_name = []
            cheapest_hotel_name.append(name)

    return cheapest_hotel_name


def get_stay_cost(week_date, fidelity_program):       # calculating the value of the stay in each hotel, with fidelity program and without it
    total_Lakewood = 0
    total_Bridgewood = 0
    total_Ridgewood = 0

    for day in week_date:
        if(fidelity_program == "Rewards"):
            if day in weekend:
                total_Lakewood += hotel_values_rewards["Lakewood"][1]
                total_Bridgewood += hotel_values_rewards["Bridgewood"][1]
                total_Ridgewood += hotel_values_rewards["Ridgewood"][1]

            else:
                total_Lakewood += hotel_values_rewards["Lakewood"][0]
                total_Bridgewood += hotel_values_rewards["Bridgewood"][0]
                total_Ridgewood += hotel_values_rewards["Ridgewood"][0]
        
        else:
            if day in weekend:
                total_Lakewood += hotel_values_regular["Lakewood"][1]
                total_Bridgewood += hotel_values_regular["Bridgewood"][1]
                total_Ridgewood += hotel_values_regular["Ridgewood"][1]

            else:
                total_Lakewood += hotel_values_regular["Lakewood"][0]
                total_Bridgewood += hotel_values_regular["Bridgewood"][0]
                total_Ridgewood += hotel_values_regular["Ridgewood"][0]

    values = {"Lakewood": total_Lakewood, "Bridgewood": total_Bridgewood, "Ridgewood": total_Ridgewood}     # dictionaty with the name and the value of each hotel

    return values


def get_cheapest_hotel(number):   #DO NOT change the function's name
    
    input = str(number)     #making sure function input is a string

    s_input = input.replace(':', ' ').replace(',', ' ').split()     # removing punctuation and spliting the words

    try:
        fidelity_program = s_input[0]      # saving the fidelity program mode in its own variable

        if fidelity_program not in fidelity:
            raise ValueError("Fidelity program not available!")
    except ValueError as fe:
        print(fe)
        sys.exit(1)

    stay_date = s_input[1:]      # saving the date of reservation

    week_date = []          # variable to save the extracted day-of-the-week

    for i in range(len(stay_date)):      # extracting the days-of-the-week from the date format

        try:
            day = stay_date[i][stay_date[i].find("(") + 1:stay_date[i].find(")")]
            week_date.append(day)
            if (day not in days_of_week) and (day not in weekend):
                raise ValueError("Wrong day-of-the-week format!")
        except ValueError as de:
            print(de)
            sys.exit(1)

    values = get_stay_cost(week_date, fidelity_program)

    cheapest_hotel_names = get_cheapest_hotel_names(values)

    if len(cheapest_hotel_names) > 1:     # if there are two or more hotels with the same value, the one with most stars is chosen

        if "Ridgewood" in cheapest_hotel_names:
            cheapest_hotel = "Ridgewood"

        else:
            cheapest_hotel = "Bridgewood"

    else:       # if only one hotel is cheaper
        cheapest_hotel = cheapest_hotel_names[0]

    return cheapest_hotel