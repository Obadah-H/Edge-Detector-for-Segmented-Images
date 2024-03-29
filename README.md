# Edge Detector for Segmented Images
Once, I had to train an edge detector with a database which contained images and their segmentations instead of edges. As a lazy person, I googled for something ready to convert them to edges, but didn't find anything. So, I wrote this script.

## Features
* "Detect" edges of segmented images
* "Detect" edges of a specific segment (detect a car or person for example)
* Choose the thickness of edges
* Increase the thickness of detected edges (Whether the input is a segmented image or an edges-detected image)

### Parameters

  
* input_folder: folder which contains the images
* output_folder: Where to save output images
* thickness: Thickness of line
* select_object: Whether to draw edges for a specific object
* selected_object: The color of object to "detect" in case select_object=True

### Thickness
The square way of choosing the pixels is used to express the thickness.

<p align="center"> <img src="https://github.com/Obadah-H/Edge-Detector-for-Segmented-Images/blob/master/README_files/thickness.png?raw=true"> </p>

### Example

This example shows the output of edge detection of a segmented image, and the output when detecting cars only.

<img src="https://github.com/Obadah-H/Edge-Detector-for-Segmented-Images/blob/master/input/2.png?raw=true" width="290" height="217"> <img src="https://github.com/Obadah-H/Edge-Detector-for-Segmented-Images/blob/master/output/2.png?raw=true" width="290" height="217"> <img src="https://github.com/Obadah-H/Edge-Detector-for-Segmented-Images/blob/master/output_cars/2.png?raw=true" width="290" height="217">

## License
GNU General Public License v3.0
