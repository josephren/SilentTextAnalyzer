import operator

import numpy as np
from numpy.linalg import norm


def _to_ppmi(x):
    all_sum = np.sum(x)
    context_sum = np.diag(1.0 / np.sum(x, 0))
    word_sum = np.diag(1.0 / np.sum(x, 1))
    all_matrix = np.mat(word_sum) * np.mat(x) * np.mat(context_sum) * all_sum
    all_matrix = np.array(np.log2(all_matrix))
    all_matrix = np.array([[_positive_value(w) for w in row] for row in all_matrix])
    return all_matrix


def _positive_value(x):
    if x > 0:   return x
    return 0


def _cosine_similarty(x, y):
    x = np.ravel(x)
    y = np.ravel(y)
    return sum(x * y) / norm(x) / norm(y)


def similarity_list(x):
    m = len(x)
    score_dict = {}
    for i in range(m):
        for j in range(i + 1, m):
            score_dict[str(i) + " " + str(j)] = _cosine_similarty(x[i], x[j])
            score_dict[str(i) + " " + str(j)] = _cosine_similarty(x[i], x[j])

    sorted_score_list = sorted(score_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for entry in sorted_score_list:
        print entry[0], entry[1]


x = np.array([[0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1], [0, 2, 1, 0, 1, 0], [0, 1, 6, 0, 4, 0]])
x = _to_ppmi(x)
similarity_list(x)