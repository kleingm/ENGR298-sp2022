
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows


ekg_data = np.loadtxt(path, skiprows=2, delimiter=",")


# save each vector as own variable
# load raw time
# Time = np.loadtxt('../data/ekg/mitdb_201.csv', skiprows=2, usecols=0)
# load time variable
Time = ekg_data[:, 0]

# load voltage variable
volts = ekg_data[:, 2]


# use matplot lib to generate a single plot
# Using numpy and matplotlib, load a dataset from ekg_data.
# Plot the first 10 seconds of a signal. Apply appropriate labels and title to figure. Upload code and figure.

plt.xlim([0,10])
plt.plot(Time, volts)
plt.xlabel("Time (s)")
plt.ylabel("raw voltage")
plt.title("Raw Heartbeat Data")
plt.show()