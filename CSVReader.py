import csv

class CSVReader:

    naam = ""
    pid = []
    arrivalTime = []
    serviceTime = []
    waitingTime = []
    turnAroundTime = []
    normTurnAroundTime = []

    def __init__(self, n):
        self.naam = n

    def read_csv(self):
        output = [[], [], [], [], [], []]

        with open(self.naam) as file:
            reader = csv.reader(file)
            for each_row in reader:
                output[0].append(int(each_row[0]))
                output[1].append(int(each_row[1]))
                output[2].append(int(each_row[2]))
                output[3].append(int(each_row[3]))
                output[4].append(int(each_row[4]))
                output[5].append(float(each_row[5]))

        self.pid = output[0]
        self.arrivalTime = output[1]
        self.serviceTime = output[2]
        self.waitingTime = output[3]
        self.turnAroundTime = output[4]
        self.normTurnAroundTime = output[5]