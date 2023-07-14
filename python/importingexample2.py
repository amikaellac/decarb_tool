import pandas as pd



# def calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360):
#     DAYS_PER_YEAR =365 
   
# underway = 0.9
# not_underway = 0.1
# cold_iron = 0 

# df = pd.read_csv('F76_Fuel_consumption_values.csv')
# result_dict = df.set_index('Ship names').to_dict(orient='index')  #stores all values assosiated with 

# def make_results_dict(results_dict):
#     fuel_dictionary = {}
#     # ships_dictionary = {}
#     # definition_dictionary = {}

#     if ship_name in result_dict:
#         ship_data = result_dict[ship_name]
#         fuel_dictionary[ship_name] = {}

#         x_underway = ship_data['x underway']
#         x_not_underway = ship_data['x not underway']
#         x_cold_iron = ship_data['x cold iron']
#         b = ship_data['b']
#         hours_year = 8760

#         bbl_to_co2 = 942.48
#         lbs_to_ton = 0.0005
#         ethanol_to_co2 = 532.41573
#         lpg_to_co2 = 525.9341472
#         menthol_to_co2 = 379.635564

#         ethanol_density = 0.5934
#         lpg_density = 1.0549
#         methanol_density = 0.4989

#         #F76 BBL
#         bbl_underway = round(((underway * x_underway + b) * hours_year), 2)

#         bbl_not_underway = round(((not_underway * x_not_underway + b) * hours_year), 2)

#         bbl_cold_iron = round(((cold_iron * x_cold_iron + b) * hours_year), 2) 
        
#         # BBL Ethanol
#         ethanol_underway = round((bbl_underway / ethanol_density),2)

#         ethanol_not_underway = round((bbl_not_underway / ethanol_density),2)

#         ethanol_cold_iron = round((bbl_cold_iron / ethanol_density),2)

#         #BBL LPG
#         lpg_underway = round((bbl_underway / lpg_density),2)

#         lpg_not_underway = round((bbl_not_underway / lpg_density),2)

#         lpg_cold_iron = round((bbl_cold_iron / lpg_density),2)
#         #bbl menthol
#         methanol_underway = round((bbl_underway / methanol_density),2)

#         methanol_not_underway = round((bbl_not_underway / methanol_density),2)

#         methanol_cold_iron = round((bbl_cold_iron / methanol_density),2) 


#         #Total bbl 
#         f76_total_bbl_consumed = round((bbl_underway + bbl_not_underway + bbl_cold_iron),2)
#         ethanol_total_bbl_consumed = round((ethanol_underway + ethanol_not_underway + ethanol_cold_iron),2)
#         lpg_total_bbl_consumed = round((lpg_underway + lpg_not_underway + lpg_cold_iron),2)
#         methanol_total_bbl_consumed = round((methanol_underway + methanol_not_underway + methanol_cold_iron),2)



#         #BBL to CO2 conversion for each fuel type 
#         f76_co2_underway = round(bbl_underway * bbl_to_co2 * lbs_to_ton, 2)
#         f76_co2_not_underway = round(bbl_not_underway * bbl_to_co2 * lbs_to_ton, 2)
#         f76_co2_cold_iron = round(bbl_cold_iron * bbl_to_co2 * lbs_to_ton, 2)

#         ethanol_co2_underway = round(ethanol_underway * ethanol_to_co2 * lbs_to_ton, 2)
#         ethanol_co2_not_underway = round(ethanol_not_underway * ethanol_to_co2 * lbs_to_ton, 2)
#         ethanol_co2_cold_iron = round(ethanol_cold_iron * ethanol_to_co2 * lbs_to_ton, 2)

#         lpg_co2_underway = round(lpg_underway * lpg_to_co2 * lbs_to_ton, 2)
#         lpg_co2_not_underway = round(lpg_not_underway * lpg_to_co2 * lbs_to_ton, 2)
#         lpg_co2_cold_iron = round(lpg_cold_iron * lpg_to_co2 * lbs_to_ton, 2)

