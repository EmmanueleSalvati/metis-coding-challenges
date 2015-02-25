"""MongoDB challenges"""

import seaborn as sns
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def hist_var(variable_to_plot):
    """Make a plot of a specific variable.
    It assumes a global variable, which is the database collection hmm"""

    # variable = []
    # for row in hmm.find({}, fields={variable_to_plot: True, '_id': False}):
    #     print row[variable_to_plot]
    #     variable.append(row[variable_to_plot])

    variable = a_field_list(variable_to_plot)

    plt.ion()
    plt.figure()
    plt.hist(variable, bins=50, facecolor='g', alpha=0.75)
    plt.title("Heavy metal movies over time")
    plt.xlabel("%s of production" % variable_to_plot)
    plt.ylabel("Movies per %s" % variable_to_plot)
    plt.show()


def a_field_list(field):
    """Given a field (such as 'title'), it makes a list of all the 'title's"""

    field_list = []
    for row in hmm.find({}, fields={field: True, '_id': False}):
        field_list.append(row[field])

    return field_list


def metal_cred_keywords(year):
    """Return a sorted list of popular keywords in the metal cred for a given
    decade, which starts at year"""

    pipeline = [{'$project': {'_id': 0, 'metal_cred': 1, 'year': 1}},
                {'$match': {'year': {'$gte': year}}},
                {'$match': {'year': {'$lt': year+10}}},
                {"$unwind": '$metal_cred'},
                {"$match": {"metal_cred": {"$ne": 'METAL CRED'}}}
                ]

    cred_words = {}
    cursor = hmm.aggregate(pipeline, cursor={})
    for doc in cursor:
        metal_words = doc['metal_cred'].split()
        for word in metal_words:
            if word in STRUCTURE_WORDS:
                continue
            if word not in cred_words.keys():
                cred_words[word] = 1
            else:
                cred_words[word] += 1

    return sorted(cred_words.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    sns.set()

    STRUCTURE_WORDS = ['the', 'an', 'and', 'of', 'by', u'\u201cThe',
                       u'\u2013', u'\u201980s', 'The', u'\u2022',
                       'in', u'\u201970s']

    client = MongoClient()
    hmm = client.dsbc.hmm

    print """Running Challenge 1
    Make a histogram of the years in the data.
    How many metal movies came out over the years?"""
    hist_var('year')

    print """\nRunning Challenge 3
    Find the most used words in Heavy Metal film titles.
    Is there a word that appears in a lot of them? Is it "The"?
    If it is something like "the", How can you get around that?
    Find one "meaningful" word that appears the most
    (this means non-structural word, unlike "the" or "a" or "in")"""
    titles = a_field_list('title')
    words_in_titles = {}
    for title in titles:
        words = title.split()
        for word in words:
            if word in STRUCTURE_WORDS:
                continue
            if word not in words_in_titles.keys():
                words_in_titles[word] = 1
            else:
                words_in_titles[word] += 1

    sorted_words = sorted(words_in_titles.items(), key=lambda x: x[1],
                          reverse=True)
    # for i in range(10):
    #     print sorted_words[i]

    print """\nRunning Challenge 4
    METAL CRED section lists themes included in these movies that makes them
    more metal. What were the top 5 metal cred keywords in the 70s? In 80s?
    In 90s, In 2000s?"""

    print '\nIn the \'70s'
    sorted_cred_words = metal_cred_keywords(1970)
    for i in range(5):
        print sorted_cred_words[i]

    print '\nIn the \'80s'
    sorted_cred_words = metal_cred_keywords(1980)
    for i in range(5):
        print sorted_cred_words[i]

    print '\nIn the \'90s'
    sorted_cred_words = metal_cred_keywords(1990)
    for i in range(5):
        print sorted_cred_words[i]

    print '\nIn the \'2000s'
    sorted_cred_words = metal_cred_keywords(2000)
    for i in range(5):
        print sorted_cred_words[i]








