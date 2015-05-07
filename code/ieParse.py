__author__ = 'intuinno'

import multiprocessing as mp
import codecs
import re
import pandas as pd

def parseSeg(num):
    print num
    NDsubject = []
    NDrelation = []
    NDargument = []
    fSource = codecs.open('../project_materials/reddit/ie-segNDepression' + str(num) + '.txt',mode='r',encoding='utf-8')
    for line in fSource:
#     print line
        match = re.search('(?:Context\(.*\):)?\((.*?);\s(.*?);\s(.*?)(?:;.*)*\)', line)
        if match:
    #         print match.group(3)   ## 'alice-b@google.com' (the whole match)
            NDsubject.append(match.group(1).lower())  ## 'alice-b' (the username, group 1)
            NDrelation.append(match.group(2).lower())  ## 'google.com' (the host, group 2)
            NDargument.append(match.group(3).lower())  ## 'google.com' (the host, group 2)
    NDtuple = pd.DataFrame({'subject':NDsubject, 'relation':NDrelation, 'argument':NDargument   })
    NDtuple.to_csv('../project_materials/reddit/segIETuples' + str(num) + '.csv',encoding='utf-8')


pool = mp.Pool(processes=4)

pool.map(parseSeg, range(100))

# parseSeg(1)