#         methanol_co2_underway = round(methanol_underway * menthol_to_co2 * lbs_to_ton, 2)
#         methanol_co2_not_underway = round(methanol_not_underway * menthol_to_co2 * lbs_to_ton, 2)
#         methanol_co2_cold_iron = round(methanol_cold_iron * menthol_to_co2 * lbs_to_ton, 2)

#         total_co2_used_f76 = round(f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron, 2)
#         total_co2_used_ethanol = round(ethanol_co2_underway + ethanol_co2_not_underway + ethanol_co2_cold_iron, 2)
#         total_co2_used_lpg = round(lpg_co2_underway + lpg_co2_not_underway + lpg_co2_cold_iron, 2)
#         total_co2_used_menthol = round(methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron, 2)

#         #NEED TO ADD MISSION CALCULATIONS --> in co2_calculator 
        

#       #   fuel_dictionary = {
#       #   'F76' : 'F-76 Military Diesel',
#       #   'Ethanol' : 'Ethanol Fuel',
#       #   'LPG' : 'Liquid Petroleum Gas',
#       #   'Methanol' : 'Methanol Fuel',
#       # }

 

#         # ships_dictionary = {
#         # 'LHA-6CL' : 'USS America: amphibious assault ship', 
#         # 'LPD-17CL' : 'San Antonio class: amphibious transport docks / "landing platform, dock" (LPD)',
#         # 'CG-47CL' : 'USS Ticonderoga: guided-missile cruiser', 
#         # 'MCM-1CL' : 'Avenger class: mine counter measures ships', 
#         # 'DDG-51CL' : 'Arleigh Burke class: guided missile destroyers', 
#         # 'LSD-41CL' : 'Whidbey Island-class: dock landing ship', 
#         # 'LHD-1CL' : 'USS Wasp: multipurpose amphibious assault ship', 
#         # 'LCS-1CL' : 'Freedom-class littoral combat ship', 
#         # 'LCC-19CL' : 'Blue Ridge-class amphibious command ships', 
#         # 'FFG-7CL' : 'Oliver Hazard Perry-class: guided-missile frigate', 
#         # 'LCS-2CL' : 'Littoral combat ship surface vessels', 
#         # 'LPD-4CL' : 'Amphibious transport dock', 
#         # 'DDG-1000CL' : 'USS Zumwalt: guided missile destroyer', 
#         # 'LHA-1CL' : 'Landing helicopter assault', 
#         # 'LSD-49CL' : 'USS Harpers Ferry: landing ship dock',

#       # }

 

#         results_dictionary = {
#             #for f76 fuel_type
#             'f76_bbl_underway' : bbl_underway,
#             'f76_bbl_not_underway' :  bbl_not_underway,
#             'f76_bbl_cold_iron' :  bbl_cold_iron,
#             'f76_total_bbl_consumed' : f76_total_bbl_consumed,
#             'f76_co2_underway' : f76_co2_underway,
#             'f76_co2_not_underway' : f76_co2_not_underway,
#             'f76_co2_cold_iron' : f76_co2_cold_iron,
#             'f76_total_co2_used' : total_co2_used_f76,

#             #for ethanol
#             'ethanol_underway' : ethanol_underway,
#             'ethanol_not_underway' : ethanol_not_underway,
#             'ethanol_cold_iron' : ethanol_cold_iron,
#             'ethanol_total_bbl_consumed' : ethanol_total_bbl_consumed,
#             'ethanol_co2_underway' : ethanol_co2_underway,
#             'ethanol_co2_not_underway' : ethanol_co2_not_underway,
#             'ethanol_co2_cold_iron' : ethanol_co2_cold_iron,
#             'ethanol_total_co2_used' : total_co2_used_ethanol,

#             #for lpg
#             'lpg_underway' : lpg_underway,
#             'lpg_not_underway' : lpg_not_underway,
#             'lpg_cold_iron' : lpg_cold_iron,
#             'lpg_total_bbl_consumed' : lpg_total_bbl_consumed,
#             'lpg_co2_underway' : lpg_co2_underway,
#             'lpg_co2_not_underway' : lpg_co2_not_underway,
#             'lpg_co2_cold_iron' : lpg_co2_cold_iron,
#             'lpg_total_co2_used' : total_co2_used_lpg,

