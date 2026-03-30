import numpy as np
from scipy.signal import butter, filtfilt, medfilt


def butter_lowpass_filter(data, cutoff=3.0, fs=100.0, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    return filtfilt(b, a, data)


def butter_highpass_filter(data, cutoff=0.5, fs=100.0, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="high", analog=False)
    return filtfilt(b, a, data)


def butter_bandpass_filter(data, lowcut=0.5, highcut=5.0, fs=100.0, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, data)


def moving_average(data, window_size=5):
    if window_size < 1:
        return data
    kernel = np.ones(window_size) / window_size
    return np.convolve(data, kernel, mode="same")


def median_denoise(data, kernel_size=5):
    if kernel_size % 2 == 0:
        kernel_size += 1
    return medfilt(data, kernel_size=kernel_size)