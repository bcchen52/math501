import numpy as np
import math as m
import random

# pn = sum_{i=1}^{n}((-1)^(i+1)/(i!)) -> 1/e as n-> infty

def get_prob(n):
    divisor = np.arange(1, n+1, 1)

    #O(n) factorial
    for i in range(1, len(divisor)):
        divisor[i] *= divisor[i-1]
        #can't set negatives in this loop since it would propogate 

    dividend = (-1) ** (np.arange(2, n+2))
    #i+1, init i=0, so 2
 
    result = sum(dividend/divisor)
        
    return result

def simulate(n, trials):
    envelopes = np.arange(1, n+1)
    success = 0

    for i in range(trials):
        letters = np.random.permutation(envelopes)
        #easy check to see if any original matches scrambled
        if np.any(letters == envelopes):
            success += 1
        
    return success/trials

def print_result(n, trials):
    result = simulate(n, trials)

    expected = get_prob(n)

    error = (np.abs(result-expected)/expected) * 100

    print(f"n={n}: {result} empirical; {error:.2f}% error from expected of {expected:.5f}")

print_result(5, 10000)
print_result(6, 10000)
print_result(7, 10000)
print_result(8, 10000)
print_result(9, 10000)
print_result(10, 10000)
print_result(20, 10000)

'''

The results generally fluctuate without clear pattern, sometimes n=10 has a higher % error that lower n, and other times opposite

Take for example...

n=5: 0.6272 empirical; 0.97% error from expected of 0.63333
n=6: 0.6281 empirical; 0.61% error from expected of 0.63194
n=7: 0.6307 empirical; 0.23% error from expected of 0.63214
n=8: 0.6208 empirical; 1.79% error from expected of 0.63212
n=9: 0.6398 empirical; 1.21% error from expected of 0.63212
n=10: 0.6242 empirical; 1.25% error from expected of 0.63212
n=20: 0.6308 empirical; 0.21% error from expected of 0.63212

compared to

n=5: 0.6208 empirical; 1.98% error from expected of 0.63333
n=6: 0.6259 empirical; 0.96% error from expected of 0.63194
n=7: 0.6353 empirical; 0.50% error from expected of 0.63214
n=8: 0.6306 empirical; 0.24% error from expected of 0.63212
n=9: 0.6347 empirical; 0.41% error from expected of 0.63212
n=10: 0.6293 empirical; 0.45% error from expected of 0.63212
n=20: 0.6296 empirical; 0.40% error from expected of 0.63212

However, they all tend to be around or less than the 1% range. This makes sense considering I am running 10,000 trials.
'''
