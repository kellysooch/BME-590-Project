def readbinary(filename):
    import numpy as np
    f = open(filename,'rb')
    data = np.fromfile(f, 'uint16')
    return data

def test_function():
    import numpy as np
    assert np.all(readbinary("test.bin")) == np.all([1,2,3])