def test_binary_reader():
    from FileReader import BinaryReader
    import numpy as np

    assert np.all(BinaryReader("test.bin").data) == np.all([1,2,3])