# an unnecessarily bloated and specific test. Should be enough to cover all parts of it instead

# def test_envelope_detect():
#     from SignalManipulator import prepare_signals_for_rendering
#     from math import sin
#     import numpy as np
#
#     signal_start= 0
#     # signal_end = 100
#     signal_end = 1
#
#     fs = 100
#     data_list = np.arange(signal_start, signal_end, 1/fs)
#     margin_of_error = .1  # allow for 10% error
#     f_s_cycles = 50
#     f_s_offset = .1
#     f_s_amplitude = 1
#     s_s_cycles = 3
#     s_s_offset = 0
#     s_s_amplitude = 3
#
#     faster_signal = []
#     for data_point in data_list:
#         faster_signal.append(f_s_amplitude * sin(f_s_cycles * (data_point - f_s_offset)))
#
#     slower_signal = []
#
#     for data_point in data_list:
#         slower_signal.append(s_s_amplitude * sin(s_s_cycles * (data_point - s_s_offset)))
#
#     signal = [a * b for a, b in zip(faster_signal, slower_signal)]
#
#     signal = np.asarray(signal)
#
#     # asserting that the envelope is about constant due to multiplication of non-varying sines
#     constant_envelope = f_s_amplitude * s_s_amplitude
#     for point in prepare_signals_for_rendering([signal])[0]:
#         assert constant_envelope * (1 - margin_of_error) \
#                <= point <= \
#                constant_envelope * (1 + margin_of_error)


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


