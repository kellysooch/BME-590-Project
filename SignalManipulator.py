def get_pretty_signal(multiple_beams):
    multiple_envelopes = []

    for single_beam in multiple_beams:
        rectified_signal = abs(single_beam)
        window_size = determine_window_size(rectified_signal)
        single_envelope = envelope_detect(rectified_signal, window_size)
        multiple_envelopes.append(single_envelope)

    # apply log compression
    # apply compensation for distance
    # apply compensation for harmonic interactions
    return multiple_envelopes


def determine_window_size(rectified_signal):
    first_peak = first_peak_detect(rectified_signal)
    second_peak = first_peak_detect(rectified_signal[(first_peak+1):])
    return second_peak - first_peak


def first_peak_detect(beam):
    for i in range(1, len(beam)):
        if beam[i-1] < beam[i] < beam[i+1]:
            return i


def envelope_detect(rectified_signal, sample_window):
    envelope = []
    first_total = 0
    for data in rectified_signal[:sample_window]:
        first_total += data

    average = first_total / sample_window

    envelope.append(average)

    for i in range(0, len(rectified_signal) - sample_window):
        average -= rectified_signal[i] / sample_window
        average += rectified_signal[sample_window+i] / sample_window
        envelope.append(average)

    return get_envelope_front_pad(rectified_signal, sample_window) +\
        envelope +\
        get_envelope_back_pad(rectified_signal, sample_window)


def get_envelope_front_pad(rectified_signal, sample_window):
    front_pad = []
    current_avg = 0

    for i in range(0, sample_window):
        current_avg *= i
        current_avg += rectified_signal[i]
        current_avg /= i+1

        front_pad.append(current_avg)

    return front_pad


def get_envelope_back_pad(rectified_signal, sample_window):
    return get_envelope_front_pad(rectified_signal.reverse(), sample_window).reverse()
