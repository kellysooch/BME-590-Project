
def test_read_json():
    from FileReader import JSONReader
    import numpy as np
    assert JSONReader("bmode.json").fs == 40000000