#             #for methanol
#             'methanol_underway' : methanol_underway,
#             'methanol_not_underway' : methanol_not_underway,
#             'methanol_cold_iron' : methanol_cold_iron,
#             'methanol_total_bbl_consumed' : methanol_total_bbl_consumed,
#             'methanol_co2_underway' : methanol_co2_underway,
#             'methanol_co2_not_underway' : methanol_co2_not_underway,
#             'methanol_co2_cold_iron' : methanol_co2_cold_iron,
#             'methanol_total_co2_used' : total_co2_used_menthol,
#           }

 

#         # #description dictionary
#         # definition_dictionary  = {
#         #   #For military diesel
#         #   'f76_bbl_underway' : 'BBL Fuel Consumed Underway (est):',
#         #   'f76_bbl_not_underway' : 'BBL Fuel Consumed Not Underway (est):',
#         #   'f76_bbl_cold_iron' : 'BBL Fuel Consumed Cold Iron (est):',
#         #   'f76_total_bbl_consumed' : '\tTotal BBL Fuel Consumed (est):',
#         #   'f76_co2_underway' : 'CO2E Underway (est Tons):',
#         #   'f76_co2_not_underway' : 'CO2E Not underway (est Tons):',
#         #   'f76_co2_cold_iron' : 'CO2E Cold Iron (est Tons):',
#         #   'f76_total_co2_used' : '\tTotal CO2E (est Tons):',
#         #   #For ethanol
#         #   'ethanol_underway' : 'BBL Fuel Consumed Underway (est):',
#         #   'ethanol_not_underway' : 'BBL Fuel Consumed Not Underway (est):',
#         #   'ethanol_cold_iron': 'BBL Fuel Consumed Cold Iron (est):',
#         #   'ethanol_total_bbl_consumed' : '\tTotal BBL Fuel Consumed (est):',
#         #   'ethanol_co2_underway' : 'CO2E underway (est Tons):',
#         #   'ethanol_co2_not_underway' : 'CO2E Not Underway (est Tons):',
#         #   'ethanol_co2_cold_iron' : 'CO2E Cold Iron (est Tons):',
#         #   'ethanol_total_co2_used' : '\tTotal CO2E (est Tons):',
#         #   #for LPG
#         #   'lpg_underway' : 'BBL Fuel Consumed Underway (est):',
#         #   'lpg_not_underway' : 'BBL Fuel Consumed Not Underway (est):',
#         #   'lpg_cold_iron' : 'BBL Fuel Consumed Cold Iron (est):',
#         #   'lpg_total_bbl_consumed' : '\tTotal BBL Fuel Consumed (est):',
#         #   'lpg_co2_underway' : 'CO2E underway (est Tons):',
#         #   'lpg_co2_not_underway' : 'CO2E Not Underway (est Tons) ',
#         #   'lpg_co2_cold_iron' : 'CO2E Cold Iron (est Tons):',
#         #   'lpg_total_co2_used' : '\tTotal CO2E (est Tons):',
#         #   #for methanol
#         #   'methanol_underway' : 'BBL Fuel Consumed Underway (est):',
#         #   'methanol_not_underway' : 'BBL Fuel Consumed Not Underway (est):',
#         #   'methanol_cold_iron' : 'BBL Fuel Consumed Cold Iron (est):',
#         #   'methanol_total_bbl_consumed' : '\tTotal BBL Fuel Consumed (est):',
#         #   'methanol_co2_underway' : 'CO2E underway (est Tons):',
#         #   'methanol_co2_not_underway' : 'CO2E Not Underway (est Tons):',
#         #   'methanol_co2_cold_iron' : 'CO2E Cold Iron (est Tons):',
#         #   'methanol_total_co2_used' : '\tTotal CO2E (est Tons):',
#         #   }
      
          
    
#     # return results_dictionary, definition_dictionary, ships_dictionary
#     return results_dictionary

# ship_name = 'LHA-6CL' #input("Enter ship name: ")
# fuel_type = 'Methanol' #input("Enter the fuel type: ")


# make_results_dict['f76'] = calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360)



# import pandas as pd

