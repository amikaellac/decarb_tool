# Andres Zamudio Bucio
# andres.zamudiobucio@nps.edu
# 07/05/2023
import pandas as pd

ship_name = "LHA-6CL"
fuel_type = "All"

# df = pd.read_csv("F76_fuel_consumption_values.csv")


def make_results_dict(density=0, conversion=0, underway=0, not_underway=0, cold_iron=0, optimum=0, worst=0, x_underway=0, b_underway=0,
                      x_not_underway=0, b_not_underway=0, x_cold_iron=0, b_cold_iron=0, mission_days=365, DAYS_PER_YEAR=365, hours_year=8760, lbs_to_ton=0.0005):
    results = {
        'bbl_underway': round((((underway * x_underway + b_underway) * hours_year)/density), 2),

        'bbl_not_underway': round(((not_underway * x_not_underway + b_not_underway) * hours_year)/density, 2),

        'bbl_cold_iron': round(((cold_iron * x_cold_iron + b_cold_iron) * hours_year)/density, 2),

        'total_bbl_consumed': round((((underway * x_underway + b_underway) * hours_year)/density) + (((not_underway * x_not_underway + b_not_underway) * hours_year)/density) + (((cold_iron * x_cold_iron + b_cold_iron) * hours_year)/density), 2),

        'co2_underway': round(((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton), 2),

        'co2_not_underway': round(((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton), 2),

        'co2_cold_iron': round(((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton), 2),

        'total_co2_used': round((((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton)), 2),

        'optimum_range': round(((((underway * x_underway + b_underway) * hours_year)/density) * optimum), 2),

        'worst_range': round(((((underway * x_underway + b_underway) * hours_year)/density) * worst), 2),

        'optimum_co2': round(((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton)/((((underway * x_underway + b_underway) * hours_year)/density) * optimum), 9),

        'worst_co2': round(((((underway * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton) / ((((underway * x_underway + b_underway) * hours_year)/density) * worst), 9),

        'co2_mission': round((((((underway * x_underway + b_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((not_underway * x_not_underway + b_not_underway) * hours_year)/density) * conversion * lbs_to_ton) + ((((cold_iron * x_underway + b_cold_iron) * hours_year)/density) * conversion * lbs_to_ton)) * (mission_days / DAYS_PER_YEAR), 2)

    }

    return results


def calculate_ship_info(ship_name, fuel_type, underway, not_underway, cold_iron, mission_days):

    df = pd.read_csv("F76_fuel_consumption_values.csv")

    values_dict = df.set_index('ship_names').to_dict(orient='index')

    fuel_density = {  # maps fuel types to densities
        'F76': 1,
        'Ethanol': 0.5934,
        'LPG': 1.0549,
        'Methanol': 0.4989
    }

    bbl_to_co2 = {
        'F76': 942.48,

        'Ethanol': 532.41573,

        'LPG': 525.9341472,

        'Methanol': 379.635564,

    }

    ship_results = {}
    ship_results[ship_name] = {}  # ship_results[ship_name] = {ship_name : {} }

    if ship_name in values_dict:
        ship_data = values_dict[ship_name]

        for fuel, density in fuel_density.items():
            # density = fuel_density.get(fuel_type,0)
            conversion = bbl_to_co2.get(fuel, 0)

            # ship_results[ship_name][fuel_type] = {ship_name : {fuel_type : {} } }
            ship_results[ship_name][fuel] = {}
            # results[ship_name][fuel_type] = make_results_dict(density, conversion, underway,not_underway,cold_iron,optimum,worst,x_underway,b_underway, x_not_underway, b_not_underway, x_cold_iron, b_cold_iron, mission_days,DAYS_PER_YEAR=365,hours_year=8760,lbs_to_ton=0.0005)
            ship_results[ship_name][fuel] = make_results_dict(
                density, conversion, underway, not_underway, cold_iron, **ship_data)
            
    if ship_name.lower == "all" : 
        return ship_results

    elif fuel_type in fuel_density:
        return ship_results[ship_name][fuel_type]
    
    else: 
        return ship_results[ship_name]
        


shipcalc = calculate_ship_info(
    ship_name, fuel_type, underway=0.9, not_underway=0.1, cold_iron=0, mission_days=365)

print("class :", ship_name, "fuel: ", fuel_type)

print(shipcalc)


# df = pd.read_csv("F76_fuel_consumption_values.csv")

# values_dict = df.set_index('ship_names').to_dict(orient='index')
# print(values_dict['LHA-6CL'])
