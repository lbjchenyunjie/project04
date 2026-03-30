import numpy as np
from scipy.stats import skew, kurtosis


def extract_time_features(signal):
    signal = np.array(signal)

    features = {
        "mean": float(np.mean(signal)),
        "std": float(np.std(signal)),
        "rms": float(np.sqrt(np.mean(signal ** 2))),
        "peak_to_peak": float(np.ptp(signal)),
        "max": float(np.max(signal)),
        "min": float(np.min(signal)),
        "energy": float(np.sum(signal ** 2)),
        "skewness": float(skew(signal)),
        "kurtosis": float(kurtosis(signal)),
        "zero_crossing_rate": float(((signal[:-1] * signal[1:]) < 0).sum() / len(signal))
    }

    return features