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

def runs_test(input, path = True):
    '''
    You can pass a path or a dictionary of runs lengths
    path_passed = True states that you pass a path
    '''

    if path == True:
        counter = 1
        same = True
        cats = defaultdict(lambda : defaultdict(int))

        for i, elem in enumerate(input):
            #print elem, i
            if i == len(input) - 1:
                cats[elem][counter] += 1
                break

            if input[i+1] == elem:
                same = True
                counter += 1
            else:
                cats[elem][counter] += 1
                counter = 1
    else:
        cats = input

    #print cats

    x2 = 0
    df = 0
    nr_elem = len(cats.keys())
    fail_cnt = 0

    for elem in cats.keys():
        #print elem
        #print cats[elem].keys()
        #print cats[elem]
        #print [x for x in path if x == elem]
        #ns = len([x for x in path if x == elem])
        ns = sum([x*y for x,y in cats[elem].iteritems()])
        #print ns
        rs = sum(cats[elem].values())

        #print ns, rs

        if len(cats[elem].keys()) == 1 or rs == 1 or (ns-rs) == 1:
        #if rs == 1 or (ns-rs) == 1:x
            #print "Category '%s' has only one run length or only one run or ns-rs equals one! Sorry I will ignore it!" % elem
            fail_cnt += 1
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

    #note that this is kind-of a hack, you can adapt this as wanted
    if nr_elem - fail_cnt < 2:
        raise Exception("I ignored too many categories of this sequences! Sorry can't do the test!")

    if x2 == 0 or df == 0:
        raise Exception("x2 or df are zero, this really shouldn't happen!")
    #print x2, df
    #print chi2.cdf(x2,df)
    pval = chi2.sf(x2,df)
    print "p-val %.10f" % pval
    return pval

#x = ["S", "S", "F", "S", "F", "F", "F", "F", "S", "S", "S", "F", "F"]

#x = ["S", "S", "S", "F", "S", "F", "S", "S", "S", "F", "F", "S", "S", "S"]

#x = ["B","B","A","C","C","A","C","C","C","A","B","A","A","A","B","A","A","B","B","A","B","A","A","B","A","B","B"]
#x = ["S","S","S","S","S","F", "F", "F", "F", "F","S","S","S","S","S","F", "F", "F", "F", "F", "S", "F"]


#recalculation of results in O'Brien
#runs_test({'M':{1:29, 2:10, 3:8, 4:3, 5:1, 6:1, 7:1, 8:1, 12:2}, 'D':{1:33, 2:17, 3:6, 5:1}}, path=False)

#this will produce an exception
#runs_test(["S", "S", "S", "F", "S", "F", "S", "S", "S", "F", "F", "S", "S", "S"])

#runs_test(["B","B","A","C","C","A","C","C","C","A","B","A","A","A","B","A","A","B","B","A","B","A","A","B","A","B","B"])

#runs_test(["S", "S", "S", "F", "S", "F", "F", "F", "F"])
