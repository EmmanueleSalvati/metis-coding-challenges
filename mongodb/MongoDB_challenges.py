"""MongoDB challenges"""

import seaborn as sns
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt


def hist_var(variable_to_plot):
    """Make a plot of a specific variable.
    It assumes a global variable, which is the database collection hmm"""

    variable = []
    for row in hmm.find({}, fields={variable_to_plot: True, '_id': False}):
        print row[variable_to_plot]
        variable.append(row[variable_to_plot])

    plt.ion()
    plt.figure()
    plt.hist(variable, bins=50, facecolor='g', alpha=0.75)
    plt.title("Heavy metal movies over time")
    plt.xlabel("%s of production" % variable_to_plot)
    plt.ylabel("Movies per %s" % variable_to_plot)
    plt.show()


if __name__ == '__main__':
    sns.set()
    client = MongoClient()
    hmm = client.dsbc.hmm

    print """Running Challenge 1
    Make a histogram of the years in the data.
    How many metal movies came out over the years?"""
    hist_var('year')

    print """\nRunning Challenge 2
    Find the cast member that appeared in most Heavy Metal movies.
    Is there one that is shared by more than one of these movies?
    Or are they all completely different actors for every movie?"""
