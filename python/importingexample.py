
import pandas as pd

# def calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360):
#     DAYS_PER_YEAR =365 

#     df = pd.read_csv('F76_fuel_consumption_values.csv')
#     values = df.set_index(ship_name).to_dict(orient='index')
            
#     fuel_density = {                                           #maps fuel types to densities 
#         'f76_density' : 1,
#         'ethanol_density' : 0.5934,
#         'lpg_density' : 1.0549,
#         'methanol_density' : 0.4989
    
#     }
#     bbl_to_co2 = {
#         'f76_to_co2' : 942.48,
     
#         'ethanol_to_co2' : 532.41573,

#         'lpg_to_co2' : 525.9341472,

#         'menthol_to_co2' : 379.635564,

#     }

#     ship_results= {} # will store calculated fuel consumption 

#     if ship_name in values: 
#         ship_data = values[ship_name]                       #retrives values associated with the ship name(x underway, x not underway ...)

#         for fuel_type, density in fuel_density.items():         #iterates over the items in fuel_density dictionary and assigning fuel type and desnity to variables fuel_type and density 
#             ship_results[ship_name][fuel_type] = make_results_dict(density, **ship_data[ship_name])

        
#             x_underway = ship_data['x underway']
#             x_not_underway = ship_data['x not underway']
#             x_cold_iron = ship_data['x cold iron']
#             b = ship_data['b']
#             hours_year = 8760
            
#             bbl_to_co2 = 942.48
#             lbs_to_ton = 0.0005

#     return ship_results 


# ship_name ='LHA-6CL' #input("Enter ship name: ")
# fuel_type = 'Methanol' #input("Enter the fuel type: ")
# info = calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360) 

# def make_results_dict(density = 0, underway =0, not_underway=0, cold_iron =0,b=0,best_case=0, worst_case=0,x_underway =0, x_not_underway=0, x_cold_iron =0, hours_year=8760,bbl_to_co2 =0, lbs_to_ton=0):


#     results= {
#         'bbl_underway': round((((underway * x_underway + b) * hours_year)/density), 2),

#         'bbl_not_underway':round(((not_underway * x_not_underway + b) * hours_year)/density, 2),

#         'bbl_cold_iron': round(((cold_iron * x_cold_iron + b) * hours_year)/density, 2),

#         'total_bbl_consumed': round((((underway * x_underway + b) * hours_year)/density) + (((not_underway * x_not_underway + b) * hours_year)/density) + (((cold_iron * x_cold_iron + b) * hours_year)/density),2),

#         'co2_underway': round(((((underway * x_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton),2),

#         'co2_not_underway': round(((((not_underway * x_not_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton),2),

#         'co2_cold_iron': round(((((cold_iron * x_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton),2),

#         'total_co2_used': round((((((underway * x_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton) + ((((not_underway * x_not_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton) + ((((cold_iron * x_underway + b) * hours_year)/density) * bbl_to_co2 * lbs_to_ton)),2)
        
#         }

    
#     return results
    

# def make_results_dict(density,conversion, underway, not_underway, cold_iron,b,optimum,worst,x_underway, x_not_underway, x_cold_iron, hours_year=8760, lbs_to_ton=0.0005):


#         results= {
#             'bbl_underway': round((((underway * x_underway + b) * hours_year)/density), 2),

#             'bbl_not_underway':round(((not_underway * x_not_underway + b) * hours_year)/density, 2),

#             'bbl_cold_iron': round(((cold_iron * x_cold_iron + b) * hours_year)/density, 2),

#             'total_bbl_consumed': round((((underway * x_underway + b) * hours_year)/density) + (((not_underway * x_not_underway + b) * hours_year)/density) + (((cold_iron * x_cold_iron + b) * hours_year)/density),2),

#             'co2_underway': round(((((underway * x_underway + b) * hours_year)/density) * conversion * lbs_to_ton),2),

#             'co2_not_underway': round(((((not_underway * x_not_underway + b) * hours_year)/density) * conversion * lbs_to_ton),2),

#             'co2_cold_iron': round(((((cold_iron * x_underway + b) * hours_year)/density) * conversion * lbs_to_ton),2),

#             'total_co2_used': round((((((underway * x_underway + b) * hours_year)/density) * conversion * lbs_to_ton) + ((((not_underway * x_not_underway + b) * hours_year)/density) * conversion * lbs_to_ton) + ((((cold_iron * x_underway + b) * hours_year)/density) * conversion * lbs_to_ton)),2)
            
#             }
#         return results 




# def calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360):
#     # DAYS_PER_YEAR =365 
#     hours_year = 8760
#     lbs_to_ton = 0.0005


#     df = pd.read_csv('F76_fuel_consumption_values.csv')


#     values_dict = df.set_index('Ship Names').to_dict(orient='index')

#     fuel_density = {                                           #maps fuel types to densities 
#             'f76_density' : 1,
#             'ethanol_density' : 0.5934,
#             'lpg_density' : 1.0549,
#             'methanol_density' : 0.4989
        
#         }

#     bbl_to_co2 = {
#             'f76_to_co2' : 942.48,
        
#             'ethanol_to_co2' : 532.41573,

#             'lpg_to_co2' : 525.9341472,

#             'menthol_to_co2' : 379.635564,
#         }


