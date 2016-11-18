from SignalManipulator import prepare_signals_for_rendering


class Main:

    def __init__(self):
        """ Initializer method for main. Creates the necessary parameters for other functions to access. Uses the
        argparse parameters that the user inputs and assigns them to the proper variables.
        """
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
        """
        Uses the JSONReader and BinaryReader modules to read the RF binary data containing the samples and convert
        to integers, and uses the parameters from the JSONReader to structure the data into separate beams.

        :return: data_in_beams is the input data separated into its lateral beams
        :rtype: int array
        """
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
    data_in_beams = MyMain.read_data()
    prepare_signals_for_rendering(data_in_beams)
    # pretty up the data
    # make image
    # render / save