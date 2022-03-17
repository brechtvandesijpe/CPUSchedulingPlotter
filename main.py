import matplotlib.pyplot as plt
import csv

def read_csv():
    output = [[],[]]

    with open("data.txt") as file:
        reader = csv.reader(file)
        for each_row in reader:
            output[0].append(int(each_row[0]))
            output[1].append(float(each_row[1]))

    return output;

data = read_csv()

x = data[0]
y = data[1]

x2 = []
y2 = []

x.sort()

for i in range(len(x)):
    x[i] /= len(x)
    x[i] *= 100

    if x[i] >= 90:
        x2.append(x[i])
        y2.append(y[i])

plt.plot(x2,y2)
plt.show()

print(y)