# def calculate_ship_info(ship_name, fuel_type):
#     DAYS_PER_YEAR = 365

#     underway = 0.9
#     not_underway = 0.1
#     cold_iron = 0
#     mission_days=360
    
#     df = pd.read_csv('F76_Fuel_consumption_values.csv')
#     result_dict = df.set_index('Ship names').to_dict(orient='index')  # stores all values associated with

#     def make_results_dict(results_dict):
#         fuel_dictionary = {}
#         # ships_dictionary = {}
#         # definition_dictionary = {}

#         if ship_name in result_dict:
#             ship_data = result_dict[ship_name]
#             fuel_dictionary[ship_name] = {}

#             x_underway = ship_data['x underway']
#             x_not_underway = ship_data['x not underway']
#             x_cold_iron = ship_data['x cold iron']
#             b = ship_data['b']
#             hours_year = 8760

#             bbl_to_co2 = 942.48
#             lbs_to_ton = 0.0005
#             ethanol_to_co2 = 532.41573
#             lpg_to_co2 = 525.9341472
#             menthol_to_co2 = 379.635564

#             ethanol_density = 0.5934
#             lpg_density = 1.0549
#             methanol_density = 0.4989

#             # F76 BBL
#             bbl_underway = round(((underway * x_underway + b) * hours_year), 2)

#             bbl_not_underway = round(((not_underway * x_not_underway + b) * hours_year), 2)

#             bbl_cold_iron = round(((cold_iron * x_cold_iron + b) * hours_year), 2)

#             # BBL Ethanol
#             ethanol_underway = round((bbl_underway / ethanol_density), 2)

#             ethanol_not_underway = round((bbl_not_underway / ethanol_density), 2)

#             ethanol_cold_iron = round((bbl_cold_iron / ethanol_density), 2)

#             # BBL LPG
#             lpg_underway = round((bbl_underway / lpg_density), 2)

#             lpg_not_underway = round((bbl_not_underway / lpg_density), 2)

#             lpg_cold_iron = round((bbl_cold_iron / lpg_density), 2)
#             # bbl menthol
#             methanol_underway = round((bbl_underway / methanol_density), 2)

#             methanol_not_underway = round((bbl_not_underway / methanol_density), 2)

#             methanol_cold_iron = round((bbl_cold_iron / methanol_density), 2)

#             # Total bbl
#             f76_total_bbl_consumed = round((bbl_underway + bbl_not_underway + bbl_cold_iron), 2)
#             ethanol_total_bbl_consumed = round((ethanol_underway + ethanol_not_underway + ethanol_cold_iron), 2)
#             lpg_total_bbl_consumed = round((lpg_underway + lpg_not_underway + lpg_cold_iron), 2)
#             methanol_total_bbl_consumed = round((methanol_underway + methanol_not_underway + methanol_cold_iron),2)

#             # BBL to CO2 conversion for each fuel type
#             f76_co2_underway = round(bbl_underway * bbl_to_co2 * lbs_to_ton, 2)
#             f76_co2_not_underway = round(bbl_not_underway * bbl_to_co2 * lbs_to_ton, 2)
#             f76_co2_cold_iron = round(bbl_cold_iron * bbl_to_co2 * lbs_to_ton, 2)

#             ethanol_co2_underway = round(ethanol_underway * ethanol_to_co2 * lbs_to_ton, 2)
#             ethanol_co2_not_underway = round(ethanol_not_underway * ethanol_to_co2 * lbs_to_ton, 2)
#             ethanol_co2_cold_iron = round(ethanol_cold_iron * ethanol_to_co2 * lbs_to_ton, 2)

#             lpg_co2_underway = round(lpg_underway * lpg_to_co2 * lbs_to_ton, 2)
#             lpg_co2_not_underway = round(lpg_not_underway * lpg_to_co2 * lbs_to_ton, 2)
#             lpg_co2_cold_iron = round(lpg_cold_iron * lpg_to_co2 * lbs_to_ton, 2)

#             methanol_co2_underway = round(methanol_underway * menthol_to_co2 * lbs_to_ton, 2)
#             methanol_co2_not_underway = round(methanol_not_underway * menthol_to_co2 * lbs_to_ton, 2)
#             methanol_co2_cold_iron = round(methanol_cold_iron * menthol_to_co2 * lbs_to_ton, 2)

