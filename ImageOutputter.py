import logging
logging.getLogger('ultrasound_kas100_fjm7')

def make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing, do_save, do_display):
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
        plt.savefig('image.png', format='png')
    if do_display:
        plt.show()
