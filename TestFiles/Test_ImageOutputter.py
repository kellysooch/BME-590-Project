from ImageOutputter import make_image
import matplotlib.pyplot as plt
from Main import prepared_data_in_beams, metadata

import pytest
@pytest.mark.mpl_image_compare
def test_plot_basic():
    array = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            array[i][j] = i * j
    return ip.make_image(array, display=False, save=False)
