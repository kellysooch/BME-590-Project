
class Main:

    def __init__(self):
        args = self.parse_arguments()
        self.JSONfile = args.JSONfile
        self.binfile = args.binfile

    @staticmethod
    def parse_arguments():
        import argparse as ap

        par = ap.ArgumentParser(description="ultrasound parameters",
                                formatter_class=ap.ArgumentDefaultsHelpFormatter)

        par.add_argument('--JSONfile',
                         dest='JSONfile',
                         help='filename of JSON data',
                         type=str,
                         default='bmode.json')

        par.add_argument('--binfile',
                         dest = 'binfile',
                         help='filename of binary data',
                         type = str,
                         default = 'rfdat.bin')

        args = par.parse_args()

        return args

    def read_data(self):
        from FileReader import JSONReader, BinaryReader
        jsreader = JSONReader(self.JSONfile)
        axial_samples = jsreader.axial_samples
        num_beams = jsreader.num_beams
        binreader = BinaryReader(self.binfile)
        data = binreader.data

        data_in_beams = []
        for x in range(num_beams):
            beam = data[x*axial_samples:(x+1)*axial_samples]
            data_in_beams.append(beam)
        return data_in_beams

if __name__ == "__main__":
    MyMain = Main()
    MyMain.read_data()
    # read data
    # pretty up the data
    # make image
    # render / save