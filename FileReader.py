import logging
logging.getLogger('ultrasound_kas100_fjm7')

class JSONReader:

    def __init__(self, JSONfile):
        """
        Reads JSON text file and outputs fs, c, axial_samples, num_beams, and beam_spacing.

        :param JSONfile: JSON text file
        :type JSONfile: str

        """
        import json
        f = open(JSONfile)
        data = json.load(f)

        logging.debug('reading in JSON file')
        self.fs = data["fs"]
        self.c = data["c"]
        self.axial_samples = data["axial_samples"]
        self.num_beams = data["num_beams"]
        self.beam_spacing = data["beam_spacing"]

class BinaryReader:

    def __init__(self, filename):
        """
        Reads binary data and converts 16-bits to integers

        :param filename: binary file
        :type filename: str
        """
        import numpy as np
        logging.debug('reading in binary data')
        f = open(filename, 'rb')
        self.data = np.fromfile(f, 'int16')
