# if __name__ == "__main__":
from FileReader import JSONReader, BinaryReader
objects = JSONReader.read_json("bmode.json") # objects contain fs, c, axial_samples, num_beams, beam_spacing
data = BinaryReader.read_binary("rfdat.bin") # contains array of data converted from binary to int
    # read data
    # pretty up the data
    # make image
    # render / save