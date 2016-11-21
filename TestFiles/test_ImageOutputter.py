def test_save_image():
    from ImageOutputter import make_image
    import os

    data_in_beams = [[0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1]]
    fs = 1
    c = 1
    axial_samples = 3
    num_beams = 4
    beam_spacing = 0.01
    image_name = 'test.png'

    make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing,image_name, do_save=True,
                       do_display=False)

    assert os.path.isfile('test.png') is True