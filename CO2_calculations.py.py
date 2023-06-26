def calculate_ship_info(ship, fuel_type, underway=0.4, not_underway=0.5, cold_iron=0.1, mission_days =180, mission_underway =0.9, mission_notunderway=0.1):
    CO2_dict = {}  # Create an empty dictionary

    
    list_of_ships = [
        'LHA-6CL', 'LPD-17CL', 'CG-47CL', 'MCM-1CL', 'DDG-51CL', 'LSD-41CL',
        'LHD-1CL', 'LCS-1CL', 'LCC-19CL', 'FFG-7CL', 'LCS-2CL', 'LPD-4CL',
        'DDG-1000CL', 'LHA-1CL', 'LSD-49CL']
    
    fuel_types = ['F76', 'Ethanol', 'Liquid Petroleum gas', 'Menthol', 'All',]

    if ship in list_of_ships and fuel_type in fuel_types:
        index = list_of_ships.index(ship)
        fuel_index = fuel_types.index(fuel_type)

        underway_values = [28.992, 14.438, 29.861, 1.1068,24.867,12.162,42.691,10.619,23.038,10.663,9.8959,21.566,28.075,46.501,12.07,]
        not_underway_values = [8.1288, 4.6906, 6.0818, 0.2608,5.4049,3.7654,13.337,0.6568,11.841,1.7882,1.8031,9.1597,4.6964,18.91,3.4972]
        cold_iron_values = [0.0153, 0.0687, 0.0168, 0.0012,0.0144,0.0194,0.01221,0.0296,0.0219,0.03,0.0515,0.042,0.0005,0.1845,0.0308]

        #conversions 
        b_value = 0
        hours_year = 8760
        hours_day = 24

        BBL_to_CO2 = 942.48
        lbs_to_ton = 0.0005
        Ethanol_to_CO2 = 532.41573
        LPG_to_CO2 = 525.9341472
        Menthol_to_CO2 = 379.635564

        Ethanol_density = 0.5934
        LPG_density = 1.0549
        Menthol_density = 0.4989
        #conversions end 

        #mission calc 
        mission_days= 180
        mission_underway = 0.9
        mission_notunderway = 0.1 

        f_underway = float(underway)
        f_not_underway = float(not_underway)
        f_cold_iron = float(cold_iron)
        xvalue_underway = underway_values[index]
        xvalue_not_underway = not_underway_values[index]
        xvalue_cold_iron = cold_iron_values[index]

        mission_hours_underway = (mission_days*mission_underway*hours_day)
        mission_hours_notunderway = (mission_days*mission_notunderway*hours_day)


        #F76 BBL  # BBL underway == F76 BBL
        bbl_underway = round(((f_underway * xvalue_underway + b_value) * hours_year),2)
        bbl_not_underway = round(((f_not_underway * xvalue_not_underway + b_value) * hours_year),2)
        bbl_cold_iron = round(((f_cold_iron * xvalue_cold_iron + b_value) * hours_year),2) 

        # BBL F76
        Ethanol_underway = round((bbl_underway / Ethanol_density),2)
        Ethanol_not_underway = round((bbl_not_underway / Ethanol_density),2)
        Ethanol_cold_iron = round((bbl_cold_iron / Ethanol_density),2)

        #BBL LPG
        LPG_underway = round((bbl_underway / LPG_density),2)
        LPG_not_underway = round((bbl_not_underway / LPG_density),2)
        LPG_cold_iron = round((bbl_cold_iron / LPG_density),2)
        #BBL Menthol
        Menthol_underway = round((bbl_underway / Menthol_density),2)
        Menthol_not_underway = round((bbl_not_underway / Menthol_density),2)
        Menthol_cold_iron = round((bbl_cold_iron / Menthol_density),2) 
        

        #Mission caluculator BBL 
        Mission_BBL_underway = (mission_hours_underway * xvalue_underway + b_value)
        Mission_BBL_notunderway =(mission_hours_notunderway * xvalue_not_underway + b_value)


        #Total Mission BBL for all fuel types 
        Total_mission_bbl_F76= (Mission_BBL_notunderway + Mission_BBL_underway)
        Total_mission_bbl_Ethanol = ((Mission_BBL_underway + Mission_BBL_notunderway)/Ethanol_density)
        Total_mission_bbl_LPG = ((Mission_BBL_underway + Mission_BBL_notunderway)/LPG_density)
        Total_mission_bbl_Menthol = ((Mission_BBL_underway + Mission_BBL_notunderway)/Menthol_density)

        #Total Mission CO2 in tons 
        
        Total_Mission_CO2_F76 = round((Total_mission_bbl_F76 * BBL_to_CO2 * lbs_to_ton),2)
        Total_Mission_CO2_Ethanol = round((Total_mission_bbl_Ethanol * BBL_to_CO2 * lbs_to_ton),2)
        Total_Mission_CO2_LPG = round((Total_mission_bbl_LPG * BBL_to_CO2 * lbs_to_ton),2)
        Total_Mission_CO2_Menthol = round((Total_mission_bbl_Menthol * BBL_to_CO2 * lbs_to_ton),2)

        #BBL to CO2 conversion for each fuel type 
        F76_CO2_underway = round(bbl_underway * BBL_to_CO2 * lbs_to_ton, 2)
        F76_CO2_not_underway = round(bbl_not_underway * BBL_to_CO2 * lbs_to_ton, 2)
        F76_CO2_cold_iron = round(bbl_cold_iron * BBL_to_CO2 * lbs_to_ton, 2)

        Ethanol_CO2_underway = round(Ethanol_underway * Ethanol_to_CO2 * lbs_to_ton, 2)
        Ethanol_CO2_not_underway = round(Ethanol_not_underway * Ethanol_to_CO2 * lbs_to_ton, 2)
        Ethanol_CO2_cold_iron = round(Ethanol_cold_iron * Ethanol_to_CO2 * lbs_to_ton, 2)

        LPG_CO2_underway = round(LPG_underway * LPG_to_CO2 * lbs_to_ton, 2)
        LPG_CO2_not_underway = round(LPG_not_underway * LPG_to_CO2 * lbs_to_ton, 2)
        LPG_CO2_cold_iron = round(LPG_cold_iron * LPG_to_CO2 * lbs_to_ton, 2)

        Menthol_CO2_underway = round(Menthol_underway * Menthol_to_CO2 * lbs_to_ton, 2)
        Menthol_CO2_not_underway = round(Menthol_not_underway * Menthol_to_CO2 * lbs_to_ton, 2)
        Menthol_CO2_cold_iron = round(Menthol_cold_iron * Menthol_to_CO2 * lbs_to_ton, 2)

        Total_CO2_used_F76 = round(F76_CO2_underway + F76_CO2_not_underway + F76_CO2_cold_iron, 2)
        Total_CO2_used_Ethanol = round(Ethanol_CO2_underway + Ethanol_CO2_not_underway + Ethanol_CO2_cold_iron, 2)
        Total_CO2_used_LPG = round(LPG_CO2_underway + LPG_CO2_not_underway + LPG_CO2_cold_iron, 2)
        Total_CO2_used_Menthol = round(Menthol_CO2_underway + Menthol_CO2_not_underway + Menthol_CO2_cold_iron, 2)

    
        #Dictionaries  
        F76_CO2_dict = {
            'F-76 Military Deisel Consumption ' :  (' '),
            'Annual hours Underway ' : (hours_year *underway),
            'Annual hours Not Underway ' : (hours_year * not_underway) ,
            'Annual hours Cold Iron ' :  (hours_year*cold_iron), 

            'BBL Fuel Consumed Underway (est)' : bbl_underway,
            'BBL Fuel Consumed Not Underway (est) ' : bbl_not_underway,
            'BBL Fuel Consumed cold Iron (est) ' : bbl_cold_iron,
            'Total BBL Fuel Consumed (est)'  : round((bbl_underway + bbl_not_underway + bbl_cold_iron),2),

            'CO2E Underway (est Tons) ': F76_CO2_underway,
            'CO2E Not underway (est Tons) ': F76_CO2_not_underway,
            'CO2E Cold Iron (est Tons) ': F76_CO2_cold_iron,
            'Total CO2E (est Tons) ': Total_CO2_used_F76,
        }
        CO2_dict['F76_CO2'] = F76_CO2_dict

        Ethanol_CO2_dict = {
            'Ethanol consumption '              :  (' '),
            'Annual Hours Underway ' : (hours_year *underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year*cold_iron),
            
            'BBL Fuel Consumed Underway (est)' : Ethanol_underway ,
            'BBL Fuel Consumed Not Underway (est)' : Ethanol_not_underway ,
            'BBL Fuel Consumed Cold Iron (est) ' : Ethanol_CO2_cold_iron ,
            'Total BBL Fuel Consumed (est)'  : round((Ethanol_underway + Ethanol_not_underway + Ethanol_cold_iron),2), 

            'CO2E underway (est Tons)': Ethanol_CO2_underway,
            'CO2E Not Underway (est Tons) ': Ethanol_CO2_not_underway,
            'CO2E Cold Iron (est Tons) ': Ethanol_CO2_cold_iron,
            'Total CO2E (est Tons) ': Total_CO2_used_Ethanol,
        }

        CO2_dict['Ethanol_CO2'] = Ethanol_CO2_dict

        LPG_CO2_dict = {
            'Liquid Petroleum gas ' :    ('  '), 
            'Annual Hours Underway ' : (hours_year *underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year*cold_iron), 

            'BBL Fuel Consumed Underway (est) ' : LPG_underway ,
            'BBL Fuel Consumed Not Underway (est) ' : LPG_not_underway,
            'BBL Fuel Consumed Cold Iron (est) ' : LPG_cold_iron ,
            'Total BBL Fuel Consumed (est) '  : round((LPG_underway + LPG_not_underway + LPG_cold_iron),2), 

            'CO2E underway (est Tons) ': LPG_CO2_underway,
            'CO2E Not Underway (est Tons) ': LPG_CO2_not_underway,
            'CO2E Cold Iron (est Tons) ': LPG_CO2_cold_iron,
            'Total CO2E (est Tons) ': Total_CO2_used_LPG,

        }

        CO2_dict['LPG_CO2'] = LPG_CO2_dict

        Menthol_CO2_dict = {
            'Menthol consumption '  : ('   '),
            'Annual Hours Underway ' : (hours_year *underway),
            'Annual Hours Not Underway ' : (hours_year * not_underway) ,
            'Annual Hours Cold Iron ' :  (hours_year*cold_iron), 

            'BBL Fuel Consumed Underway (est) ' : Menthol_underway ,
            'BBL Fuel Consumed Not Underway (est) ' : Menthol_not_underway ,
            'BBL Fuel Consumed Cold Iron (est) ' : Menthol_cold_iron,
            'Total BBL FUel Consumed (est) ' : round((Menthol_underway + Menthol_not_underway + Menthol_cold_iron),2),

            'CO2E underway (est Tons) ': Menthol_CO2_underway,
            'CO2E Not Underway (est Tons) ': Menthol_CO2_not_underway,
            'CO2E Cold Iron (est Tons) ': Menthol_CO2_cold_iron,
            'Total CO2E (est Tons) ': Total_CO2_used_Menthol,

        }

        CO2_dict['Menthol_CO2'] = Menthol_CO2_dict

        
        if fuel_type == 'F76':
            return CO2_dict['F76_CO2']

        elif fuel_type == 'Ethanol':
            return CO2_dict['Ethanol_CO2']

        elif fuel_type == 'Menthol':
            return CO2_dict['Menthol_CO2']

        elif fuel_type == 'LPG':
            return CO2_dict['LPG_CO2']

        elif fuel_type == 'All' : 
            return CO2_dict
        
        else:
            print("Invalid fuel")

        return CO2_dict

ship_name = input("Enter ship name: ")
fuel_type = input("Enter the fuel type: ")
CO2_calculations = calculate_ship_info(ship_name, fuel_type, underway=0.4, not_underway=0.5, cold_iron=0.1, mission_days =180, mission_underway =0.9, mission_notunderway=0.1)

print('Class: ', ship_name, '\nFuel: ', fuel_type) 



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