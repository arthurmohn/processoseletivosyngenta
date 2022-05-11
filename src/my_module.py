import sys

days_of_week = ['mon', 'tues', 'wed', 'thur', 'fri']
weekend = ['sat', 'sun']
fidelity = ['Rewards', 'Regular']

hotel_stars = {"Lakewood": 3, "Bridgewood": 4, "Ridgewood": 5}
hotel_values_rewards = {"Lakewood": [80, 80], "Bridgewood": [110, 50], "Ridgewood": [100, 40]}
hotel_values_regular = {"Lakewood": [110, 90], "Bridgewood": [160, 60], "Ridgewood": [220, 150]}

def get_cheapest_hotel_name(values):     # function to determine the cheapeast hotel name
    cheapest_hotel_name = []
    min_value = float("inf")

    for hotel, value in values.items():
        if value == min_value:
            cheapest_hotel_name.append(hotel)

        if value < min_value:
            min_value = value
            cheapest_hotel_name = []
            cheapest_hotel_name.append(hotel)

    if len(cheapest_hotel_name) > 1:     # if there are two or more hotels with the same value, the one with most stars is chosen
        hotel_star = []

        for hotel in cheapest_hotel_name:
            hotel_star.append(hotel_stars[hotel])
    
        cheapest_hotel = dict((star, hotel) for star, hotel in hotel_stars.items()).get(max(hotel_star))

    else:                                  # if only one hotel is cheaper
        cheapest_hotel = cheapest_hotel_name[0]
        
    return cheapest_hotel


def get_stay_cost(week_date, fidelity_program):        # calculating the value of the stay in each hotel, with fidelity program and without it
    values_dic = {}                                    # dictionaty with the name and the value of each hotel

    for hotel in hotel_values_regular:  

        for day in week_date:

            if(fidelity_program == "Rewards"):
                if day in weekend:
                    values_dic[hotel] =+ hotel_values_rewards[hotel][1]
                else:
                    values_dic[hotel] =+ hotel_values_rewards[hotel][0]
            
            else:
                if day in weekend:
                    values_dic[hotel] =+ hotel_values_regular[hotel][1]
                else:
                    values_dic[hotel] =+ hotel_values_regular[hotel][0]
    
    return values_dic


def get_cheapest_hotel(number):   #DO NOT change the function's name
    
    input = str(number)     #making sure input is a string

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

    cheapest_hotel = get_cheapest_hotel_name(values)

    return cheapest_hotel