class JSONReader:

    def __init__(self, JSONfile):
        import json
        f = open(JSONfile)
        data = json.load(f)

        self.fs = data["fs"]
        self.c = data["c"]
        self.axial_samples = data["axial_samples"]
        self.num_beams = data["num_beams"]
        self.beam_spacing = data["beam_spacing"]

class BinaryReader:

    def __init__(self, filename):
        import numpy as np
        f = open(filename, 'rb')
        self.data = np.fromfile(f, 'int16')

