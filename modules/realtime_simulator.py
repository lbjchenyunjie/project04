import numpy as np


def generate_squat_signals(n_points=500):
    x = np.linspace(0, 10, n_points)
    signal_1 = np.sin(2 * np.pi * 0.8 * x) + 0.08 * np.random.randn(n_points)
    signal_2 = 0.8 * np.sin(2 * np.pi * 1.2 * x + 0.5) + 0.08 * np.random.randn(n_points)
    signal_3 = 0.6 * np.sin(2 * np.pi * 1.6 * x + 1.0) + 0.08 * np.random.randn(n_points)
    signal_4 = 0.9 * np.sin(2 * np.pi * 0.5 * x + 0.2) + 0.08 * np.random.randn(n_points)

    return {
        "x": x,
        "通道1": signal_1,
        "通道2": signal_2,
        "通道3": signal_3,
        "通道4": signal_4,
    }


def generate_pressure_map(rows=8, cols=8):
    return np.random.rand(rows, cols)