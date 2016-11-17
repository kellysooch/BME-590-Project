class Metadata:
    def __init__(self, fs, c, axial_samples, num_beams, beam_spacing):
        self.fs = fs
        self.c = c
        self.axial_samples = axial_samples
        self.num_beams = num_beams
        self.beam_spacing = beam_spacing

    def get_fs(self):
        return self.fs

    def get_c(self):
        return self.c
