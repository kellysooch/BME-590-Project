Description:

This project is run from Main.py. The file includes the input argument parser, and it has a function for reading
in the data from FileReader.py and structuring the data into a list of beams. First, the data is read,
using as inputs the filename that the user can specify or change from the default, and then the signal is
cleaned up (envelope detection, logarithmic compression, time gain compensation, and harmonics compensation),
and then the image is created.

Imported packages:

- matplotlib.pyplot
- os
- numpy

How to Use:

Run Main.py. Make sure the binary file and JSON file are in the directory.

