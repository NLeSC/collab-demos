
- **url**: http://viaappia.esciencecenter.nl/
- **contact person**: Maarten van Meersbergen


# General idea of the project

The [Via Appia](https://en.wikipedia.org/wiki/Appian_Way) was one of the earliest and strategically most important roads of the Roman world, dating from the fourth century BC. It connected ancient Rome to Greece and the East. Its total length was more than 500 km running al the way to modern-day [Brindisi](https://www.google.nl/maps/place/Brindisi+BR,+Italy/@40.6422249,17.9009354,7z/data=!4m2!3m1!1s0x13467a3bc980ec6d:0x110cef7cc03daf9) in southeast Italy. As a consequence of the Roman custom of cremation and burial outside the city walls, the most opulent and prestigious funerary monuments were erected all along the Via Appia, rendering the first miles of the Via Appia into a boastful necropolis. At the end of the 19th century, the Via Appia became one of the first archaeological parks in the world, and has been preserved ever since. 

_Reconstructing the functioning of the Via Appia in antiquity_

The "Mapping the Via Appia" project aims at a thorough inventory and analysis of the Roman interventions in this suburban landscape. The research focuses on a section of two kilometers that covers parts of the fifth and sixth mile of the Via Appia, supplemented with a research area that covers the hinterland as far as nearly one kilometer northeast and about 2.5 kilometers southwest of the road. Based on the physical remains in combination with historical sources, archaeologists aim to reconstruct the functioning of the road in antiquity. The study area contains more than 2000 archaeological objects directly alongside the road. The biggest difficulty for the archaeologists is that the archaeological remains are scattered alongside the road and often not in situ.


The [Via Appia](https://en.wikipedia.org/wiki/Appian_Way) was the main highway connecting ancient Rome to Greece and the East. Its total length was more than 500 km running al the way to modern-day [Brindisi](https://www.google.nl/maps/place/Brindisi+BR,+Italy/@40.6422249,17.9009354,7z/data=!4m2!3m1!1s0x13467a3bc980ec6d:0x110cef7cc03daf9). Over time, many funeral monuments were erected along the street. Currently there is an effort underway to catalogue all of these monuments. 

Previously, this was mostly done using [Geographical Information Systems](https://en.wikipedia.org/wiki/Geographic_information_system) (GIS), but the inherent 3-D nature of archaeology requires a different solution. For example, questions such as _Did this block of tufa come from that funeral monument down the road?_ are difficult to answer in GIS software, because it is not very well suited for viewing 3-D geometries. Alternatively one could measure the block in the field and measure the funerary monument that the block is thought to originate from. However, this is a lot of work, and it is only feasible when it's known which block and which monument need to be measured. Slightly different questions such as _Is there a funeral monument nearby from which this block of tufa may have originated?_ cannot be answered by either a GIS or by measuring just one funeral monument and one block. 

So instead, what was needed was a system that measures the shape of the entire object, for every object along the Via Appia. This type of information can be collected using a relatively new technology, known as [_lidar_](https://en.wikipedia.org/wiki/Lidar). Lidar data was collected by Fugro using a laser scanner device mounted on a vehicle. The vehicle is equipped with multiple, very accurate GPS devices that work together with a very accurate gyroscope to determine the vehicle's location on Earth. The laser scanner that is mounted on the vehicle subsequently sends out a laser pulse and records the time it took for the laser light to be reflected. Since the reflection time is a measure of distance from the vehicle to the object that reflected the light, this technique can be used to construct so-called _point clouds_ of the environment.

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
