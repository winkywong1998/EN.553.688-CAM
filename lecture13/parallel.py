import numpy as np
import math
import multiprocessing as mp
import time

#
# Function to return the number of changes from 0 to 1 or 1 to 0
# in a list of 0's and 1's
#
def number_of_changes(X):
    s=X[0] # value in current run
    nchanges=0
    for i in range(1,n):
        if X[i]==s: # no change
            continue
        else:
            s=X[i]
            nchanges+=1
    return(nchanges)


def simulate_once(args): # note - we can also pass empty tuple as an argument
    n=args[0]
    p=args[1]
    X=np.random.choice([0,1],size=n,p=[p,1-p])
    LR=number_of_changes(X)
    return(LR)

N=10000
n=1000
p=.75
nprocesses=4


if __name__=="__main__":
    time0 = time.time()
    #
    # create a pool of workers
    #
    pool = mp.Pool(nprocesses)
    #
    # create a list of arguments
    #
    arglist=[(n,p) for i in range(N)]
    # arglist=[() for i in range(N)]
    #
    # use pool.map to apply the simulate_once function to every
    # element in the argument list
    #
    result = pool.map(simulate_once,arglist)
    pool.close()
    pool.join()
    time1=time.time()
    print("time = "+ "{:10.3f}".format(time1-time0))
    print("mean = " + "{:10.3f}".format(np.mean(np.array(result))))
    print("std err = " + "{:10.3f}".format(np.std(np.array(result))/np.sqrt(N)))
