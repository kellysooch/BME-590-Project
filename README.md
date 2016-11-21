Assignment #5: Ultrasound
=========================

Contributors: Kelly Sooch, Filip Mazurek

Description
-----------
This project is run from Main.py. The file includes the input argument parser, and it has a function for reading
in the data from FileReader.py and structuring the data into a list of beams. First, the data is read,
using as inputs the filename that the user can specify or change from the default, and then the signal is
cleaned up (envelope detection, logarithmic compression, time gain compensation, and harmonics compensation),
and then the image is created.

The cleaning of the signal uses envelope detection through a moving average. The process is as follows:
1. The list of individual signals is split up.
2. Each signal is rectified.
3. A new moving average window size is quickly determined for each signal through peak detection
4. The envelope is created by the moving average strategy
5. The signal is logarithmically compressed. This compensates for the extreme signal reactions.
6. The signal quadratically accounts for distance weakening.
7. The signal accounts for harmonic interaction by the gaussian function.

The cleaned up signal is then passed into the image creation, and the image is created using pcolormesh.

Imported packages
-----------------
- matplotlib.pyplot
- os
- numpy

How to Use
----------
Run Main.py. If using custom data, please ensure that the binary file and JSON file are in the directory.
