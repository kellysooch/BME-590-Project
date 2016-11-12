class JSONReader:

    def read_json(self):
        return #class that is Metadata

class BinaryReader:

    def read_binary(self):
        f = open(filename, 'rb')
        data = np.fromfile(f,'uint16')
        return data