#     density = fuel_density.get(fuel_type + "_density") 
#     conversion = bbl_to_co2.get(fuel_type + "_to_co2")
#     # print(density)
#     # print(conversion) 
   
#     # ship_results ={} 
#     # ship_results[ship_name]={}
#     # if ship_name in values_dict:
#     #     ship_data =values_dict[ship_name]
        
#         # ship_results[ship_name][fuel_type] = make_results_dict(density,conversion, **ship_data[ship_name])

#         # x_underway = ship_data['x underway']
#         # x_not_underway = ship_data['x not underway']
#         # x_cold_iron = ship_data['x cold iron']
#         # b = ship_data['b']
#         # Op= ship_data['optimum']
#         # worst= ship_data['worst']



#     results ={}
#     results[ship_name] ={}

#     if ship_name in values_dict: 
#         ship_data=values_dict[ship_name]
    
#         results[ship_name][fuel_type]={}
#         print(ship_name)


#         results[ship_name][fuel_type] = make_results_dict(density,conversion, **ship_data[ship_name])

#     return results[ship_name][fuel_type]

#     # for fuel, density in fuel_density.items():                            # this code iterates the (fuel_desity) dictionary. 
#     #     if fuel == (fuel_type + "_density" ):
#     #         density 

#     # density_value = density

#     # for fuel, conversion in bbl_to_co2.items():
#     #     if fuel == (fuel_type +"to_co2"): 
#     #         conversion

# shipinfo = calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =360) 

# print(shipinfo)

import pandas as pd 

ship_name = "LHA-6CL"
fuel_type = "all"

df = pd.read_csv("F76_fuel_consumption_values.csv")

def make_results_dict(density=0, conversion=0, underway=0, not_underway=0, cold_iron=0, optimum=0, worst=0, x_underway=0, b_underway=0, x_not_underway=0, b_not_underway=0, x_cold_iron=0, b_cold_iron=0, mission_days=0,DAYS_PER_YEAR=365,hours_year=8760,lbs_to_ton=0.0005):
    results= {
        'bbl_underway': round((((underway * x_underway + b_underway) * hours_year)/density), 2),

        'bbl_not_underway':round(((not_underway * x_not_underway + b_not_underway) * hours_year)/density, 2),
                 
                 
        'bbl_cold_iron': round(((cold_iron * x_cold_iron + b_cold_iron) * hours_year)/density, 2),

        'total_bbl_consumed': round((((underway * x_underway + b_underway) * hours_year)/density) + (((not_underway * x_not_underway + b_not_underway) * hours_year)/density) + (((cold_iron * x_cold_iron + b_cold_iron) * hours_year)/density),2),

        'co2_underway': round(((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton),2),

        'co2_not_underway': round(((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton),2),

        'co2_cold_iron': round(((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton),2),

        'total_co2_used': round((((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton)),2),
                
        'optimum_range': round(((((underway * x_underway + b_underway) * hours_year)/density) * optimum ),2),

        'worst_range' : round(((((underway * x_underway + b_underway) * hours_year)/density)* worst),2),

        'optimum_co2' : round(((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton)/((((underway * x_underway + b_underway) * hours_year)/density) * optimum ),9),

        'worst_co2':round(((((underway * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton) / ((((underway * x_underway + b_underway) * hours_year)/density)* worst),9),
            
        'co2_mission ' : round(((((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton))) * (mission_days/DAYS_PER_YEAR),2)
            }
    
    return results


def calculate_ship_info(ship_name, fuel_type, underway, not_underway, cold_iron, mission_days):

    df = pd.read_csv("F76_fuel_consumption_values.csv")

    values_dict = df.set_index('ship_names').to_dict(orient='index')
    
    fuel_density = {                                           #maps fuel types to densities 
            'f76' : 1,
            'ethanol' : 0.5934,
            'lpg' : 1.0549,
            'methanol' : 0.4989
        }
    
    bbl_to_co2 = {
            'f76' : 942.48,
        
            'ethanol' : 532.41573,

            'lpg' : 525.9341472,

            'methanol' : 379.635564,

        }

    ship_results ={}                           
    ship_results[ship_name] ={}         #ship_results[ship_name] = {ship_name : {} }

    if ship_name in values_dict: 
        ship_data=values_dict[ship_name]

        for fuel, density in fuel_density.items():       
            #density = fuel_density.get(fuel_type,0) 
            conversion = bbl_to_co2.get(fuel,0)
            
            ship_results[ship_name][fuel]={}       ##ship_results[ship_name][fuel_type] = {ship_name : {fuel_type : {} } }
            #results[ship_name][fuel_type] = make_results_dict(density, conversion, underway,not_underway,cold_iron,optimum,worst,x_underway,b_underway, x_not_underway, b_not_underway, x_cold_iron, b_cold_iron, mission_days,DAYS_PER_YEAR=365,hours_year=8760,lbs_to_ton=0.0005)
            ship_results[ship_name][fuel]=make_results_dict(density,conversion,underway,not_underway,cold_iron,**ship_data)
            

            # print(conversion)
            
    if fuel_type in fuel_density: 
        return ship_results[ship_name][fuel_type]

    else: 
        return ship_results

    return ship_results[ship_name][fuel_type]


shipcalc = calculate_ship_info(ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days =365)

print("class :" , ship_name, "fuel: ", fuel_type)

print(shipcalc)

