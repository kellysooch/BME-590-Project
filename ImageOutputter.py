import logging
logging.getLogger('ultrasound_kas100_fjm7')

def make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing, do_save, do_display):
    """
    Creates Ultrasound image using pcolormesh, taking as inputs the data in beams and the parameters from the JSON file,
    as well as allowing the user to specify whether they want to save, display, or save and display image. The function
    first creates a 2d array of the data, with the columns as beams and the rows as axial depth. Then, the meshgrid is
    created, manipulating the axes such that axial depth will be the y-axis, and lateral distance will be the x-axis.

    :param data_in_beams: data as list of list of data points in a single beam
    :param fs: sampling frequency (Hz)
    :param c: sound speed (m/s)
    :param axial_samples: number of samples in beam
    :param num_beams: number of lateral beams
    :param beam_spacing: space between beams
    :param do_save: Boolean logic if user wants to save image to png
    :param do_display: Boolean logic if user wants to display image
    :return: a displayed and/or saved image
    """
    import numpy as np
    import matplotlib.pyplot as plt

    logging.debug('putting data into 2d array')
    Matrix = np.zeros(num_beams, axial_samples)
    for i, beam in enumerate(data_in_beams):
        for j,point in enumerate(beam):
            Matrix[i][j] = point

    logging.debug('setting axes, x=Lateral, y=Axial')
    X = np.linspace(0, beam_spacing*num_beams, num_beams)
    Y = np.linspace(0, (axial_samples/fs)*c, axial_samples)
    Z = Matrix

    logging.debug('creating Ultrasound image with pcolormesh')
    xx, yy = np.meshgrid(X, Y)
    plt.pcolormesh(xx, yy, Z)

    if do_save:
        logging.debug('saving image')
        plt.savefig('image.png', format='png')
    if do_display:
        logging.debug('displaying image')
        plt.show()