#             total_co2_used_f76 = round(f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron, 2)
#             total_co2_used_ethanol = round(ethanol_co2_underway + ethanol_co2_not_underway + ethanol_co2_cold_iron, 2)
#             total_co2_used_lpg = round(lpg_co2_underway + lpg_co2_not_underway + lpg_co2_cold_iron, 2)
#             total_co2_used_menthol = round(methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron, 2)

#             # NEED TO ADD MISSION CALCULATIONS --> in co2_calculator

#             fuel_dictionary['F76'] = f76_d
#             fuel_dictionary['Ethanol'] = ethanol_d
#             fuel_dictionary['LPG'] = lpg_d 
#             fuel_dictionary['Methanol'] = methanol_d


#             f76_d ={
#              # for f76 fuel_type
#               'f76_bbl_underway': bbl_underway,
#               'f76_bbl_not_underway': bbl_not_underway,
#               'f76_bbl_cold_iron': bbl_cold_iron,
#               'f76_total_bbl_consumed': f76_total_bbl_consumed,
#               'f76_co2_underway': f76_co2_underway,
#               'f76_co2_not_underway': f76_co2_not_underway,
#               'f76_co2_cold_iron': f76_co2_cold_iron,
#               'f76_total_co2_used': total_co2_used_f76,
#                 }

#             ethanol_d = {
#                 # for ethanol
#                 'ethanol_underway': ethanol_underway,
#                 'ethanol_not_underway': ethanol_not_underway,
#                 'ethanol_cold_iron': ethanol_cold_iron,
#                 'ethanol_total_bbl_consumed': ethanol_total_bbl_consumed,
#                 'ethanol_co2_underway': ethanol_co2_underway,
#                 'ethanol_co2_not_underway': ethanol_co2_not_underway,
#                 'ethanol_co2_cold_iron': ethanol_co2_cold_iron,
#                 'ethanol_total_co2_used': total_co2_used_ethanol,
#                  }
#             lpg_d = {
#                 # for lpg
#                 'lpg_underway': lpg_underway,
#                 'lpg_not_underway': lpg_not_underway,
#                 'lpg_cold_iron': lpg_cold_iron,
#                 'lpg_total_bbl_consumed': lpg_total_bbl_consumed,
#                 'lpg_co2_underway': lpg_co2_underway,
#                 'lpg_co2_not_underway': lpg_co2_not_underway,
#                 'lpg_co2_cold_iron': lpg_co2_cold_iron,
#                 'lpg_total_co2_used': total_co2_used_lpg,
#               }

#             methanol_d = {
#                 # for methanol
#                 'methanol_underway': methanol_underway,
#                 'methanol_not_underway': methanol_not_underway,
#                 'methanol_cold_iron': methanol_cold_iron,
#                 'methanol_total_bbl_consumed': methanol_total_bbl_consumed,
#                 'methanol_co2_underway': methanol_co2_underway,
#                 'methanol_co2_not_underway': methanol_co2_not_underway,
#                 'methanol_co2_cold_iron': methanol_co2_cold_iron,
#                 'methanol_total_co2_used': total_co2_used_menthol,
            
#               } 
            
           

#             return fuel_dictionary
        
#         results = make_results_dict(fuel_type)

#     ship_name = 'LHA-6CL'  # input("Enter ship name: ")
#     fuel_type = 'Methanol'  # input("Enter the fuel type: ")

#     results = calculate_ship_info(ship_name, fuel_type)
#     print(results)



# import pandas as pd

# def calculate_ship_info(ship_name, fuel_type):
#     DAYS_PER_YEAR = 365

#     underway = 0.9
#     not_underway = 0.1
#     cold_iron = 0
#     mission_days = 360
    
#     df = pd.read_csv('F76_Fuel_consumption_values.csv')
#     result_dict = df.set_index('Ship names').to_dict(orient='index')
   

#     def make_results_dict(result_dict):
#         fuel_dictionary = {}

