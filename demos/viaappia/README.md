
- **url**: http://viaappia.esciencecenter.nl/
- **contact person**: Maarten van Meersbergen


# General idea of the project

The [Via Appia](https://en.wikipedia.org/wiki/Appian_Way) was one of the earliest and strategically most important roads of the Roman world, dating from the fourth century BC. It connected ancient Rome to Greece and the East. Its total length was more than 500 km running al the way to modern-day [Brindisi](https://www.google.nl/maps/place/Brindisi+BR,+Italy/@40.6422249,17.9009354,7z/data=!4m2!3m1!1s0x13467a3bc980ec6d:0x110cef7cc03daf9) in southeast Italy. As a consequence of the Roman custom of cremation and burial outside the city walls, the most opulent and prestigious funerary monuments were erected all along the Via Appia, rendering the first miles of the Via Appia into a boastful necropolis. At the end of the 19th century, the Via Appia became one of the first archaeological parks in the world, and has been preserved ever since. 

_Reconstructing the functioning of the Via Appia in antiquity_

The "Mapping the Via Appia" project aims at a thorough inventory and analysis of the Roman interventions in this suburban landscape. The research focuses on a section of two kilometers that covers parts of the fifth and sixth mile of the Via Appia, supplemented with a research area that covers the hinterland as far as nearly one kilometer northeast and about 2.5 kilometers southwest of the road. Based on the physical remains in combination with historical sources, archaeologists aim to reconstruct the functioning of the road in antiquity. The study area _alone_ contains more than 2000 archaeological objects directly alongside the road. The number of objects, combined with the fact that many artifacts are no longer in situ, but instead have been scattered along the road, poses a challenge when trying to reconstruct a given object.

Traditionally, archaeologists would go out into the field, measure an object of interest, and record their findings in a database or [GIS  software](https://en.wikipedia.org/wiki/Geographic_information_system). However, a question such as _May this block of tufa have originated from that funeral monument down the road?_ or the more general question _Is there a funeral monument nearby from which this block of tufa may have originated?_ is difficult to answer with these tools due to the inherently 3-D nature of archaeology. 

So instead, what was needed was a system that measures the shape of _everything_, blocks, monuments, and everything else. Nowadays, the required type of information can be collected using a relatively new technology, known as [_lidar_](https://en.wikipedia.org/wiki/Lidar). Lidar data was collected by Fugro's [drive-map](http://www.drive-map.eu/) service using a laser scanner device mounted on a vehicle. The vehicle is equipped with multiple, very accurate GPS devices that work together with a very accurate gyroscope to determine the vehicle's location on Earth. The laser scanner that is mounted on the vehicle subsequently sends out a laser pulse and records the time it took for the laser light to be reflected when looking in a certain direction. Since the reflection time is a measure of distance from the vehicle to the object that reflected the light, this technique can be used to construct so-called _point clouds_ of the environment. These point clouds can be viewed in software, such that the archaeologists may then perform measurements of length, area, and volume in the virtual world rather than the real one.

# Usage

# Known quirks

User controls are not what you expect (issue #11) and vary with the mode of viewing (of which there are 4):

1. On rails (cowboy icon)
2. Free fly (helicopter icon)
3. Demo mode (play icon)
4. Object inspection (no icon)

I've included a [cheatsheet](/cheatsheet).


# Scientifically interesting aspects

# Technologically interesting aspects

# Further reading

- Project [website](https://www.esciencecenter.nl/via-appia)
- [http://mappingtheviaappia.nl/3dgis/](http://mappingtheviaappia.nl/3dgis/)
- [Video](https://youtu.be/I3DLXSrRiyk) made by Rens de Hond
