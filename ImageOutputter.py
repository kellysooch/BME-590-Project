
def make_image(data_in_beams, fs, c, axial_samples, num_beams, beam_spacing, do_save, do_display):
    # manipulate axes
    import numpy as np
    import matplotlib.pyplot as plt

    Matrix = np.zeros(num_beams, axial_samples)
    for beam in data_in_beams:
        for point in beam:
            Matrix[beam.index()][point.index()] = point

    X = np.linspace(0, beam_spacing*num_beams, num_beams)
    Y = np.linspace(0, (axial_samples/fs)*c, axial_samples)
    Z = Matrix
    xx, yy = np.meshgrid(X, Y)
    plt.pcolormesh(xx, yy, Z)

    if do_save:
        plt.savefig('image.png', format='png')
    if do_display:
        plt.show()
