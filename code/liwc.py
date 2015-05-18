__author__ = 'intuinno'


import pandas as pd
import re
import fnmatch


liwc_def = {}

for line in open('../other_data/liwc_defs.txt'):
    lineSplit = line.split()
    liwc_def[lineSplit[0]] = lineSplit[1]


liwc_words = []

for line in open('../other_data/liwc_words.txt'):
    lineSplit = line.split()
    liwc_words.append( (lineSplit[0],  lineSplit[1:len(lineSplit)] ) )

liwc_wordsExact = {}
liwc_wordsWild = {}

for line in open('../other_data/liwc_words.txt'):
    lineSplit = line.split()

    if lineSplit[0].endswith('*'):
        liwc_wordsWild[  lineSplit[0].rstrip('*') ] =   lineSplit[1:len(lineSplit)]
    else:
        liwc_wordsExact[lineSplit[0]] = lineSplit[1:len(lineSplit)]


def getLIWC_Id(w):
    for (reExp, catList) in liwc_words:
        if fnmatch.fnmatch(w, reExp):
            # print w + ' : ' + str(catList)
            return catList

def getLIWC_Str(w):
    for (reExp, catList) in liwc_words:
        if fnmatch.fnmatch(w, reExp):
            # print w + ' : ' + str(catList)
            return [liwc_def[catId] for  catId in catList ]

def getLIWC_IdFast(w):
        if w in liwc_wordsExact:
            # print w + ' : ' + str(catList)
            return liwc_wordsExact[w]
        else:
            for key, value in liwc_wordsWild.iteritems():
                if w.startswith(key):
                    return value



print getLIWC_Str('abandons')
print getLIWC_Id('affect')

print getLIWC_IdFast('abandons')
print getLIWC_IdFast('affect')

import codecs
import re
from nltk import *

f = codecs.open('../project_materials/reddit/depressed.txt', 'rU', 'utf-8')

depressedAllText = word_tokenize(f.read())


liwcDist = FreqDist()

for (i,w) in enumerate(depressedAllText):
    wlower = w.lower()
    if i%1000 == 0:
        print i
    catList =  getLIWC_IdFast(wlower)
    if catList:
        for cat in catList:
            liwcDist[cat] += 1
