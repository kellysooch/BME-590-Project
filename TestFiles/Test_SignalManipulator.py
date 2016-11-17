def test_envelope_detect():
    from math import sin

    signal_start= 0
    signal_end = 100
    fs = 100
    data_list = range(signal_start, signal_end, 1/fs)
    margin_of_error = .1  # allow for 10% error
    faster_signal_cycles = 50
    faster_signal_offset = .1
    faster_signal_amplitude = 1
    slower_signal_cycles = 3
    slower_signal_offset = 0
    slower_signal_amplitude = 3
    positive_offset = 10

    faster_signal = faster_signal_amplitude * sin(faster_signal_cycles(data_list - faster_signal_offset)) + positive_offset
    slower_signal =

    signal_
