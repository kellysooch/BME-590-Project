class JSONReader:

    def __init__(self,fs, c, axial_samples, num_beams, beam_spacing):
        self.fs = fs
        self.c = c
        self.axial_samples = axial_samples
        self.num_beams = num_beams
        self.beam_spacing = beam_spacing

    def read_json(filename):
        import json
        f = open(filename)
        data = json.load(f)
        fs = data["fs"]
        c = data["c"]
        axial_samples = data["axial_samples"]
        num_beams = data["num_beams"]
        beam_spacing = data["beam_spacing"]
        objects = fs, c, axial_samples, num_beams, beam_spacing
        return objects

class BinaryReader:

    def __init__(self, data):
        self.data = data

    def read_binary(filename):
        import numpy as np
        f = open(filename, 'rb')
        data = np.fromfile(f,'uint16')
        return data
