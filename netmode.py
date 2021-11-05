import matplotlib.pyplot as plt

def plot_ergasthrio(ax):
    ax.hlines(y=0, xmin=0, xmax=6, linewidth=2, color='r')
    ax.hlines(y=3.5, xmin=0, xmax=6, linewidth=2, color='r')
    ax.hlines(y=9.5, xmin=0, xmax=6, linewidth=2, color='r')
    ax.hlines(y=11.5, xmin=2, xmax=4, linewidth=2, color='r')

    ax.vlines(x=0, ymin=0, ymax=9.5, linewidth=2, color='r')
    ax.vlines(x=6, ymin=0, ymax=9.5, linewidth=2, color='r')
    ax.vlines(x=2, ymin=9.5, ymax=11.5, linewidth=2, color='r')
    ax.vlines(x=4, ymin=9.5, ymax=11.5, linewidth=2, color='r')
