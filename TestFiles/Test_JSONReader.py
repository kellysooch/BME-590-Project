
def readjson(filename):
    import json
    f = open(filename)
    data = json.load(f)
    fs = data["fs"]
    c = data["c"]
    return fs, c

def test_function():
    import numpy as np
    assert np.all(readjson("bmode.json")) == np.all([40000000, 1540])