#         if ship_name in result_dict:
#             ship_data = result_dict[ship_name]
#             fuel_dictionary[ship_name] = {}

#             x_underway = ship_data['x underway']
#             x_not_underway = ship_data['x not underway']
#             x_cold_iron = ship_data['x cold iron']
#             b = ship_data['b']
#             hours_year = 8760

#             bbl_to_co2 = 942.48
#             lbs_to_ton = 0.0005
#             ethanol_to_co2 = 532.41573
#             lpg_to_co2 = 525.9341472
#             menthol_to_co2 = 379.635564

#             ethanol_density = 0.5934
#             lpg_density = 1.0549
#             methanol_density = 0.4989

#             # F76 BBL
#             bbl_underway = round(((underway * x_underway + b) * hours_year), 2)
#             bbl_not_underway = round(((not_underway * x_not_underway + b) * hours_year), 2)
#             bbl_cold_iron = round(((cold_iron * x_cold_iron + b) * hours_year), 2)

#             # BBL Ethanol
#             ethanol_underway = round((bbl_underway / ethanol_density), 2)
#             ethanol_not_underway = round((bbl_not_underway / ethanol_density), 2)
#             ethanol_cold_iron = round((bbl_cold_iron / ethanol_density), 2)

#             # BBL LPG
#             lpg_underway = round((bbl_underway / lpg_density), 2)
#             lpg_not_underway = round((bbl_not_underway / lpg_density), 2)
#             lpg_cold_iron = round((bbl_cold_iron / lpg_density), 2)

#             # BBL Methanol
#             methanol_underway = round((bbl_underway / methanol_density), 2)
#             methanol_not_underway = round((bbl_not_underway / methanol_density), 2)
#             methanol_cold_iron = round((bbl_cold_iron / methanol_density), 2)

#             # Total bbl
#             f76_total_bbl_consumed = round((bbl_underway + bbl_not_underway + bbl_cold_iron), 2)
#             ethanol_total_bbl_consumed = round((ethanol_underway + ethanol_not_underway + ethanol_cold_iron), 2)
#             lpg_total_bbl_consumed = round((lpg_underway + lpg_not_underway + lpg_cold_iron), 2)
#             methanol_total_bbl_consumed = round((methanol_underway + methanol_not_underway + methanol_cold_iron), 2)

#             # BBL to CO2 conversion for each fuel type
#             f76_co2_underway = round(bbl_underway * bbl_to_co2 * lbs_to_ton, 2)
#             f76_co2_not_underway = round(bbl_not_underway * bbl_to_co2 * lbs_to_ton, 2)
#             f76_co2_cold_iron = round(bbl_cold_iron * bbl_to_co2 * lbs_to_ton, 2)

#             ethanol_co2_underway = round(ethanol_underway * ethanol_to_co2 * lbs_to_ton, 2)
#             ethanol_co2_not_underway = round(ethanol_not_underway * ethanol_to_co2 * lbs_to_ton, 2)
#             ethanol_co2_cold_iron = round(ethanol_cold_iron * ethanol_to_co2 * lbs_to_ton, 2)

#             lpg_co2_underway = round(lpg_underway * lpg_to_co2 * lbs_to_ton, 2)
#             lpg_co2_not_underway = round(lpg_not_underway * lpg_to_co2 * lbs_to_ton, 2)
#             lpg_co2_cold_iron = round(lpg_cold_iron * lpg_to_co2 * lbs_to_ton, 2)

#             methanol_co2_underway = round(methanol_underway * menthol_to_co2 * lbs_to_ton, 2)
#             methanol_co2_not_underway = round(methanol_not_underway * menthol_to_co2 * lbs_to_ton, 2)
#             methanol_co2_cold_iron = round(methanol_cold_iron * menthol_to_co2 * lbs_to_ton, 2)

#             total_co2_used_f76 = round(f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron, 2)
#             total_co2_used_ethanol = round(ethanol_co2_underway + ethanol_co2_not_underway + ethanol_co2_cold_iron, 2)
#             total_co2_used_lpg = round(lpg_co2_underway + lpg_co2_not_underway + lpg_co2_cold_iron, 2)
#             total_co2_used_methanol = round(methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron, 2)

