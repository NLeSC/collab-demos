

- **url:**  [http://jiskattema.github.io/summerinthecity/](http://jiskattema.github.io/summerinthecity/)
- **contact**: Jisk Atttema


# General idea of the project

On warm days, a city can become uncomfortably hot. Cities experience a so-called _urban heat island_ effect and are typically warmer than their surroundings. Also, cities experience two parallel developments: increased urbanization and an enhanced frequency of warm episodes due to the changing global climate. These developments may increase human health risks. For example, the 2003 European heat wave led to a health crisis in several European countries and 70.000 heat-related deaths. The situation is especially worrying for vulnerable groups, such as the elderly and people with health issues, but affects the work productivity and well-being of us all. If we want to keep life in the city comfortable in the future, a better understanding of urban weather and climate is essential.

The forecasting of thermal human comfort requires simulations on very high spatial and temporal scales, posing both a meteorological and an eScience challenge. Observational data to validate the weather forecasts at street level are based on a network of weather stations in two cities: Wageningen and Amsterdam. This network has a fine spatial detail compared to other networks in the research field and allows for an evaluation of the forecasted temperature and humidity. Bike traverse measurements of temperature, humidity, wind speed, and radiation are taken regularly. These observations resolve a high degree of spatial detail in urban weather and contribute to an understanding of urban climate.

# Demo usage

[The demo](http://jiskattema.github.io/summerinthecity/) is a publicly accessible web demo. That means you should be able to access it from any computer using your browser as long as you have a working internet connection.

The demo consists of an interactive map showing the urban heat island effect (UHI). It should be used in combination with a traditional temperature forecast to get an estimation of the actual temperature in your neighborhood. Take the traditional temperature forecast and add the UHI50P for an average day, and the UHI95P for a heatwave. 

When hovering over the map, a pop-up shows some summary statistics, such as the population count, the area fraction of urbanization (houses, streets), vegetation (trees, grass, gardens, parks), and water.

## Known quirks
- UHI vector overlay only visible for intermediate zoom levels. If you zoom out too much, you see only 'gemeentes' without color information on temperature; zoom in too much and you see only houses.



# Technologically interesting aspects

_Bringing together various data sources_

  - Kadaster (what building is located where?)
  - [AHN](http://ahn.maps.arcgis.com/apps/webappviewer/index.html?id=c3c98b8a4ff84ff4938fafe7cc106e88) (what is the local surface elevation of the landscape (including objects such as buildings, trees, etc)?
  -  Aerial photography (how green is a given area?)
  -  _Citizen science_: [Weather Underground](http://www.wunderground.com/) observations
  -  Wageningen University's sensor network of 30 weather stations located in and around the city of Wageningen

_High-resolution modeling requires a lot of compute power_

  - A 2-days ahead prediction for the Amsterdam area takes about 10 hours walltime on 96 cores of the [Cartesius](https://userinfo.surfsara.nl/systems/cartesius) supercomputer, so approximately 5x realtime.

# Scientifically interesting aspects

- High-resolution modeling provides street-level forecast
- Forecasting human thermal comfort in urban areas at the required resolution is novel
- Comparing high-resolution weather model of urban environments to traditional weather forecasts shows structural differences (for example with respect to temperature). Finding the mechanisms that explain such structural differences will lead to better understanding of weather in urban environments.

# Further reading

- [https://www.esciencecenter.nl/?/project/summer-in-the-city](https://www.esciencecenter.nl/?/project/summer-in-the-city)
- [http://www.parool.nl/parool/nl/8/WEER/article/detail/3673212/2014/06/16/Universiteit-zet-30-weerstations-in-Amsterdam.dhtml](http://www.parool.nl/parool/nl/8/WEER/article/detail/3673212/2014/06/16/Universiteit-zet-30-weerstations-in-Amsterdam.dhtml)
- [https://vimeo.com/109430452](https://vimeo.com/109430452)
