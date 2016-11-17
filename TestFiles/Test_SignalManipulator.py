def test_envelope_detect():
    from SignalManipulator import envelope_detect
    from math import sin

    signal_start= 0
    signal_end = 100
    fs = 100
    data_list = range(signal_start, signal_end, 1/fs)
    margin_of_error = .1  # allow for 10% error
    f_s_cycles = 50
    f_s_offset = .1
    f_s_amplitude = 1
    s_s_cycles = 3
    s_s_offset = 0
    s_s_amplitude = 3
    positive_offset = 10

    faster_signal = []
    for data_point in data_list:
        faster_signal.append(f_s_amplitude * sin(f_s_cycles * (data_point - f_s_offset)))

    slower_signal = []

    for data_point in data_list:
        slower_signal.append(s_s_amplitude * sin(s_s_cycles * (data_point - s_s_offset)))

    signal = [a * b + positive_offset for a, b in zip(faster_signal, slower_signal)]

    # asserting that the envelope is about constant due to multiplication of non-varying sines
    constant_envelope = positive_offset + f_s_amplitude * s_s_amplitude
    for(point in envelope_detect(signal)):
        assert constant_envelope * (1 - margin_of_error) \
               <= point <= \
               constant_envelope * (1 + margin_of_error)
