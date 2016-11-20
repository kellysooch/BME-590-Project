from ImageOutputter import make_image
import matplotlib.pyplot as plt


def test_save_image():

    data_in_beams = [[0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1]]
    fs = 1
    c = 1
    axial_samples = 3
    num_beams = 4
    beam_spacing = 0.01
    image_name = 'test.png'

    image = make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing,image_name, do_save=True,
                       do_display=False)

    assert image == plt.savefig('test.png', format='png')