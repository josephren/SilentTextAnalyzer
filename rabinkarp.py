# coding=utf-8
__author__ = 'renwang'
'''
Input: pattern, document
Output: Index of the pattern. -1 if not get.
Las Vagas version, if Hash Match, then return
'''
def search(pattern,document):
    #get the hash of the pattern
    R = 256
    Q = 997
    pattern_hash = 0
    N = len(pattern)
    for i in range(N):
        pattern_hash = (pattern_hash * R + ord(pattern[i:i+1])) % Q

    M = len(document)
    if M < N:
        return -1

    doc_hash = 0
    for i in range(N):
        doc_hash = (doc_hash * R + ord(document[i:i+1])) % Q

    if doc_hash == pattern_hash:                    return 0

    #get the rm of the pattern. Details see algorithm
    rm = 1
    for i in range(N-1):
        rm = rm * R % Q
    for i in range(N,M):
        doc_hash = ((doc_hash + Q - ord(document[i-N:i-N+1]) * rm % Q) % Q  * R + ord(document[i:i+1])) % Q
        if doc_hash == pattern_hash:
            return i - N + 1

    return -1
