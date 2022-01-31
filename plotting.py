import matplotlib.pyplot as plt


# still need to update the date axis - to be readable
def plot(date, data1, index, prediction1, name):
    fig, ax = plt.subplots()
    line1, = ax.plot(date, data1, label="Original data of {}".format(name))
    line2, = ax.plot(index, prediction1, label="Prediction of {}".format(name))
    ax.set(xlabel='Time', ylabel=str(name))
    ax.legend()
    fig.savefig(str(name)+'.png')
