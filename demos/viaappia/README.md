
# In short

- **url**: http://viaappia.esciencecenter.nl/
 - IP-whitelisting or username/password (see LastPass)
 - Works better with GPU
- **screencast**: [https://www.youtube.com/watch?v=I3DLXSrRiyk](https://www.youtube.com/watch?v=I3DLXSrRiyk)
- **contact person**: [Maarten van Meersbergen](https://www.esciencecenter.nl/profile/maarten-van-meersbergen-msc)
- **screenshot**:

![screenshot](/demos/viaappia/screencapture-demo-viaappia.png "screenshot demo Via Appia")


# General idea of the project

The [Via Appia](https://en.wikipedia.org/wiki/Appian_Way) was one of the earliest and strategically most important roads of the Roman world, dating from the fourth century BC. It connected ancient Rome to Greece and the East. Its total length was more than 500 km running al the way to modern-day [Brindisi](https://www.google.nl/maps/place/Brindisi+BR,+Italy/@40.6422249,17.9009354,7z/data=!4m2!3m1!1s0x13467a3bc980ec6d:0x110cef7cc03daf9) in southeast Italy. As a consequence of the Roman custom of cremation and burial outside the city walls, the most opulent and prestigious funerary monuments were erected all along the Via Appia, rendering the first miles of the Via Appia into a boastful necropolis. At the end of the 19th century, the Via Appia became one of the first archaeological parks in the world, and has been preserved ever since. 

_Reconstructing the functioning of the Via Appia in antiquity_

The "Mapping the Via Appia" project aims at a thorough inventory and analysis of the Roman interventions in this suburban landscape. The research focuses on a section of two kilometers that covers parts of the fifth and sixth mile of the Via Appia, supplemented with a research area that covers the hinterland as far as nearly one kilometer northeast and about 2.5 kilometers southwest of the road. Based on the physical remains in combination with historical sources, archaeologists aim to reconstruct the functioning of the road in antiquity. The study area _alone_ contains more than 2000 archaeological objects directly alongside the road. The number of objects, combined with the fact that many artifacts are no longer in situ, but instead have been scattered along the road, poses a challenge when trying to reconstruct a given object.

Traditionally, archaeologists would go out into the field, measure an object of interest, and record their findings in a database or [GIS  software](https://en.wikipedia.org/wiki/Geographic_information_system). However, a question such as _May this block of tufa have originated from that funeral monument down the road?_ or the more general question _Is there a funeral monument nearby from which this block of tufa may have originated?_ is difficult to answer with these tools due to the inherently 3-D nature of archaeology. 

_Using lidar to create a virtual representation of the environment_

So instead, what was needed was a system that measures the shape of _everything_&mdash;blocks, monuments, and everything else. Nowadays, the required type of information can be collected using a relatively new technology, known as [_lidar_](https://en.wikipedia.org/wiki/Lidar). Lidar data was collected by Fugro's [drive-map](http://www.drive-map.eu/) service using a laser scanner device mounted on a vehicle. The vehicle is equipped with multiple, very accurate GPS devices that work together with a very accurate gyroscope to determine the vehicle's location on Earth. The laser scanner that is mounted on the vehicle subsequently sends out a laser pulse and records the time it took for the laser light to be reflected when looking in a certain direction. Since the reflection time is a measure of distance from the vehicle to the object that reflected the light, this technique can be used to construct so-called _point clouds_ of the environment. 

_Using photographs to construct point clouds of archaeological objects_

The drive map point cloud provides good spatial coverage and is very accurate, but the archaeological objects themselves were a bit coarse. To mitigate this, it was necessary to introduce another source of information in the form of photographs: during the course of an archaeological dig, each object is meticulously photographed using consumer grade cameras. Using [stereophotogrammetry](https://en.wikipedia.org/wiki/Photogrammetry#Stereophotogrammetry), the photographs were combined into a point cloud, providing additional detail about the object. 

The point clouds resulting from stereophotogrammetry were then combined with the drive map point clous, and the result was put into a database. A point cloud viewer was then built to be able to move through the virtual landscape, to inspect the archaeological objects close up, and even to perform measurements of length, area, and volume&mdash;all in the virtual world. 

# Known quirks

User controls are not what you expect and vary with the mode of viewing (of which there are 4):

1. On rails (cowboy icon)
2. Free fly (helicopter icon)
3. Demo mode (play icon)
4. Object inspection (no icon)

I've included a [cheatsheet](/demos/viaappia/cheatsheet.md).

Also the demo sometimes crashes unexpectedly. It is currently unknown what causes this. In any case, it seems to happen more frequently when loading a lot of data.

The demo uses **IP-whitelisting** to get the data from the server (which is located in Germany). In practice, this means that the webdemo will work as long as you are showing the demo on a computer anywhere in The Netherlands eScience Center including the Collaboratorium (as long as you use a wired network connection).

Information on **known quirks** is collected [here](/../../issues/11). See also the [general remarks](/doc/demo-usage-general-remarks.md) about web demos.


# Scientifically interesting aspects

- Different types of questions can now be asked
- Query the shape of the landscape and the objects in it 

# Technologically interesting aspects

- visualization of large numbers of points in a web-based viewer
- generation of detailed point clouds and textured meshes from a collection of photographs using distributed computing to speed up the process
- bringing together point clouds from different sources, generated using different techniques.
- integrating the point cloud 3-D environment with additional information in the form of old maps, images, and existing  descriptions of objects
 

# Further reading

- Project [website](https://www.esciencecenter.nl/via-appia) on esciencecenter.nl
- Project [video](https://youtu.be/I3DLXSrRiyk) on youtube.com made by Rens de Hond
- A screencast [video](https://vimeo.com/154200277) of the demo on vimeo.com
- Browse the code on github.com:
  - [PattyData](https://github.com/NLeSC/PattyData): data management for the Via Appia 3D GIS
  - [PattyVis](https://github.com/NLeSC/PattyVis): WebGL pointcloud visualization of the Via Appia 3D GIS based on potree.
  - [PattyAnalytics](https://github.com/NLeSC/PattyAnalytics): Reusable point cloud analytics software. Includes segmentation, registration, file format conversion.
  - [structure-from-motion](https://github.com/NLeSC/structure-from-motion): Structure from Motion Pipeline: stereophotogrammetry
- Pitch presentations on [sharepoint](https://nlesc.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2FShared%20Documents%2FNLeSC%20Project%20Presentations%2FCurrent%2FVia%20Appia&FolderCTID=0x0120004EB0DBA245A10041AA401E78745EB1B1&View={2CC9F224-02CB-49B5-9DBB-C97AE29C8572})
- [http://mappingtheviaappia.nl/3dgis/](http://mappingtheviaappia.nl/3dgis/)
- Fugro's drive-map service [website](http://www.drive-map.eu/drive-map-data/default.asp)



