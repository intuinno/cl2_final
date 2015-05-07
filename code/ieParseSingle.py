__author__ = 'intuinno'


import codecs
import re

f = codecs.open('../other_data/ie-NDepression.txt', 'rU', 'utf-8')

NDsubject = []
NDrelation = []
NDargument = []

for line in f:
    # print line
    match = re.search('(?:Context\(.*\):)?\((.*?);\s(.*?);\s(.*?)(?:;.*)*\)', line)
    if match:
        print match.group(3)   ## 'alice-b@google.com' (the whole match)
        NDsubject.append(match.group(1).lower())  ## 'alice-b' (the username, group 1)
        NDrelation.append(match.group(2).lower())  ## 'google.com' (the host, group 2)
        NDargument.append(match.group(3).lower())  ## 'google.com' (the host, group 2)
        if match.group(3) == '0.95 (TaskerData sr="" dvi="1" tv=; m; 4.6u3)':
            print line
