

- **url:**  [http://jiskattema.github.io/summerinthecity/](http://jiskattema.github.io/summerinthecity/)
- **contact**: Jisk Atttema


# general idea

On warm days, a city can become uncomfortably hot. Cities experience a so-called _urban heat island_ effect and are typically warmer than their surroundings. Also, cities experience two parallel developments: increased urbanization and an enhanced frequency of warm episodes due to the changing global climate. These developments may increase human health risks. For example, the 2003 European heat wave led to a health crisis in several European countries and 70.000 heat-related deaths. The situation is especially worrying for vulnerable groups, such as the elderly and people with health issues, but affects the work productivity and well-being of us all. If we want to keep life in the city comfortable in the future, a better understanding of urban weather and climate is essential.

The forecasting of thermal human comfort requires simulations on very high spatial and temporal scales, posing both a meteorological and an eScience challenge. Observational data to validate the weather forecasts at street level are based on a network of weather stations in two cities: Wageningen and Amsterdam. This network has a fine spatial detail compared to other networks in the research field and allows for an evaluation of the forecasted temperature and humidity. Bike traverse measurements of temperature, humidity, wind speed, and radiation are taken regularly. These observations resolve a high degree of spatial detail in urban weather and contribute to an understanding of urban climate.

Next to the proposed research, dissemination of results via the Internet and social media will be explored. Forecasting human thermal comfort on street level is novel and will be of added value for public health and society in general. The first step is to process the urban morphological data into parameters relevant to the weather forecasting model. The mesoscale meteorological model WRF (Weather Research and Forecasting) can then produce fine spatial scale weather forecasts. These forecasts are downscaled to the street scale using knowledge of the available geo-information. Truly a Big Data challenge.

# usage

This demo is a publicly accessible web demo. That means you should be able to access it with your browser as long as you have a working internet connection.

The map shows the urban heat island effect (UHI). It should be used in combination with a traditional temperature forecast to get an estimation of the actual temperature in your neighborhood. Take the temperature forecast and add the UHI50P for an average day, and the UHI95P for a heatwave. When hovering over the map, a pop-up also shows the population count, and the area fraction of urbanization (houses, streets), vegetation (trees, grass, gardens, parks), and water.

## quirks
- vector overlay only specified for certain zoom levels. If you zoom out too much, you see only 'gemeentes' without color information on heat; zoom in too much and you see only houses.



# technologically interesting aspects

- bringing together various data sources
  - kadaster (what building is located where?)
  - [AHN](http://ahn.maps.arcgis.com/apps/webappviewer/index.html?id=c3c98b8a4ff84ff4938fafe7cc106e88) (what is the local surface elevation of the landscape (including objects such as buildings, trees, etc)?
  -  aerial photography (how green is a given area?)
  -  _citizen science_: [Weather Underground](http://www.wunderground.com/) observations
  -  Wageningen University's sensor network of 30 weather stations located in and around the city of Wageningen



# science

- 
