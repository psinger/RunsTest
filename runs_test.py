from __future__ import division

__author__ = 'psinger'

from collections import Counter, defaultdict
import sys
import math
from scipy.stats import chi2

def weighted_variance(counts):
    #counts = Counter(x).items()

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
        ns = len([x for x in path if x is elem])
        rs = sum(cats[elem].values())
        ss = weighted_variance(cats[elem])
        cs = (pow(rs,2)-1)*(rs+2)*(rs+3) / (2*rs*(ns-rs-1)*(ns+1))
        vs = cs * ns * (ns-rs) / (rs*(rs+1))

        x2 += ss * cs
        df += vs

    print x2, df
    print chi2.sf(x2,df)

#x = [1,1,1,1,2,2,2]
#x = [1,1,1,3,2,1,2,1]
#x = [2,1,1,2,1,1,2]
x = [2,2,1,3,3,1,3,3,3,1,2,1,1,1,2,1,1,2,2,1,2,1,1,2,1,2,2]
#x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

runs_test(x)

#weighted_variance(dict({1:4, 2:3}))

#weighted_variance(x)