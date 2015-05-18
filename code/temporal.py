__author__ = 'intuinno'


import pandas as pd
import json
import re
import codecs
from nltk import *

f = codecs.open('../other_data/hedonometer/hedonometer.json',mode='r',encoding='cp1252')

contents = f.read()

a = json.loads(contents)

wordlist = a['objects']

hedonDict = {}
for w in wordlist:
    hedonDict[w['word']] = w['happs']

print hedonDict['laughter']

trimmed_user_status = pd.read_csv('../project_materials/mypersonality_depression/trimmed_user_statuses.csv',encoding='cp1252')

def calculateHappyness(s):
    words = word_tokenize(s)
    score = 0
    for w in words:
        if w.lower() in hedonDict:
            score += hedonDict[w.lower()]
    return score / len(words)


def calculateHappynessRow(row):
    s = row['status_update']



    # print row['userid']

    words = word_tokenize(s)
    score = 0
    for w in words:
        if w.lower() in hedonDict:
            score += hedonDict[w.lower()]
    return score / len(words)


# print calculateHappyness('Happier terror')


print calculateHappyness(':) :) :)')


# print calculateHappyness(trimmed_user_status['status_update'][''])

test = trimmed_user_status[ trimmed_user_status['userid'] == 'e23570d2dc6e6ac6adf320c91e0826df'].dropna()

allData = trimmed_user_status.fillna('0')
# test.apply(calculateHappynessRow, axis=1)
allData['happy'] = allData.apply(calculateHappynessRow, axis=1)