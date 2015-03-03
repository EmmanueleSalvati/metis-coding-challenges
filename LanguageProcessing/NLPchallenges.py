"""Week 7 NLP (nltk) challenges"""

from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def max_10_tfidf_movies(a_review_array, features_list):
    """Returns a sorted list of the 10 words with highest tfidf words in this
    movie review

    It takes a numpy array with a row of a sparse matrix
    i.e. created with matrix[i].toarray()"""

    movie_s = pd.Series(a_review_array).order(ascending=False)
    first_ten = movie_s[:10]

    for word_index in first_ten.index:
        print features_list[word_index]


if __name__ == '__main__':

    # The movies are stored in a specific nltk format:
    # type(movie_reviews)
    # nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader

    fileids = movie_reviews.fileids()[:100]

    doc_words = [movie_reviews.words(fileid) for fileid in fileids]
    documents = [' '.join(words) for words in doc_words]

    vectorizer = TfidfVectorizer(stop_words='english')
    doc_vectors = vectorizer.fit_transform(documents)

    # This is challenge 1: Calculate the tf-idf for each word in the first 100
    # reviews in the nltk movie reviews corpus.
    # For each document, print the top 10 tf-idf words.
    features = vectorizer.get_feature_names()
    counter = 1
    for i in range(doc_vectors.shape[0]):
        review = doc_vectors[i].toarray()[0]
        print 'review number:', counter
        max_10_tfidf_movies(review, features)
        counter += 1
        print
