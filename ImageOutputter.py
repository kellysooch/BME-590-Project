import logging
logging.getLogger('ultrasound_kas100_fjm7')


def make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing, image_name, do_save, do_display):
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
    :param do_save: Boolean logic if user wants to save image to png, default=True
    :param do_display: Boolean logic if user wants to display image, default=True
    :param image_name: filename of B-mode png image, default=bmode.png
    :return: a displayed and/or saved image
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import exposure

    logging.debug('putting data into 2d array')
    matrix = np.zeros((axial_samples, num_beams))
    logging.debug('num_beams = %d\n axial_samples = %d\n length of beams = %d\n length of samples = %d',
                  num_beams, axial_samples, len(data_in_beams), len(data_in_beams[0]))
    for i, beam in enumerate(data_in_beams):
        for j, point in enumerate(beam):
            matrix[len(beam) - 1 - j][len(data_in_beams) - 1 - i] = point
    logging.debug('setting axes, x=Lateral, y=Axial')

    X = np.linspace(0, beam_spacing*num_beams, num_beams)
    Y = np.linspace(0, (axial_samples/fs)*c, axial_samples)
    Z = matrix

    logging.debug('creating Ultrasound image with pcolormesh')
    xx, yy = np.meshgrid(X, Y)
    plt.pcolormesh(xx, yy, Z, cmap="gray")
    plt.ylabel("Axial distance (meters)")
    plt.xlabel("Lateral distance (meters)")
    plt.axis([0, 0.03, 0, 0.06])

    if do_save:
        logging.debug('saving image')
        plt.savefig(image_name, format='png')
    if do_display:
        logging.debug('displaying image')
        plt.show()
