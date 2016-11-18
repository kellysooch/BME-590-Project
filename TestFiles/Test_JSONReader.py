
def test_read_json():
    from FileReader import JSONReader
    assert JSONReader("bmode.json").fs == 40000000
    assert JSONReader("bmode.json").c == 1540
    assert JSONReader("bmode.json").axial_samples == 1556
    assert JSONReader("bmode.json").beam_spacing == 0.00011746274509803921
    assert JSONReader("bmode.json").num_beams == 256