#             fuel_dictionary['F76'] = {
#                 'bbl_underway': bbl_underway,
#                 'bbl_not_underway': bbl_not_underway,
#                 'bbl_cold_iron': bbl_cold_iron,
#                 'total_bbl_consumed': f76_total_bbl_consumed,
#                 'co2_underway': f76_co2_underway,
#                 'co2_not_underway': f76_co2_not_underway,
#                 'co2_cold_iron': f76_co2_cold_iron,
#                 'total_co2_used': total_co2_used_f76
#             }

#             fuel_dictionary['Ethanol'] = {
#                 'underway': ethanol_underway,
#                 'not_underway': ethanol_not_underway,
#                 'cold_iron': ethanol_cold_iron,
#                 'total_bbl_consumed': ethanol_total_bbl_consumed,
#                 'co2_underway': ethanol_co2_underway,
#                 'co2_not_underway': ethanol_co2_not_underway,
#                 'co2_cold_iron': ethanol_co2_cold_iron,
#                 'total_co2_used': total_co2_used_ethanol
#             }

#             fuel_dictionary['LPG'] = {
#                 'underway': lpg_underway,
#                 'not_underway': lpg_not_underway,
#                 'cold_iron': lpg_cold_iron,
#                 'total_bbl_consumed': lpg_total_bbl_consumed,
#                 'co2_underway': lpg_co2_underway,
#                 'co2_not_underway': lpg_co2_not_underway,
#                 'co2_cold_iron': lpg_co2_cold_iron,
#                 'total_co2_used': total_co2_used_lpg
#             }

#             fuel_dictionary['Methanol'] = {
#                 'underway': methanol_underway,
#                 'not_underway': methanol_not_underway,
#                 'cold_iron': methanol_cold_iron,
#                 'total_bbl_consumed': methanol_total_bbl_consumed,
#                 'co2_underway': methanol_co2_underway,
#                 'co2_not_underway': methanol_co2_not_underway,
#                 'co2_cold_iron': methanol_co2_cold_iron,
#                 'total_co2_used': total_co2_used_methanol
#             }

#             return fuel_dictionary
#     results = make_results_dict()



# ship_name = 'LHA-6CL'  # input("Enter ship name: ")
# fuel_type = 'Methanol'  # input("Enter the fuel type: ")

# calculate_ship_info(ship_name, fuel_type)

ship_name = 'LHA-6CL'  # input("Enter ship name: ")
fuel_type = 'F76'  # input("Enter the fuel type: ")

df = pd.read_csv('F76_Fuel_consumption_values.csv')

result_dict = df.set_index(ship_name).to_dict(orient='index')
# result_dict = df.set_index('Ship names').to_dict(orient='index')
   

