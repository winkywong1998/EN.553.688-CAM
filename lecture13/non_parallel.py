#
# Non parallel version of Monte-Carlo program.
# Question - Flip a coin P(heads)=p P(tails)=1-p n times. 
# What is the expected number of times we see a change from 0 to 1 or 1 to 0
# We do N Monte-Carlo trials.
#
import numpy as np
import math
import time

#
# Function to return the number of changes from 0 to 1 or 1 to 0
# in a list of 0's and 1's
#
def number_of_changes(X):
    s=X[0] 
    nchanges=0
    for i in range(1,n):
        if X[i]==s: # no change
            continue
        else:
            s=X[i]
            nchanges+=1
    return(nchanges)

#
# Function to do a single realization of n Bernoulli(p) trials 
# and call the number of changes program. The function takes a tuple 
# of arguments (n,p).
#
# We can pass an empty tuple if we wish (n and p could be global)
#
def simulate_once(args):
    n=args[0]
    p=args[1]
    X=np.random.choice([0,1],size=n,p=[p,1-p])
    LR=number_of_changes(X)
    return(LR)
#
# Set the values of the parameters
#
N=10000
n=1000
p=.75
#
# Create a list of 2-tuples and apply simulate_once() to every 2-tuple using
# map.
#
time0 = time.process_time()
arglist=[(n,p) for i in range(N)]
result = list(map(simulate_once,arglist))
time1=time.process_time()
print("time = "+ "{:10.3f}".format(time1-time0))
print("mean = " + "{:10.3f}".format(np.mean(np.array(result))))
print("std err = " + "{:10.3f}".format(np.std(np.array(result))/np.sqrt(N)))