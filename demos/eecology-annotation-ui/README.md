# In short

- **url**: [http://nlesc.github.io/eEcology-Annotation-UI/demo/demo-na.html](http://nlesc.github.io/eEcology-Annotation-UI/demo/demo-na.html)
   - IP-whitelisting: No. The gull data is publicly available
   - GPU: Not required, but it does help
   - Login required: No
   - Database: No performance problems
- **screencast**: [https://vimeo.com/158029473](https://vimeo.com/158029473)
- **contact person**: [Stefan Verhoeven](https://www.esciencecenter.nl/profile/ing.-stefan-verhoeven)
- **screenshot**:

![screenshot](/demos/eecology-annotation-ui/screenshots/screenshot-33.png "eecology-annotation-ui demo screenshot")


# General idea of the project

This demo is part of a larger effort to better understand bird migration. Traditionally, bird migration is studied by expert observers who go out into the field to observe birds at their stopover sites, nests, colonies, or other sites that are known to be important. Due to the nature of the observation process, it is difficult to answer certain research questions, e.g. with respect to:

- night-time behavior
- foraging behavior
- energy expenditure
- travel time of migration
- response to environmental factors such as rain storms during flight
- densities of bird migration

The e-Ecology project aims to address some of these problems by integrating two new sources of data into the traditional workflow:

1. custom-made GPS tracking devices to study individual birds
1. Doppler-capable weather radars to observe density of migration

This repository/demo pertains to the former.

_About the GPS tracker_

- solar powered with battery
- GPS sensor, accelerometer [(:sound:)](http://static.sfdict.com/staticrep/dictaudio/A00/A0054100.mp3), temperature, and other sensors
- automatic download of data to base stations
- enough storage to measure at very high frequency for long periods of time
- measurement schedule can be updated while the bird flying
- web application to manage trackers remotely from 1000s of kilometers away


# Demo usage

For a storyline, look [here](/demos/eecology-annotation-ui/storyline.md). **Known quirks** are being collected in [this](/../../issues/23) issue. See also the [general remarks](/doc/demo-usage-general-remarks.md) about web demos.


# Scientifically interesting aspects

New insights about behavior of individual birds:

   - response to rain storms
   - response to dust storms
   - response to wind direction at different altitudes
   - anthropogenic effects: landfills, water treatment plants
   - foraging area:
      - some gulls forage from The Netherlands all the way to England
      - oyster catchers from different colonies do not forage at another colony's feeding grounds
   - how birds utilize local wind effects to minimize energy expenditure, for example by using the updraft along coastal dunes
   - finding mate/fidelity
   - sleeping/resting behavior while floating at sea
   - interactive discovery using the web application


# Technologically interesting aspects

- tracker
- bringing together data sources in one web application
- machine learning to automatically recognize (anomalous, previously unknown) bird behavior
- remote administration of trackers


# Further reading

- Project [website](https://www.esciencecenter.nl/project/eecology) on esciencecenter.nl
- Project [video](https://vimeo.com/106796321) on vimeo.com
- A screencast [video](https://vimeo.com/158029473) of the demo on vimeo.com
- Browse [the code](https://github.com/NLeSC/eEcology-Annotation-UI) on github.com
- Pitch presentations on [sharepoint](https://nlesc.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2FShared%20Documents%2FNLeSC%20Project%20Presentations%2FCurrent%2FeEcology&FolderCTID=0x0120004EB0DBA245A10041AA401E78745EB1B1&View={2CC9F224-02CB-49B5-9DBB-C97AE29C8572})
- [http://www.uva-bits.nl/](http://www.uva-bits.nl/)
- [http://enram.eu/](http://enram.eu/)
- Nederland van Boven [video](https://vimeo.com/85808414) about migration of Honey Buzzards