def make_results_dict(ship_name, fuel_type):
  fuel_dictionary = {}
  underway = 0.9
  not_underway = 0.1
  cold_iron = 0

  if ship_name in result_dict:
      ship_data = result_dict[ship_name]
      fuel_dictionary[ship_name] = {}

      x_underway = ship_data['x underway']
      x_not_underway = ship_data['x not underway']
      x_cold_iron = ship_data['x cold iron']
      b = ship_data['b']
      hours_year = 8760

      bbl_to_co2 = 942.48
      lbs_to_ton = 0.0005
      ethanol_to_co2 = 532.41573
      lpg_to_co2 = 525.9341472
      menthol_to_co2 = 379.635564

      f76_density= 1
      ethanol_density = 0.5934
      lpg_density = 1.0549
      methanol_density = 0.4989
      

      # F76 BBL 
      bbl_underway = round(((underway * x_underway + b) * hours_year)/f76_density, 2)
      bbl_not_underway = round(((not_underway * x_not_underway + b) * hours_year), 2)
      bbl_cold_iron = round(((cold_iron * x_cold_iron + b) * hours_year), 2)
      f76_total_bbl_consumed = round((bbl_underway + bbl_not_underway + bbl_cold_iron), 2)
       # BBL to CO2 conversion for each fuel type
      f76_co2_underway = round(bbl_underway * bbl_to_co2 * lbs_to_ton, 2)
      f76_co2_not_underway = round(bbl_not_underway * bbl_to_co2 * lbs_to_ton, 2)
      f76_co2_cold_iron = round(bbl_cold_iron * bbl_to_co2 * lbs_to_ton, 2)
      total_co2_used_f76 = round(f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron, 2)

      fuel_dictionary['F76'] = {
                'bbl_underway': bbl_underway,
                'bbl_not_underway': bbl_not_underway,
                'bbl_cold_iron': bbl_cold_iron,
                'total_bbl_consumed': f76_total_bbl_consumed,
                'co2_underway': f76_co2_underway,
                'co2_not_underway': f76_co2_not_underway,
                'co2_cold_iron': f76_co2_cold_iron,
                'total_co2_used': total_co2_used_f76
            }

       # Ethanol BBL
      ethanol_underway = round((bbl_underway / ethanol_density), 2)
      ethanol_not_underway = round((bbl_not_underway / ethanol_density), 2)
      ethanol_cold_iron = round((bbl_cold_iron / ethanol_density), 2)

        # LPG BBL 
      lpg_underway = round((bbl_underway / lpg_density), 2)
      lpg_not_underway = round((bbl_not_underway / lpg_density), 2)
      lpg_cold_iron = round((bbl_cold_iron / lpg_density), 2)

      # Methanol BBL 
      methanol_underway = round((bbl_underway / methanol_density), 2)
      methanol_not_underway = round((bbl_not_underway / methanol_density), 2)
      methanol_cold_iron = round((bbl_cold_iron / methanol_density), 2)

      # Total bbl
      f76_total_bbl_consumed = round((bbl_underway + bbl_not_underway + bbl_cold_iron), 2)
      ethanol_total_bbl_consumed = round((ethanol_underway + ethanol_not_underway + ethanol_cold_iron), 2)
      lpg_total_bbl_consumed = round((lpg_underway + lpg_not_underway + lpg_cold_iron), 2)
      methanol_total_bbl_consumed = round((methanol_underway + methanol_not_underway + methanol_cold_iron), 2)

      # BBL to CO2 conversion for each fuel type
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
      total_co2_used_methanol = round(methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron, 2)

      fuel_dictionary['F76'] = {
                'bbl_underway': bbl_underway,
                'bbl_not_underway': bbl_not_underway,
                'bbl_cold_iron': bbl_cold_iron,
                'total_bbl_consumed': f76_total_bbl_consumed,
                'co2_underway': f76_co2_underway,
                'co2_not_underway': f76_co2_not_underway,
                'co2_cold_iron': f76_co2_cold_iron,
                'total_co2_used': total_co2_used_f76
            }

      fuel_dictionary['Ethanol'] = {
                'underway': ethanol_underway,
                'not_underway': ethanol_not_underway,
                'cold_iron': ethanol_cold_iron,
                'total_bbl_consumed': ethanol_total_bbl_consumed,
                'co2_underway': ethanol_co2_underway,
                'co2_not_underway': ethanol_co2_not_underway,
                'co2_cold_iron': ethanol_co2_cold_iron,
                'total_co2_used': total_co2_used_ethanol
            }

      fuel_dictionary['LPG'] = {
                'underway': lpg_underway,
                'not_underway': lpg_not_underway,
                'cold_iron': lpg_cold_iron,
                'total_bbl_consumed': lpg_total_bbl_consumed,
                'co2_underway': lpg_co2_underway,
                'co2_not_underway': lpg_co2_not_underway,
                'co2_cold_iron': lpg_co2_cold_iron,
                'total_co2_used': total_co2_used_lpg
            }

      fuel_dictionary['Methanol'] = {
                'underway': methanol_underway,
                'not_underway': methanol_not_underway,
                'cold_iron': methanol_cold_iron,
                'total_bbl_consumed': methanol_total_bbl_consumed,
                'co2_underway': methanol_co2_underway,
                'co2_not_underway': methanol_co2_not_underway,
                'co2_cold_iron': methanol_co2_cold_iron,
                'total_co2_used': total_co2_used_methanol
            }

  return fuel_dictionary


results = make_results_dict( result_dict)

print(results)