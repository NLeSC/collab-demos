
eecology demo walkthrough

# setup

1. start google earth
1. (optionally) clear browsing data
1. go to http://nlesc.github.io/eEcology-Annotation-UI/demo/demo-na.html
1. windows > reset layout
1. close 'altitude'
1. close 'temperature'
1. close 'speed'
1. close 'accelerometers'
1. in annotations, click configure classes and delete all the existing classes
1. close 'annotations' (press F11 to go full screen for this)
1. F11 again to leave fullscreen
1. exit google chrome


# demo

1. start google chrome
1. press F11 to go full screen
1. set cesium map to 2-D representation, zoom to where the data is
1. red line in Timeline widget is linked to current position in Cesium map, slide back and forth to show
1. along the track the bird's behavior is not the same everywhere, we want to investigate
1. let's see what it's doing from 00:00 till 03:00 -> input the times, click 'load tracker'
1. show 'altitude' widget
1. show 'temperature' widget
1. show 'speed' widget
1. period A = 01:19-01:24, period B = 01:35-02:15, similar behavior in altitude, speed, temperature, but is the bird's behavior the same?
1. show 'accelerometers' widget
1. grey lines in top figure correspond with burst of accelerometer data
1. show 'annotations' widget
1. click configure classes -> add
1. label the class, e.g. "floating", and pick a color or accept the default
1. in accelerometer widget, left-click 01:14:00's data, label as "floating". Same for 01:19:04 and 01:24:08. Note that the data in the Timeline and Cesium widgets get annotated automatically.
1. the accelerometer data at 01:29:12 suggests "flapping" behavior
1. in 'annotations' widget, click configure classes -> add
1. label the class, e.g. "flapping", and pick a color or accept the default
1. in accelerometer widget, left-click 01:29:22's data, label as "flapping".
1. from 01:39:12 onward, there's different behavior again, this time it's "standing"
1. in 'annotations' widget, click configure classes -> add
1. label the class, e.g. "standing", and pick a color or accept the default
1. in accelerometer widget, left-click 01:39:22's data, label as "standing". Same for 01:44:26.
1. in the timeline widget, move the mouse to the new "standing" annotation, extend it to the right by dragging
1. now that the data has been annotated, we can feed it to machine learning algorithms, for instance decision trees, and use the trained/calibrated decision tree to automatically annotate all "flapping", "standing" etc, as well as notify us of unusual behavior.













