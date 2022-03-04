
import matplotlib.pyplot as plt
import numpy as np

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

# pass data through LOW PASS FILTER (OPTIONAL)
# your code here

# pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result
# your code here


# pass data through differentiator
diffvolt = np.diff(volts)
diffvolt_2 = np.insert(diffvolt, [0], [0])

# pass data through square function
squared = np.square(diffvolt_2)

# pass through moving average window
mov_avg = np.convolve(squared, 1)
# use matplotlib to generate figures for each intermediate signal
# you may wish to example the sampling rate for your selected file
# to determine how many points for each vector to plot

# sample a signal at a given rate (Hz)
# sample_rate = 1000

# determine the sample period
# period = 1/sample_rate
# time = np.arange(0, 10, period)
plt.xlim([0, 10])
# plt.ylim([0, 10000])
plt.plot(Time, volts)
plt.grid([])
plt.plot(Time, diffvolt_2)
plt.plot(Time, squared)
plt.plot(Time, mov_avg)
plt.xlabel("Time (s)")
plt.ylabel("manipulated voltage data")
plt.show()
