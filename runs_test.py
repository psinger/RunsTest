from __future__ import division

__author__ = 'psinger'

from collections import Counter, defaultdict
import sys
import math
from scipy.stats import chi2

def weighted_variance(counts):
    #counts = Counter(x).items()

    #print counts

    avg = 0

    for length, count in counts.iteritems():
        avg += count * length

    counts_only = counts.values()
    #print counts_only
    avg /= sum(counts_only)

    var = 0

    for length, count in counts.iteritems():
        var += count * math.pow((length - avg),2)

    try:
        var /= sum(counts_only) - 1
    except:
        #var = 0
        raise Exception("Division by zero due to too few counts!")

    #print var
    return var

def runs_test(path):

    counter = 1
    same = True
    cats = defaultdict(lambda : defaultdict(int))

    for i, elem in enumerate(path):
        #print elem, i
        if i == len(path) - 1:
            cats[elem][counter] += 1
            break

        if path[i+1] == elem:
            same = True
            counter += 1
        else:
            cats[elem][counter] += 1
            counter = 1

    #print cats

    x2 = 0
    df = 0

    for elem in cats.keys():
        #print elem
        #print cats[elem].keys()
        #print cats[elem]
        #print [x for x in path if x == elem]
        ns = len([x for x in path if x == elem])
        #print ns
        rs = sum(cats[elem].values())

        if len(cats[elem].keys()) == 1 or rs == 1 or (ns-rs) == 1:
            print elem
            print cats[elem]
            continue

        #print rs
        ss = weighted_variance(cats[elem])
        #print ss
        cs = (pow(rs,2)-1)*(rs+2)*(rs+3) / (2*rs*(ns-rs-1)*(ns+1))
        #print cs
        vs = cs * ns * (ns-rs) / (rs*(rs+1))

        x2 += ss * cs
        #print x2
        #sys.exit()
        df += vs

    print x2, df
    print chi2.cdf(x2,df)
    print "%.10f" % chi2.sf(x2,df)

#x = [1,1,1,1,2,2,2]
#x = [1,1,1,3,2,1,2,1]
#x = [2,1,1,2,1,1,2]
#x = [2,2,1,3,3,1,3,3,3,1,2,1,1,1,2,1,1,2,2,1,2,1,1,2,1,2,2]
#x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,2]

x = ["B","B","A","C","C","A","C","C","C","A","B","A","A","A","B","A","A","B","B","A","B","A","A","B","A","B","B"]

runs_test(x)

#weighted_variance(dict({1:4, 2:3}))

#weighted_variance(x)