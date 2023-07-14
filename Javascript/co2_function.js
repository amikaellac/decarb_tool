// fetch("F76_fuel_consumption_values.csv")
//   .then((response) => response.text())
//   .then((csvData) => {
//     const df = csvData.split("\n").map((row) => row.split(","));

//     // Use `df` variable for further processing
//     // Call `calculate_ship_info` function here or perform any other operations
//   })
//   .catch((error) => {
//     console.error("Error loading CSV file:", error);
//   });

//function to obtain values from csv file

async function getData(ship_name) {
  var headerNames;
  var shipDict = {};
  values_dict = {};

  const response = await fetch("test.csv");
  const data = await response.text();
  const csvData = data.split("\r\n");

  csvData.forEach((row, index) => {
    const columns = row.split(",");
    if (index === 0) {
      headerNames = columns;
    } else {
      const shipData = {};
      for (let i = 1; i < headerNames.length; i++) {
        shipData[headerNames[i]] = columns[i];
      }
      const shipKey = columns[0];
      shipDict[shipKey] = shipData;
    }
    // values_dict = shipDict[ship_name];  //here to check
  });
  //console.log(shipDict[ship_name]);
  //console.log(values_dict);               //here to check
  return shipDict[ship_name];
}

// function calculate_ship_info(
//   ship_name,
//   fuel_type,
//   underway,
//   not_underway,
//   cold_iron
// ) {
//   // Assuming you have loaded the CSV data into `values_dict` variable

//   // const values_dict = df.reduce((acc, curr) => {
//   //   acc[curr.ship_names] = curr;
//   //   return acc;
//   // }, {});

//   const fuel_density = {
//     f76: 1,
//     ethanol: 0.5934,
//     lpg: 1.0549,
//     methanol: 0.4989,
//   };

//   const bbl_to_co2 = {
//     f76: 942.48,
//     ethanol: 532.41573,
//     lpg: 525.9341472,
//     methanol: 379.635564,
//   };

//   const ship_results = {};
//   ship_results[ship_name] = {};

//   if (ship_name in values_dict) {
//     const ship_data = values_dict[ship_name];

//     for (const fuel in fuel_density) {
//       const density = fuel_density[fuel];
//       const conversion = bbl_to_co2[fuel];

//       ship_results[ship_name][fuel] = make_results_dict(
//         density,
//         conversion,
//         underway,
//         not_underway,
//         cold_iron,
//         ...Object.values(ship_data)
//       );
//     }
//   }

//   if (fuel_type in fuel_density) {
//     return ship_results[ship_name][fuel_type];
//   } else {
//     return ship_results;
//   }
// }

// function make_results_dict({
//   density = 0,
//   conversion = 0,
//   underway = 0,
//   not_underway = 0,
//   cold_iron = 0,
//   optimum = 0,
//   worst = 0,
//   x_underway = 0,
//   b_underway = 0,
//   x_not_underway = 0,
//   b_not_underway = 0,
//   x_cold_iron = 0,
//   b_cold_iron = 0,
//   mission_days = 365,
//   DAYS_PER_YEAR = 365,
//   hours_year = 8760,
//   lbs_to_ton = 0.0005,
// }) {
//   const results = {
//     bbl_underway: (
//       ((underway * x_underway + b_underway) * hours_year) /
//       density
//     ).toFixed(2),

//     bbl_not_underway: (
//       ((not_underway * x_not_underway + b_not_underway) * hours_year) /
//       density
//     ).toFixed(2),

//     bbl_cold_iron: (
//       ((cold_iron * x_cold_iron + b_cold_iron) * hours_year) /
//       density
//     ).toFixed(2),

//     total_bbl_consumed: (
//       ((underway * x_underway + b_underway) * hours_year) / density +
//       ((not_underway * x_not_underway + b_not_underway) * hours_year) /
//         density +
//       ((cold_iron * x_cold_iron + b_cold_iron) * hours_year) / density
//     ).toFixed(2),

//     co2_underway: (
//       (((underway * x_underway + b_underway) * hours_year) / density) *
//       conversion *
//       lbs_to_ton
//     ).toFixed(2),

//     co2_not_underway: (
//       (((not_underway * x_not_underway + b_not_underway) * hours_year) /
//         density) *
//       conversion *
//       lbs_to_ton
//     ).toFixed(2),

//     co2_cold_iron: (
//       (((cold_iron * x_underway + b_cold_iron) * hours_year) / density) *
//       conversion *
//       lbs_to_ton
//     ).toFixed(2),

//     total_co2_used: (
//       (((underway * x_underway + b_underway) * hours_year) / density) *
//         conversion *
//         lbs_to_ton +
//       (((not_underway * x_not_underway + b_not_underway) * hours_year) /
//         density) *
//         conversion *
//         lbs_to_ton +
//       (((cold_iron * x_underway + b_cold_iron) * hours_year) / density) *
//         conversion *
//         lbs_to_ton
//     ).toFixed(2),

//     optimum_range: (
//       (((underway * x_underway + b_underway) * hours_year) / density) *
//       optimum
//     ).toFixed(2),

//     worst_range: (
//       (((underway * x_underway + b_underway) * hours_year) / density) *
//       worst
//     ).toFixed(2),

//     optimum_co2:
//       ((((not_underway * x_not_underway + b_not_underway) * hours_year) /
//         density) *
//         conversion *
//         lbs_to_ton) /
//       (
//         (((underway * x_underway + b_underway) * hours_year) / density) *
//         optimum
//       ).toFixed(9),

//     worst_co2:
//       ((((underway * x_underway + b_cold_iron) * hours_year) / density) *
//         conversion *
//         lbs_to_ton) /
//       (
//         (((underway * x_underway + b_underway) * hours_year) / density) *
//         worst
//       ).toFixed(9),

//     co2_mission:
//       ((((underway * x_underway + b_underway) * hours_year) / density) *
//         conversion *
//         lbs_to_ton +
//         (((not_underway * x_not_underway + b_not_underway) * hours_year) /
//           density) *
//           conversion *
//           lbs_to_ton +
//         (((cold_iron * x_underway + b_cold_iron) * hours_year) / density) *
//           conversion *
//           lbs_to_ton) *
//       (mission_days / DAYS_PER_YEAR).toFixed(2),
//   };

//   return results;
// }
