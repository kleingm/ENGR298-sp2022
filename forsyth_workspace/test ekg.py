
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
# import the CSV file using numpy
path = '../data/ekg/mitdb_201.csv'


# load data in matrix from CSV file; skip first two rows
file = open(path)
# read the header
header = file.readline()
# read the units
units = file.readline()
# create new variable ekg_data
ekg_data = np.loadtxt(file, skiprows=0, delimiter=",")


# save each vector as own variable
# load raw time
Time = ekg_data[:, 0]
# load voltage variable
volts = ekg_data[:, 2]


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = scipy.signal.lfilter(b, a, data)
    return y

    # Sample rate and desired cutoff frequencies (in Hz).
    # F1 score of  for 201


if database_name := 'mitdb_219':
    fs = 70
    lowcut = 0.43
    highcut = 2
    order = 5

    # Filter EKG data
    filtered = butter_bandpass_filter(volts, lowcut, highcut, fs, order)

    # pass data through differentiator
    diffvolt = np.diff(filtered)
    diffvolt_2 = np.insert(diffvolt, [0], [0])

    # pass data through square function
    squared = np.square(diffvolt_2)

    # pass through moving average window
    mov_avg = 2*np.convolve(squared, 1)
    # use matplotlib to generate figures for each intermediate signal
    # you may wish to example the sampling rate for your selected file
    # to determine how many points for each vector to plot
    signal = mov_avg

    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result
    peaks, _ = scipy.signal.find_peaks(signal, distance=90, height=0.0014)

plt.xlim([0, 10])
plt.ylim([0, 0.05])
# plt.plot(Time, volts)
plt.grid(True)
# plt.plot(Time, diffvolt_2)
# plt.plot(Time, squared)
plt.plot(Time, signal)
plt.xlabel("Time (s)")
plt.ylabel("manipulated voltage data")
plt.show()
