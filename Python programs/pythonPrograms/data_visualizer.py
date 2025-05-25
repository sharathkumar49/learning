# Data Visualizer (matplotlib/seaborn, e.g., plot CSV data)
import matplotlib.pyplot as plt
import csv

def plot_csv(filename):
    x, y = [], []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            x.append(row[0])
            y.append(float(row[1]))
    plt.plot(x, y)
    plt.xlabel(header[0])
    plt.ylabel(header[1])
    plt.title('CSV Data Plot')
    plt.show()

if __name__ == "__main__":
    fname = input("Enter CSV filename: ")
    plot_csv(fname)
