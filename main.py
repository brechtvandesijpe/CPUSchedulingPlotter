from matplotlib import pylab
from matplotlib import pyplot as plt
import numpy as np
from numpy import array
from scipy.interpolate import *
import CSVReader as csvr

def plotGrafiek(datax, datay, percentielen, log, trend, aantalPercentielen, xname, yname, title):

    x, y = [], []

    if percentielen:
        for i in range(len(datax)):
            x.append(i / 100)
            y.append(datay[i])

        '''xx = []
        x = list(range(aantalPercentielen))
        for i in range(len(x) - 1):
            xx.append((i + 1) * 100)
            y.append(data[((i + 1) * 100) - 1])
        y.append(data[-1])
        #x.pop(-1)
        plt.xticks(list(range(0,101,10)))

    else:
        x = list(range(len(data)))
        y = data'''

    if log:
        plt.yscale('log')

    if trend:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        pylab.plot(x, p(x), "r-")

    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)

    plt.scatter(x, y, s=0.2)

# naam = ["fcfsServiceSort10k.txt", "fcfsServiceSort20k.txt", "fcfsServiceSort50k.txt"]

'''for i in range(len(naam)):
    reader = csvr.CSVReader(naam[i])
    reader.read_csv()
    plotGrafiek(reader.serviceTime, reader.waitingTime, True, False, True, 100, "Service time", "Waiting time", naam[i]) #
    plt.show()
    plotGrafiek(reader.serviceTime, reader.normTurnAroundTime, True, True, False, 100, "Service time", "Normalized turnaround time", naam[i])
    plt.show()'''

naam = "fcfsServiceSort10k.txt"
reader = csvr.CSVReader(naam)
reader.read_csv()
# plotGrafiek(reader.serviceTime, reader.normTurnAroundTime, True, True, False, 100, "Service time", "Normalized turnaround time", naam)
# p =
# plt.plot(range(len(reader.serviceTime)), p)
plt.show()