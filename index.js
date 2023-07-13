function calculate_ship_info(ship, fuel_type, underway, not_underway, cold_iron, mission_days = 180, mission_underway = 0.9, mission_notunderway = 0.1) {
  // Declarations & calculations
  const list_of_ships = ['LHA-6CL', 'LPD-17CL', 'CG-47CL', 'MCM-1CL', 'DDG-51CL', 'LSD-41CL', 'LHD-1CL', 'LCS-1CL', 'LCC-19CL', 'FFG-7CL', 'LCS-2CL', 'LPD-4CL', 'DDG-1000CL', 'LHA-1CL', 'LSD-49CL'];

  const fuel_types = ['F76', 'Ethanol', 'LPG', 'Methanol', 'All'];

  if (list_of_ships.includes(ship) && fuel_types.includes(fuel_type)) {
    const index = list_of_ships.indexOf(ship);

    const underway_values = [28.992, 14.438, 29.861, 1.1068, 24.867, 12.162, 42.691, 10.619, 23.038, 10.663, 9.8959, 21.566, 28.075, 46.501, 12.07];
    const not_underway_values = [8.1288, 4.6906, 6.0818, 0.2608, 5.4049, 3.7654, 13.337, 0.6568, 11.841, 1.7882, 1.8031, 9.1597, 4.6964, 18.91, 3.4972];
    const cold_iron_values = [0.0153, 0.0687, 0.0168, 0.0012, 0.0144, 0.0194, 0.01221, 0.0296, 0.0219, 0.03, 0.0515, 0.042, 0.0005, 0.1845, 0.0308];

    // Conversions
    // ALL CAPS TO INDICATE CONST
    const B_VALUE = 0;
    const HOURS_YEAR = 8760;

    const BBL_TO_CO2 = 942.48;
    const LBS_TO_TON = 0.0005;
    const ETHANOL_TO_CO2 = 532.41573;
    const LPG_TO_CO2 = 525.9341472;
    const METHANOL_TO_CO2 = 379.635564;

    const ETHANOL_DENSITY = 0.5934;
    const LPG_DENSITY = 1.0549;
    const METHANOL_DENSITY = 0.4989;
    // Conversions end

    const f_underway = parseFloat(underway);
    const f_not_underway = parseFloat(not_underway);
    const f_cold_iron = parseFloat(cold_iron);
    const xvalue_underway = underway_values[index];
    const xvalue_not_underway = not_underway_values[index];
    const xvalue_cold_iron = cold_iron_values[index];

    //For f76 military diesel
    const bbl_underway = parseFloat(((f_underway * xvalue_underway + B_VALUE) * HOURS_YEAR).toFixed(2));
    const bbl_not_underway = parseFloat(((f_not_underway * xvalue_not_underway + B_VALUE) * HOURS_YEAR).toFixed(2));
    const bbl_cold_iron = parseFloat(((f_cold_iron * xvalue_cold_iron + B_VALUE) * HOURS_YEAR).toFixed(2));

    //Ethanol BBL
    const ethanol_underway = parseFloat((bbl_underway / ETHANOL_DENSITY).toFixed(2));
    const ethanol_not_underway = parseFloat((bbl_not_underway / ETHANOL_DENSITY).toFixed(2));
    const ethanol_cold_iron = parseFloat((bbl_cold_iron / ETHANOL_DENSITY).toFixed(2));

    //LPG BBL
    const lpg_underway = parseFloat((bbl_underway / LPG_DENSITY).toFixed(2));
    const lpg_not_underway = parseFloat((bbl_not_underway / LPG_DENSITY).toFixed(2));
    const lpg_cold_iron = parseFloat((bbl_cold_iron / LPG_DENSITY).toFixed(2));

    //Methanol BBl
    const methanol_underway = parseFloat((bbl_underway / METHANOL_DENSITY).toFixed(2));
    const methanol_not_underway = parseFloat((bbl_not_underway / METHANOL_DENSITY).toFixed(2));
    const methanol_cold_iron = parseFloat((bbl_cold_iron / METHANOL_DENSITY).toFixed(2));

    //BBL to CO2 conversion for each fuel type 
    const f76_co2_underway = parseFloat((bbl_underway * BBL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const f76_co2_not_underway = parseFloat((bbl_not_underway * BBL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const f76_co2_cold_iron = parseFloat((bbl_cold_iron * BBL_TO_CO2 * LBS_TO_TON).toFixed(2));


    const ethanol_co2_underway = parseFloat((ethanol_underway * ETHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const ethanol_co2_not_underway = parseFloat((ethanol_not_underway * ETHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const ethanol_co2_cold_iron = parseFloat((ethanol_cold_iron * ETHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));

    const lpg_co2_underway = parseFloat((lpg_underway * LPG_TO_CO2 * LBS_TO_TON).toFixed(2));
    const lpg_co2_not_underway = parseFloat((lpg_not_underway * LPG_TO_CO2 * LBS_TO_TON).toFixed(2));
    const lpg_co2_cold_iron = parseFloat((lpg_cold_iron * LPG_TO_CO2 * LBS_TO_TON).toFixed(2));

    const methanol_co2_underway = parseFloat((methanol_underway * METHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const methanol_co2_not_underway = parseFloat((methanol_not_underway * METHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));
    const methanol_co2_cold_iron = parseFloat((methanol_cold_iron * METHANOL_TO_CO2 * LBS_TO_TON).toFixed(2));

    const total_co2_used_f76 = parseFloat((f76_co2_underway + f76_co2_not_underway + f76_co2_cold_iron).toFixed(2));
    const total_co2_used_ethanol = parseFloat((ethanol_co2_underway + ethanol_co2_not_underway + ethanol_co2_cold_iron).toFixed(2));
    const total_co2_used_lpg = parseFloat((lpg_co2_underway + lpg_co2_not_underway + lpg_co2_cold_iron).toFixed(2));
    const total_co2_used_methanol = parseFloat((methanol_co2_underway + methanol_co2_not_underway + methanol_co2_cold_iron).toFixed(2));

    //Total fuel consumed per Fuel
    const f76_total_bbl_consumed = parseFloat((bbl_underway + bbl_not_underway + bbl_cold_iron).toFixed(2));
    const ethanol_total_bbl_consumed = parseFloat((ethanol_underway + ethanol_not_underway + ethanol_cold_iron).toFixed(2));
    const lpg_total_bbl_consumed = parseFloat((lpg_underway + lpg_not_underway + lpg_cold_iron).toFixed(2));
    const methanol_total_bbl_consumed = parseFloat((methanol_underway + methanol_not_underway + methanol_cold_iron).toFixed(2));
    //Dictionaries
    let fuel_dictionary = {
      'F76': 'F-76 Military Diesel',
      'Ethanol': 'Ethanol Fuel',
      'LPG': 'Liquid Petroleum Gas',
      'Methanol': 'Methanol Fuel',
    };

    let ships_dictionary = {
      'LHA-6CL': 'USS America amphibious assault ship',
      'LPD-17CL': 'San Antonio class landing platform dock',
      'CG-47CL': 'USS Ticonderoga guided-missile cruiser',
      'MCM-1CL': 'Avenger class mine countermeasures ships',
      'DDG-51CL': 'Arleigh Burke class guided missile destroyers',
      'LSD-41CL': 'Whidbey Island-class dock landing ship',
      'LHD-1CL': 'USS Wasp multipurpose amphibious assault ship',
      'LCS-1CL': 'Freedom-class littoral combat ship',
      'LCC-19CL': 'Blue Ridge-class amphibious command ships',
      'FFG-7CL': 'Oliver Hazard Perry-class guided-missile frigate',
      'LCS-2CL': 'Littoral combat ship surface vessels',
      'LPD-4CL': 'Amphibious transport dock',
      'DDG-1000CL': 'USS Zumwalt guided missile destroyer',
      'LHA-1CL': ' America class landing helicopter assault',
      'LSD-49CL': 'USS Harpers Ferry: landing ship dock',
    };

    let results_dictionary = {
      //for f76 fuel_type
      'f76_bbl_underway': bbl_underway,
      'f76_bbl_not_underway': bbl_not_underway,
      'f76_bbl_cold_iron': bbl_cold_iron,
      'f76_total_bbl_consumed': f76_total_bbl_consumed,
      'f76_co2_underway': f76_co2_underway,
      'f76_co2_not_underway': f76_co2_not_underway,
      'f76_co2_cold_iron': f76_co2_cold_iron,
      'f76_total_co2_used': total_co2_used_f76,

      //for ethanol
      'ethanol_underway': ethanol_underway,
      'ethanol_not_underway': ethanol_not_underway,
      'ethanol_cold_iron': ethanol_cold_iron,
      'ethanol_total_bbl_consumed': ethanol_total_bbl_consumed,
      'ethanol_co2_underway': ethanol_co2_underway,
      'ethanol_co2_not_underway': ethanol_co2_not_underway,
      'ethanol_co2_cold_iron': ethanol_co2_cold_iron,
      'ethanol_total_co2_used': total_co2_used_ethanol,

      //for lpg
      'lpg_underway': lpg_underway,
      'lpg_not_underway': lpg_not_underway,
      'lpg_cold_iron': lpg_cold_iron,
      'lpg_total_bbl_consumed': lpg_total_bbl_consumed,
      'lpg_co2_underway': lpg_co2_underway,
      'lpg_co2_not_underway': lpg_co2_not_underway,
      'lpg_co2_cold_iron': lpg_co2_cold_iron,
      'lpg_total_co2_used': total_co2_used_lpg,

      //for methanol
      'methanol_underway': methanol_underway,
      'methanol_not_underway': methanol_not_underway,
      'methanol_cold_iron': methanol_cold_iron,
      'methanol_total_bbl_consumed': methanol_total_bbl_consumed,
      'methanol_co2_underway': methanol_co2_underway,
      'methanol_co2_not_underway': methanol_co2_not_underway,
      'methanol_co2_cold_iron': methanol_co2_cold_iron,
      'methanol_total_co2_used': total_co2_used_methanol,
    };

    let definition_dictionary = {
      //For military diesel
      'f76_bbl_underway': 'BBL Fuel Consumed Underway (est)',
      'f76_bbl_not_underway': 'BBL Fuel Consumed Not Underway (est)',
      'f76_bbl_cold_iron': 'BBL Fuel Consumed Cold Iron (est)',
      'f76_total_bbl_consumed': 'Total BBL Fuel Consumed (est)',
      'f76_co2_underway': 'CO2E Underway (est Tons)',
      'f76_co2_not_underway': 'CO2E Not underway (est Tons)',
      'f76_co2_cold_iron': 'CO2E Cold Iron (est Tons)',
      'f76_total_co2_used': 'Total CO2E (est Tons)',

      //For ethanol
      'ethanol_underway': 'BBL Fuel Consumed Underway (est)',
      'ethanol_not_underway': 'BBL Fuel Consumed Not Underway (est)',
      'ethanol_cold_iron': 'BBL Fuel Consumed Cold Iron (est)',
      'ethanol_total_bbl_consumed': 'Total BBL Fuel Consumed (est)',
      'ethanol_co2_underway': 'CO2E underway (est Tons)',
      'ethanol_co2_not_underway': 'CO2E Not Underway (est Tons)',
      'ethanol_co2_cold_iron': 'CO2E Cold Iron (est Tons)',
      'ethanol_total_co2_used': 'Total CO2E (est Tons)',

      //for LPG
      'lpg_underway': 'BBL Fuel Consumed Underway (est)',
      'lpg_not_underway': 'BBL Fuel Consumed Not Underway (est)',
      'lpg_cold_iron': 'BBL Fuel Consumed Cold Iron (est)',
      'lpg_total_bbl_consumed': 'Total BBL Fuel Consumed (est)',
      'lpg_co2_underway': 'CO2E underway (est Tons)',
      'lpg_co2_not_underway': 'CO2E Not Underway (est Tons)',
      'lpg_co2_cold_iron': 'CO2E Cold Iron (est Tons)',
      'lpg_total_co2_used': 'Total CO2E (est Tons)',

      //for methanol
      'methanol_underway': 'BBL Fuel Consumed Underway (est)',
      'methanol_not_underway': 'BBL Fuel Consumed Not Underway (est)',
      'methanol_cold_iron': 'BBL Fuel Consumed Cold Iron (est)',
      'methanol_total_bbl_consumed': 'Total BBL Fuel Consumed (est)',
      'methanol_co2_underway': 'CO2E underway (est Tons)',
      'methanol_co2_not_underway': 'CO2E Not Underway (est Tons)',
      'methanol_co2_cold_iron': 'CO2E Cold Iron (est Tons)',
      'methanol_total_co2_used': 'Total CO2E (est Tons)',
    };
    //cannot return multiple dictionaries in javascript use array or objects to do so  
    return {
      results: results_dictionary,
      definitions: definition_dictionary,
      fuel: fuel_dictionary,
      ships: ships_dictionary
    };
  }
}

// Function to display the results on the webpage
function displayResults(results, definitions, fuelKey) {
  const resultContainer = document.getElementById("resultContainer");
  const resultContent = document.getElementById("resultContent");

  resultContent.innerHTML = ""; // Clear previous results

  for (const key in results) {
  if (fuelKey === 'All' || key.toLowerCase().startsWith(fuelKey.toLowerCase())) {
    const label = document.createElement("p");
    const value = document.createElement("p");

    const labelContent = definitions[key] || key;
    const valueContent = results[key];

    label.textContent = labelContent + ":";
    value.textContent = valueContent;

    resultContent.appendChild(label);
    resultContent.appendChild(value);
  }
}
  resultContainer.style.display = "block"; // Show the result section
}

// Add an event listener to the submit button
document.getElementById("submitBtn").addEventListener("click", function(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get input values from the HTML elements
  const ship = document.getElementById("ship_name").value;
  const fuelType = document.getElementById("fuel_type").value;
  const underway = parseFloat(document.getElementById("hours_underway").value);
  const notUnderway = parseFloat(document.getElementById("hours_not_underway").value);
  const coldIron = parseFloat(document.getElementById("cold_iron").value);

  // Perform the calculations
  if (ship && fuelType && !isNaN(underway) && !isNaN(notUnderway) && !isNaN(coldIron)) {
    const {
      results: resultsDictionary,
      definitions: definitionDictionary,
      fuel: fuelDictionary,
      ships: shipsDictionary
    } = calculate_ship_info(ship, fuelType, underway, notUnderway, coldIron);

    // Clear the console
    //console.clear();

    // Display the results in the console or update the HTML elements with the results
    console.log('Class:', ship, '\nFuel:', fuelType);
    console.log();

    if (ship in shipsDictionary) {
      const shipInfo = shipsDictionary[ship];
      console.log(ship, shipInfo);
    } else {
      console.log("Ship not found in the dictionary.");
    }

    console.log();

    if (fuelType === 'All') {
      for (const fuelKey in fuelDictionary) {
        const fuelVal = fuelDictionary[fuelKey];
        console.log(fuelVal);
        for (const key in resultsDictionary) {
          if (key.toLowerCase().startsWith(fuelKey.toLowerCase())) {
            const value = resultsDictionary[key];
            const definitionKey = key.replace(fuelKey, fuelVal);
            const definition = definitionDictionary[definitionKey];
            console.log(definition, value);
          }
        }
        console.log();
      }
    }
    else if(fuelType in fuelDictionary) {
      const fuelVal = fuelDictionary[fuelType];
      console.log(fuelVal);
      for (const key in resultsDictionary) {
        if (key.toLowerCase().startsWith(fuelType.toLowerCase())) {
          const value = resultsDictionary[key];
          const definitionKey = key.replace(fuelType, fuelVal);
          const definition = definitionDictionary[definitionKey];
          console.log(definition, value);
        }
      }
    }

    // Call the function to display the results on the webpage
    displayResults(resultsDictionary, definitionDictionary, fuelType);

    console.log('Results dictionary:');
    console.log(resultsDictionary);

  }
  else {
    console.log("Please fill in all the required fields with valid values.");
  }
});
