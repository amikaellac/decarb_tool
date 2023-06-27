
import csv
def calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360):
    DAYS_PER_YEAR =365 
    co2_dict = {}  # Create an empty dictionary

    list_of_ships = []
    underway_x_values =[]
    not_underway_x_values = []
    coldiron_x_values = []
    b = []
    optimum_values =[]
    worst_values = []

    with open('fuel_consumption_values.csv','r') as csvfile: 
        csv_reader = csv.reader(csvfile)
        next(csv_reader,None) #skips the header 
        
        for line in csv_reader: 
            list_of_ships.append(line[0])
            underway_x_values.append(line[1])
            not_underway_x_values.append(line[2])
            coldiron_x_values.append(line[3])
            b.append(line[4])
            optimum_values.append(line[5])
            worst_values.append(line[6])

    # print(list_of_ships)
    # print(underway_x_values)
    # print(not_underway_x_values)
    # print(coldiron_x_values)
    # print(optimum_values)
    # print(worst_values)


    #fuel_types = ['F76', 'Ethanol', 'Liquid Petroleum gas', 'Methanol', 'All',]

    if ship_name in list_of_ships : #and fuel_type in fuel_types: 
        index = list_of_ships.index(ship_name)
        #fuel_index = fuel_types.index(fuel_type)


        # print(index)
         # I added a zero to check caluclations 
        # underway_values = [0,28.992, 14.438, 29.861, 1.1068,24.867,12.162,42.691,10.619,23.038,10.663,9.8959,21.566,28.075,46.501,12.07,]
        # not_underway_values = [0,8.1288, 4.6906, 6.0818, 0.2608,5.4049,3.7654,13.337,0.6568,11.841,1.7882,1.8031,9.1597,4.6964,18.91,3.4972]
        # cold_iron_values = [0,0.0153, 0.0687, 0.0168, 0.0012,0.0144,0.0194,0.01221,0.0296,0.0219,0.03,0.0515,0.042,0.0005,0.1845,0.0308]

        # Optimum_fuel_consumption = [0,3.083333333, 1.107142857,2.666666667,0,0,0,1.107142857,0,0,0,0,0,0,0,0,]
        # Worst_fuel_consumption = [0,4.428571429,2.69047619,6.33333333,0,0,0,2.738095238,0,0,0,0,0,0,0,0,]

        #conversions 
        hours_year =8760
        hours_day = 24

        bbl_to_co2 = 942.48
        lbs_to_ton = 0.0005
        ethanol_to_co2 = 532.41573
        lpg_to_co2 = 525.9341472
        menthol_to_co2 = 379.635564

        ethanol_density = 0.5934
        lpg_density = 1.0549
        methanol_density = 0.4989
    
        f_underway = float(underway)
        f_not_underway = float(not_underway)
        f_cold_iron = float(cold_iron)
        xvalue_underway = float(underway_x_values[index])     #stores value from matching index 
        xvalue_not_underway = float(not_underway_x_values[index])
        xvalue_cold_iron = float(coldiron_x_values[index])

        optimum_value = float(optimum_values[index])
        worst_value = float(worst_values[index]) 
        b_value =float(b[index])

        #F76 BBL  # BBL underway == F76 BBL                                                                                     #All calulations are dependant on F76 - Diesel 
        bbl_underway = round(((f_underway * xvalue_underway + b_value) * hours_year),2)
        bbl_not_underway = round(((f_not_underway * xvalue_not_underway + b_value) * hours_year),2)
        bbl_cold_iron = round(((f_cold_iron * xvalue_cold_iron + b_value) * hours_year),2) 

        # BBL F76
        ethanol_underway = round((bbl_underway / ethanol_density),2)
        ethanol_not_underway = round((bbl_not_underway / ethanol_density),2)
        ethanol_cold_iron = round((bbl_cold_iron / ethanol_density),2)

        #BBL LPG
        lpg_underway = round((bbl_underway / lpg_density),2)
        lpg_not_underway = round((bbl_not_underway / lpg_density),2)
        lpg_cold_iron = round((bbl_cold_iron / lpg_density),2)
        #bbl menthol
        methanol_underway = round((bbl_underway / methanol_density),2)
        methanol_not_underway = round((bbl_not_underway / methanol_density),2)
        methanol_cold_iron = round((bbl_cold_iron / methanol_density),2) 


        #BBL to CO2 conversion for each fuel type 
        f76_co2_underway = round(bbl_underway * bbl_to_co2 * lbs_to_ton, 2)
        f76_co2_not_underway = round(bbl_not_underway * bbl_to_co2 * lbs_to_ton, 2)
        f76_co2_cold_iron = round(bbl_cold_iron * bbl_to_co2 * lbs_to_ton, 2)

        ethanol_co2_underway = round(ethanol_underway * ethanol_to_co2 * lbs_to_ton, 2)
        ethanol_co2_not_underway = round(ethanol_not_underway * ethanol_to_co2 * lbs_to_ton, 2)
        ethanol_co2_cold_iron = round(ethanol_cold_iron * ethanol_to_co2 * lbs_to_ton, 2)

        lpg_co2_underway = round(lpg_underway * lpg_to_co2 * lbs_to_ton, 2)
        lpg_co2_not_underway = round(lpg_not_underway * lpg_to_co2 * lbs_to_ton, 2)
        lpg_co2_cold_iron = round(lpg_cold_iron * lpg_to_co2 * lbs_to_ton, 2)

        methanol_co2_underway = round(methanol_underway * menthol_to_co2 * lbs_to_ton, 2)
        methanol_co2_not_underway = round(methanol_not_underway * menthol_to_co2 * lbs_to_ton, 2)
        methanol_co2_cold_iron = round(methanol_cold_iron * menthol_to_co2 * lbs_to_ton, 2)

        total_co2_used_f76 = round(f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron, 2)
        total_co2_used_ethanol = round(ethanol_co2_underway + ethanol_co2_not_underway + ethanol_co2_cold_iron, 2)
        total_co2_used_lpg = round(lpg_co2_underway + lpg_co2_not_underway + lpg_co2_cold_iron, 2)
        total_co2_used_menthol = round(methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron, 2)

        #co2e per mission 
        co2e_per_mission_f76 = round(total_co2_used_f76 * (mission_days/DAYS_PER_YEAR),2)
        co2e_per_mission_ethanol = round(total_co2_used_ethanol * (mission_days/DAYS_PER_YEAR),2)
        co2e_per_mission_lpg = round(total_co2_used_lpg* (mission_days/DAYS_PER_YEAR),2) 
        co2e_per_mission_methanol = round(total_co2_used_menthol * (mission_days/DAYS_PER_YEAR),2)

        #Worst/Best case range F76
        f76_worst_case_range = round((bbl_underway * worst_value),2)
        f76_best_case_range =  round((bbl_underway * optimum_value),2)
        f76_worst_case_tons_of_co2 = round((f76_co2_underway/f76_worst_case_range),9)
        f76_best_case_tons_of_co2 = round((f76_co2_not_underway/f76_best_case_range),9)

        #worst/best case range ethanol
        ethanol_worst_case = round((ethanol_underway * worst_value),2)
        ethanol_best_case = round((ethanol_underway * optimum_value),2)
        ethanol_worst_case_co2 = round((ethanol_co2_underway/ethanol_worst_case),9)
        ethanol_best_case_co2 = round((ethanol_co2_not_underway/ethanol_best_case),9)

        #worst/best case range liquid petroleum gas 
        lpg_worst_case = round((lpg_underway *worst_value),2)
        lpg_best_case = round((lpg_underway * optimum_value),2)
        lpg_worst_case_co2 = round((lpg_co2_underway/ lpg_worst_case),9)
        lpg_best_case_co2 = round((lpg_not_underway/lpg_best_case),9)
        

        #Worst/best case range Methanol 

        methanol_worst_case = round((methanol_underway * worst_value ),2)
        methanol_best_case = round((methanol_underway * optimum_value),2)
        methanol_worst_case_co2 = round((methanol_co2_underway/ methanol_worst_case ),9)
        methanol_best_case_co2 = round((methanol_co2_not_underway/methanol_best_case),9) 
    
        #Dictionaries  
        f76_co2_dict = {
            'F-76 Military Deisel Consumption ' :  (' '),
            'Annual hours Underway ' : (hours_year * underway),
            'Annual hours Not Underway ' : (hours_year * not_underway) ,
            'Annual hours Cold Iron ' :  (hours_year * cold_iron), 

            'BBL Fuel Consumed Underway (est)' : bbl_underway,
            'BBL Fuel Consumed Not Underway (est) ' : bbl_not_underway,
            'BBL Fuel Consumed cold Iron (est) ' : bbl_cold_iron,
            'Total BBL Fuel Consumed (est)'  : round((bbl_underway + bbl_not_underway + bbl_cold_iron),2),

            'CO2E Underway (est Tons) ': f76_co2_underway,
            'CO2E Not underway (est Tons) ': f76_co2_not_underway,
            'CO2E Cold Iron (est Tons) ': f76_co2_cold_iron,
            'Total CO2E (est Tons) ': total_co2_used_f76,
            'Total Co2E per mission (est tons)' : co2e_per_mission_f76, 

            'Worst Case Range (NM)' : f76_worst_case_range, 
            'Best Case Range (NM)' : f76_best_case_range, 
            'Worst Case Tons of CO2E/NM ' : f76_worst_case_tons_of_co2,
            'Best Case Tons of CO2E/NM ' : f76_best_case_tons_of_co2,
        }
        co2_dict['F76_CO2'] = f76_co2_dict

        ethanol_co2_dict = {
            'Ethanol consumption '              :  (' '),
            'Annual Hours Underway ' : (hours_year *underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year * cold_iron),
            
            'BBL Fuel Consumed Underway (est)' : ethanol_underway ,
            'BBL Fuel Consumed Not Underway (est)' : ethanol_not_underway ,
            'BBL Fuel Consumed Cold Iron (est) ' : ethanol_co2_cold_iron ,
            'Total BBL Fuel Consumed (est)'  : round((ethanol_underway + ethanol_not_underway + ethanol_cold_iron),2), 

            'CO2E underway (est Tons)': ethanol_co2_underway,
            'CO2E Not Underway (est Tons) ': ethanol_co2_not_underway,
            'CO2E Cold Iron (est Tons) ': ethanol_co2_cold_iron,
            'Total CO2E (est Tons) ': total_co2_used_ethanol,
            'Total Co2E per mission (est tons)' : co2e_per_mission_ethanol,

            'Worst Case Range (NM)' : ethanol_worst_case, 
            'Best Case Range (NM)' : ethanol_best_case, 
            'Worst Case Tons of CO2E/NM ' : ethanol_worst_case_co2,
            'Best Case Tons of CO2E/NM ' : ethanol_best_case_co2,
        }
        

        co2_dict['Ethanol_CO2'] = ethanol_co2_dict

        lpg_co2_dict = {
            'Liquid Petroleum gas ' :    ('  '), 
            'Annual Hours Underway ' : (hours_year *underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year  * cold_iron), 

            'BBL Fuel Consumed Underway (est) ' : lpg_underway ,
            'BBL Fuel Consumed Not Underway (est) ' : lpg_not_underway,
            'BBL Fuel Consumed Cold Iron (est) ' : lpg_cold_iron ,
            'Total BBL Fuel Consumed (est) '  : round((lpg_underway + lpg_not_underway + lpg_cold_iron),2), 

            'CO2E underway (est Tons) ': lpg_co2_underway,
            'CO2E Not Underway (est Tons) ': lpg_co2_not_underway,
            'CO2E Cold Iron (est Tons) ': lpg_co2_cold_iron,
            'Total CO2E (est Tons) ': total_co2_used_lpg,
            'Total Co2E per mission (est tons)' : co2e_per_mission_lpg,

            'Worst Case Range (NM)' : lpg_worst_case, 
            'Best Case Range (NM)' : lpg_best_case, 
            'Worst Case Tons of CO2E/NM ' : lpg_worst_case_co2,
            'Best Case Tons of CO2E/NM ' : lpg_best_case_co2, 

        }

        co2_dict['LPG_CO2'] = lpg_co2_dict

        Methanol_CO2_dict = {
            'Menthol consumption '  : ('   '),
            'Annual Hours Underway ' : (hours_year  * underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year * cold_iron), 

            'BBL Fuel Consumed Underway (est) ' : methanol_underway ,
            'BBL Fuel Consumed Not Underway (est) ' : methanol_not_underway ,
            'BBL Fuel Consumed Cold Iron (est) ' : methanol_cold_iron,
            'Total BBL FUel Consumed (est) ' : round((methanol_underway + methanol_not_underway + methanol_cold_iron),2),

            'CO2E underway (est Tons) ': methanol_co2_underway,
            'CO2E Not Underway (est Tons) ': methanol_co2_not_underway,
            'CO2E Cold Iron (est Tons) ': methanol_co2_cold_iron,
            'Total CO2E (est Tons) ': total_co2_used_menthol,
            'Total Co2E per mission (est tons)' : co2e_per_mission_methanol, 

            'Worst Case Range (NM)' : methanol_worst_case,
            'Best Case Range (NM)' : methanol_best_case,
            'Worst Case Tons of CO2E/NM ' :methanol_worst_case_co2,
            'Best Case Tons of CO2E/NM ' : methanol_best_case_co2,

        }

        co2_dict['Methanol_CO2'] = Methanol_CO2_dict

        
        if fuel_type == 'F76':
            return co2_dict['F76_CO2']

        elif fuel_type == 'Ethanol':
            return co2_dict['Ethanol_CO2']

        elif fuel_type == 'Methanol':
            return co2_dict['Methanol_CO2']

        elif fuel_type == 'LPG':
            return co2_dict['LPG_CO2']

        elif fuel_type == 'All' : 
            return co2_dict
        
        else:
            print("Invalid fuel")

        return co2_dict

ship_name = 'LHA-6CL' #input("Enter ship name: ")
fuel_type = 'Methanol' #input("Enter the fuel type: ")
CO2_calculations = calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360)

#print('Class: ', ship_name, '\nFuel: ', fuel_type) 

if fuel_type == 'All':
    for key, value in CO2_calculations.items():
        #print(key + ':', value)
        if key in CO2_calculations.keys():
            fuel_dict = CO2_calculations[key]
            for fuel_key, fuel_value in fuel_dict.items():
                print(fuel_key + ':', fuel_value)
        else:
            print("Invalid fuel type.")

else:
    print(fuel_type + ' CO2 calculations:')
    for key, value in CO2_calculations.items():
        print(key + ':', value)