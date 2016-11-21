import logging
from sys import exit
logging.getLogger('ultrasound_kas100_fjm7')


class JSONReader:

    def __init__(self, JSONfile):
        """
        Reads JSON text file and outputs fs, c, axial_samples, num_beams, and beam_spacing.

        :param JSONfile: JSON text file
        :type JSONfile: str

        """
        import json
        try:
            f = open(JSONfile)
        except FileNotFoundError:
            logging.error('The JSON file of that name does not exist')
            exit('No such JSON file')

        data = json.load(f)

        logging.debug('reading in JSON file')
        try:
            self.fs = data["fs"]
            self.c = data["c"]
            self.axial_samples = data["axial_samples"]
            self.num_beams = data["num_beams"]
            self.beam_spacing = data["beam_spacing"]
        except KeyError:
            logging.error('The data specified in the JSON file is incomplete')
            exit('JSON file is incomplete')


class BinaryReader:

    def __init__(self, filename):
        """
        Reads binary data and converts 16-bits to integers

        :param filename: binary file
        :type filename: str
        """
        import numpy as np
        logging.debug('reading in binary data')
        try:
            f = open(filename, 'rb')
        except FileNotFoundError:
            logging.error('binary file was not found')
            exit('no such binary file')

        self.data = np.fromfile(f, 'int16')
