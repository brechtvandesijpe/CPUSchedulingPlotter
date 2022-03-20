from matplotlib import pylab, mlab
from matplotlib import pyplot as plt
import numpy as np
import CSVReader as csvr

def plot(data, percentielen, log, trend, aantalPercentielen, xname, yname):

    x, y = [], []

    if percentielen:
        xx = []
        x = list(range(aantalPercentielen))
        for i in range(len(x) - 1):
            xx.append((i + 1) * 100)
            y.append(data[((i + 1) * 100) - 1])
        y.append(data[-1])
        plt.xticks(list(range(0,101,10)))

    else:
        x = list(range(len(data)))
        y = data;

    if log:
        plt.yscale('log')

    if trend:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        pylab.plot(x, p(x), "r-")

    plt.xlabel(xname)
    plt.ylabel(yname)

    plt.plot(x, y)

reader = csvr.CSVReader("fcfsWaitingSort.txt")
reader.read_csv()

plot(reader.waitingTime, True, False, False, 100, "Service time", "Waiting time")


plt.show()