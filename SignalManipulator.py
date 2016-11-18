import logging
logging.getLogger('ultrasound_kas100_fjm7')


def get_pretty_signal(multiple_beams):
    """ Manipulates the given multiple beams to perform envelope detection and otherwise manipulate the signal to be
    in a form which the display may take to display in the best form possible

    :param multiple_beams: data as list of list of data points
    :return: list of list of data points. Now in desired manipulated form
    """
    logging.debug('running the get_pretty_signal function')
    multiple_envelopes = []

    for single_beam in multiple_beams:
        logging.debug('Running through a single beam signal')
        rectified_signal = abs(single_beam)
        window_size = determine_window_size(rectified_signal)
        logging.debug('window_size determined to to be %d', window_size)
        single_envelope = envelope_detect(rectified_signal, window_size)
        multiple_envelopes.append(single_envelope)

    # apply log compression
    # apply compensation for distance
    # apply compensation for harmonic interactions
    return multiple_envelopes


def determine_window_size(rectified_signal):
    """ Determines a good window size to be used for the moving average function in detecting the envelope.

    :param rectified_signal: single beam, absolute value
    :return: returns the number of samples between peaks in rectified signal
    """
    logging.debug('running determine_window_size function')
    first_peak = first_peak_detect(rectified_signal, 1)
    second_peak = first_peak_detect(rectified_signal, first_peak)
    return second_peak - first_peak


def first_peak_detect(beam, start_point):
    """ Finds the first peak point in the signal.

    :param beam: single signal
    :param start_point: where to start in the signal looking for the peak
    :return: location of first peak
    """
    logging.debug('running first_peak_detect function')
    for i in range(start_point, len(beam)):
        logging.debug('current value of i is %d', i)
        if beam[i-1] < beam[i] < beam[i+1]:
            return i


def envelope_detect(rectified_signal, sample_window):
    """ Applies a moving average to the given signal. This is effectively a low-pass filter.

    :param rectified_signal: single beam, absolute value
    :param sample_window: desired moving average window
    :return: signal after envelope detection algorithm
    """
    logging.debug('running envelope_detect function')
    envelope = []
    first_total = 0
    for data in rectified_signal[:sample_window]:
        first_total += data

    average = first_total / sample_window

    envelope.append(average)

    for i in range(0, len(rectified_signal) - sample_window):
        logging.debug('current value of i is %d', i)
        average -= rectified_signal[i] / sample_window
        average += rectified_signal[sample_window+i] / sample_window
        envelope.append(average)

    return get_envelope_front_pad(rectified_signal, sample_window) +\
        envelope +\
        get_envelope_back_pad(rectified_signal, sample_window)


def get_envelope_front_pad(rectified_signal, sample_window):
    """ Returns first few points which are not able to be created with the full moving average average algorithm.
    Does so by continually averaging the given points.

    :param rectified_signal: single beam, absolute value
    :param sample_window: desired moving average window
    :return: missing points to pad the begging of the envelope detection points
    """
    logging.debug('running get_envelope_front_pad function')
    front_pad = []
    current_avg = 0

    for i in range(0, sample_window):
        logging.debug('current value of i is %d', i)
        current_avg *= i
        current_avg += rectified_signal[i]
        current_avg /= i+1

        front_pad.append(current_avg)

    return front_pad


def get_envelope_back_pad(rectified_signal, sample_window):
    """ Returns last few points which are not able to be created with the full moving average average algorithm.
    Does so by continually averaging the given points.

    :param rectified_signal: single beam, absolute value
    :param sample_window: desired moving average window
    :return: missing points to pad the end of the envelope detection points
    """
    logging.debug('running get_envelope_back_pad function')
    return get_envelope_front_pad(rectified_signal.reverse(), sample_window).reverse()
