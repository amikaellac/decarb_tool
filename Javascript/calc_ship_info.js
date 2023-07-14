async function calculate_ship_info(
  ship_name,
  fuel_type,
  underway,
  not_underway,
  cold_iron
) {
  const values_dict = await getData(ship_name);

  const fuel_density = {
    F76: 1,
    Ethanol: 0.5934,
    LPG: 1.0549,
    Methanol: 0.4989,
  };

  const bbl_to_co2 = {
    F76: 942.48,
    Ethanol: 532.41573,
    LPG: 525.9341472,
    Methanol: 379.635564,
  };

  const ship_results = {};
  ship_results[ship_name] = {};

  if (values_dict) {
    for (const fuel in fuel_density) {
      const density = fuel_density[fuel];
      const conversion = bbl_to_co2[fuel];

      ship_results[ship_name][fuel] = make_results_dict(
        density,
        conversion,
        underway,
        not_underway,
        cold_iron,
        values_dict
      );
    }
  }

  if (fuel_type in fuel_density) {
    console.log(ship_results[ship_name][fuel_type]);
    return ship_results[ship_name][fuel_type];
  } else {
    //console.log(ship_results);
    return ship_results;
  }
  // console.log(values_dict); ////////////// correct values have been returned
  // if (typeof values_dict.x_not_underway === "number")
  //   console.log("its a number");
}
