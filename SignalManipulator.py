import logging
logging.getLogger('ultrasound_kas100_fjm7')

WINDOW_MULTIPLIER = 2

def prepare_signals_for_rendering(multiple_beams):
    """ Manipulates the given multiple beams to perform envelope detection and otherwise manipulate the signal to be
    in a form which the display may take to display in the best form possible

    :param multiple_beams: data as list of list of data points
    :return: list of list of data points. Now in desired manipulated form
    """
    logging.debug('running the get_pretty_signal function')
    multiple_envelopes = []

    for i, single_beam in enumerate(multiple_beams):
        logging.debug('Running through single beam signal number %d', i)
        rectified_signal = abs(single_beam)
        window_size = determine_window_size(rectified_signal)
        logging.debug('window_size determined to to be %d', window_size)
        single_envelope = envelope_detect(rectified_signal, window_size)
        multiple_envelopes.append(single_envelope)

    multiple_envelopes = log_compress(multiple_envelopes)
    multiple_envelopes = account_for_distance(multiple_envelopes)
    # apply compensation for harmonic interactions
    return multiple_envelopes


def determine_window_size(rectified_signal):
    """ Determines a good window size to be used for the moving average function in detecting the envelope.

    :param rectified_signal: single beam, absolute value
    :return: returns the number of samples between peaks in rectified signal
    """
    logging.debug('running determine_window_size function')
    first_peak = first_peak_detect(rectified_signal, 1)
    second_peak = first_peak_detect(rectified_signal, first_peak + 1)
    return (second_peak - first_peak) * WINDOW_MULTIPLIER


def first_peak_detect(beam, start_point):
    """ Finds the first peak point in the signal.

    :param beam: single signal
    :param start_point: where to start in the signal looking for the peak
    :return: location of first peak
    """
    logging.debug('running first_peak_detect function')
    for i in range(start_point, len(beam)):
        logging.debug('current value of i is %d', i)
        if beam[i-1] < beam[i] > beam[i+1]:
            logging.debug('value determined to be the center of the values %d, %d, %d', beam[i-1], beam[i], beam[i+1])
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
    from math import ceil
    logging.debug('running get_envelope_front_pad function')
    front_pad = []
    current_avg = 0

    for i in range(0, ceil(sample_window/2)):
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
    return get_envelope_front_pad(rectified_signal[::-1], sample_window)[::-1][:-1]


def log_compress(multiple_envelopes):
    """ Applies logarithmic compression to the signal. Takes the log of each point in each beam as long as the
    point is not equal to zero.

    :param multiple_envelopes: list of list of data points in manipulated envelope detected form
    :type multiple_envelopes: int array
    :return: list of list of data points, now compressed
    :rtype: int array
    """
    from math import log10

    compressed_envelopes = []
    logging.debug('compressing data')
    for beam in multiple_envelopes:
        compressed_envelopes.append([log10(point) for point in beam if point !=0])

    return compressed_envelopes

def account_for_distance(compressed_envelopes):
    """ Applies signal to scale the data as the axial depth increases

    :param compressed_envelopes: list of list of data points that are compressed
    :type compressed_envelopes: int array
    :return: list of list of data points, now amplified to account for axial distance
    """
    import numpy as np

    amplified_signal = []
    logging.debug('amplifying data to account for distance')
    for beam in compressed_envelopes:
        x = np.linspace(0, len(beam), len(beam))
        y = np.sqrt(x)
        amplified_signal.append(y*beam)

    return amplified_signal


