# In short

- **url**: [http://ahn2.pointclouds.nl/](http://ahn2.pointclouds.nl/)
   - Works better with GPU
- **screencast**: [https://vimeo.com/154200270](https://vimeo.com/154200270) or [https://youtu.be/odLSB2rExHQ](https://youtu.be/odLSB2rExHQ)
- **contact person**: [Oscar Martinez-Rubi](https://www.esciencecenter.nl/profile/oscar-martinez-rubi-msc)
- **screenshot**:

![screenshot](/demos/ahn2/screencapture-demo-ahn2.png "AHN2 Screenshot")


# General idea of the project

The geometry of the landscape, including the objects in it, is an important input for policy making, research, and engineering. Currently, such geometry is often recorded using laser scanning or [_LiDAR_](https://en.wikipedia.org/wiki/Lidar). Typical Lidar systems are capable of millions of measurements per hour. Obviously, this generates a lot of data. To make the data output rates more manageable, it is common to filter and aggregate the data as follows. For each pulse, there are multiple reflections or _returns_: the first return is the reflection of the closest object, the second that of the second closest, etc. It is common to pick the return that has the strongest signal and throw out the other returns. The result is a _point cloud_ where each point represents the [x,y,z]-position of the strongest return. These point clouds are then typically further reduced in size by averaging all points within, say, a 1x1 m area. Note that for a relatively small country like The Netherlands, that still gives you an image of about 40000 Megapixel. For comparison, a high end camera takes pictures of about 20 Megapixel.

The work done in this project has made management and visualization of large point clouds feasible by alleviating some of the performance problems associated with LiDAR data. In this demo we focus on the visualization. To keep our problem concrete, we chose to use [the AHN2 data set](http://www.ahn.nl/index.html), a point cloud representation of The Netherlands. This data set contains about 640 billion points of first returns (see the 0.5x0.5 m 2-D aggregation [here](http://ahn.maps.arcgis.com/apps/webappviewer/index.html?id=c3c98b8a4ff84ff4938fafe7cc106e88)). We wanted to avoid aggregating as much as possible, so that our visualization is able to show as much detail as possible. Furthermore, we wanted our visualization to respect the 3-D nature of the data. This was a problem of course, because we have many more data points than screen pixels&mdash;orders of magnitude, in fact (even relative to the [resolution of the human eye](https://www.youtube.com/watch?v=4I5Q3UXkGd0) itself). We decided to visualize only those points from our data set that a user can actually see, by letting the level of detail decrease as you move away from the point of view.

This presented us with a problem because the required _multi-resolution_ 3-D data structures are not supported by any of the databases typically used for storage of point clouds (Oracle, PostgreSQL, MonetDB and LAStools). So instead, we chose to use [Potree](http://potree.org/), which uses [octrees](https://en.wikipedia.org/wiki/Octree). This worked well for smaller point clouds, but loading the data from a traditional database into Potree proved to be a performance bottleneck for larger sets: a back-of-the-envelope calculation showed that it would have taken close to a year to load the AHN2 dataset. So we developed [MassivePotree-Converter](https://github.com/NLeSC/Massive-PotreeConverter) to parallelize the loading and be done with it quicker. MassivePotree-Converter first cuts up the data into tiles, creates an octree for each tile, then merges all octrees in the final step. Executing the middle step in parallel resulted in much improved loading times.

# Demo usage

This demo visualizes the AHN2 dataset with 640 billion points using a renderer that extends the basic Potree renderer and using data structures generated with the [MassivePotree-Converter](https://github.com/NLeSC/Massive-PotreeConverter).

- Depending on the hardware used for the demo set the quality setting accordingly. To change it press the setting button (the wheel in the left bottom of the page) and select one of the four quality modes. 
- There are two navigation modes that can be toggled with the two buttons in the bottom center of the page. The first one (a Earth-globe-shaped button) is an intuitive Google-Earth like navigation while the second one (keyboard-shaped button) allows to use the keyboard (ASDWQZ keys) to navigate.
- The measurement tools can be activated by pressing the toolbox button in the left-buttom part of the page. It allows to measure measure lengths, areas, volumes in 3-space, sections, etc.
- The used colour range can be changes. The user can select different minimum and maximum height for the colouring.
- The mini-map in the upper-right part of the page shows the 2D projection of the 3D perspective view overlapped with a 2D map.
- The search box in the upper-left part of the page allows to type addresses and even use the device position to instanly visualize the position where the user is located.
- Pressing the down-arrow button in the left-bottom of the page activate the point extraction tool. The user can select any area either in the 3D scene or the 2D mini-map and download the points contained in the selected area. The user needs to provide an email. When the point extraction job is finished the user will receive a email with the link where he can download the points. Note that depending on the size of the selected area, the full-detail points are not available for download, in such cases a lower density of points is provided.
- Notice different level of detail and tiling (you can enable visualization of the octree division under ``cog wheel``>>``Misc``>>``Bounding boxes``).

## Known quirks

Besides the [general remarks](/doc/demo-usage-general-remarks.md) about web demos, this demo does not usually work well over wireless network, due to the rate at which data is requested from the server. Furthermore, the demo works much better if you have a decent GPU. Other quirks are being collected [here](/../../issues/24).

# Scientifically interesting aspects

Previous approaches required aggregating, destroying a lot of detail that could potentially be interesting, relevant, or even necessary to answer certain questions. Our approach enables inspection of points down to the highest level of detail.

- A good example of what can be done thanks to the develop tool can be appreciated in the island of Terschelling. In this 3D visualization we can appreciate erroneous points in a straight line above 300 meters of ground (probably caused by the plane scanning itself). In derived aggregated datasets and visualizations these erroneous points were not detected, and what was worse, they were aggregated and this resulted on the island being "slightly higher" than reality. In the AHN2 3D web viewer these erroneous points could be very easily spotted and they were reported to the data owner. This demonstrated that having tools for managing and visualizing massive point clouds is essential. 

# Technologically interesting aspects

- Massive-PotreeConverter
- multi-resolution structure allows viewing point clouds on multiple platforms, including smartphones, tablets, smart TVs, as well as laptops and PCs
- TODO

# Further reading

- Project [website](https://www.esciencecenter.nl/project/massive-point-clouds-for-esciences) on esciencecenter.nl
- A screencast [video](https://vimeo.com/147450441) of the demo on vimeo.com
- Browse the code [one](https://github.com/NLeSC/ahn-pointcloud-viewer), [two](https://github.com/NLeSC/Massive-PotreeConverter), [three](https://github.com/NLeSC/ahn-pointcloud-viewer-ws) on github.com
- Pitch presentations on [sharepoint](https://nlesc.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2FShared%20Documents%2FNLeSC%20Project%20Presentations%2FClosed%2FMassive%20point%20cloud%20for%20eSciences&FolderCTID=0x0120004EB0DBA245A10041AA401E78745EB1B1&View={2CC9F224-02CB-49B5-9DBB-C97AE29C8572})
- Follow-up H2020 proposal [nD-PointCloud](http://www.gdmc.nl:8080/mpc/nd-pointcloud)
- External project [website](http://pointclouds.nl)
- Final report ([pdf](https://nlesc.sharepoint.com/Shared%20Documents/NLeSC%20Project%20Presentations/Closed/Massive%20point%20cloud%20for%20eSciences/End%20Report.pdf); requires login)
- [Overview](http://www.gdmc.nl:8080/mpc/documents/papers) of papers
- Interesting [use cases](http://www.lidar-uk.com/usage-of-lidar/) of Lidar technology

