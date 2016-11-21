def test_determine_window_size():
    from SignalManipulator import determine_window_size
    signal = [0, 1, 0, 0, 1, 0, 0, 0]

    assert determine_window_size(signal) == 6  # window size is twice the space between peaks


def test_first_peak_detection():
    from SignalManipulator import first_peak_detect
    signal = [0, 0, 0, 1, 0]

    assert first_peak_detect(signal, 0) == 3


def test_envelope_detect():
    """ envelope detection is moving average in this case. Test employs easy human-checkable tests
    """
    from SignalManipulator import envelope_detect
    signal = [0, 2, 0, 2, 0, 2, 0]

    one_envelope = envelope_detect(signal, 1)
    two_envelope = envelope_detect(signal, 2)

    assert one_envelope == signal
    assert two_envelope == [0, 1, 1, 1, 1, 1, 1]  # because padding is only added to the front


def test_get_envelope_pad():
    from SignalManipulator import get_envelope_back_pad
    from SignalManipulator import get_envelope_front_pad

    signal = [0, 1, 2, 0, 0, 0, 0, 2, 1, 0]
    window = 7  # so that first window / 2 samples are in the pad

    front_padding = get_envelope_front_pad(signal, window)
    correct_padding = [0, 0.5, 1]

    assert front_padding == correct_padding

    back_padding = get_envelope_back_pad(signal, window)

    assert back_padding[::-1] == front_padding

def test_log_compress():
    """ log_compress uses base 10 log compression. Exploit that to ensure it is correct
    """
    from SignalManipulator import log_compress

    zero_power_list = [1]
    one_power_list = [10]
    two_power_list = [100]
    three_power_list = [1000]
    compound_list = [zero_power_list, one_power_list, two_power_list, three_power_list]

    result = log_compress(compound_list)

    assert result[0] == [0]
    assert result[1] == [1]
    assert result[2] == [2]
    assert result[3] == [3]

def test_account_for_distance():
    """test that multiplying the square root of the data by the data results in a correct amplified
    signal
    """
    from SignalManipulator import account_for_distance
    import numpy as np

    test_data = [[1, 4, 9],[1,4,9]]
    new_data = [[1*np.sqrt(1), 4*np.sqrt(2), 9*np.sqrt(3)], [1*np.sqrt(1), 4*np.sqrt(2), 9*np.sqrt(3)]]

    assert np.all(account_for_distance(test_data)) == np.all(new_data)

def test_account_for_harmonics():
    """test that multiplies signal by a bell curve to account for harmonics
    """
    from SignalManipulator import account_for_harmonics
    import numpy as np

    test_data = [[1,1,1], [1,1,1]]
    x = np.linspace(-0.015, 0.015, 3)
    mu = 3
    sig = 6
    new_data = [[np.exp(-np.power(x - mu, 2) / (2 * np.power(sig, 2)))],
                [np.exp(-np.power(x - mu, 2) / (2 * np.power(sig, 2)))]]

    assert np.all(account_for_harmonics(test_data)) == np.all(new_data)