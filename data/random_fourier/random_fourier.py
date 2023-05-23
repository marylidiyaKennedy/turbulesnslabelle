"""
Generated using ChatGPT
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import savemat

def generate_random_signal(lower_freq, upper_freq, duration, sample_rate, num_components):
    """
    Generates a time signal with random Fourier composition within the given frequency range.

    Args:
        lower_freq (float): Lower bound for frequencies.
        upper_freq (float): Upper bound for frequencies.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Number of samples per second (sampling rate).

    Returns:
        numpy.ndarray: Generated time signal.
    """
    num_samples = int(duration * sample_rate)
    time = np.linspace(0, duration, num_samples)
    signal = np.zeros(num_samples)

    for _ in range(num_components):
        freq = np.random.uniform(lower_freq, upper_freq)
        phase = np.random.uniform(0, 2 * np.pi)
        amplitude = np.random.uniform(0.1, 1.0)
        component = amplitude * np.sin(2 * np.pi * freq * time + phase)
        signal += component

    return signal

if __name__ == "__main__":
    lower_freq = 5      # Lower bound for frequencies
    upper_freq = 20     # Upper bound for frequencies
    duration = 1        # Duration of the signal in seconds
    sample_rate = 500   # Number of samples per second (sampling rate)
    num_components = 5  # Random number of Fourier components


    # Generate the random signal
    signal = generate_random_signal(lower_freq, upper_freq, duration, sample_rate, num_components)

    # Plot the signal
    time = np.linspace(0, duration, len(signal))
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Random Signal')
    plt.show()

    # Save the signal as a matfile
    savemat("random_signal.mat", {"signal": signal})
