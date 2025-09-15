import math as m
import numpy as np
import matplotlib.pyplot as plt

#requires numpy and matplotlib installation
#pip install numpy matplotlib

#for sufficiently large n, normal approximates binomial

#given n trials and p probability of sucess, simulate k in [0,n] for both binomial and normal

#assume valid n: n>0 valid p, p in [0,1] for all

#a) calculate binom of k = 0, 1, ..., n
def binom(n, p):
    k = np.arange(0, n, 1)
    #n choose k is n!/k!(n-k)!
    results = m.factorial(n)*p**(k)*(1-p)**(n-k)
    for i in range(0, n):
        results[i] = results[i]/(m.factorial(i)*m.factorial(n-i))
    return results

#a) calculate normal of k = 0, 1, ..., n
def normal(n, p):
    k = np.arange(0, n, 1)
    results = (1/np.sqrt(2*np.pi))*(1/np.sqrt(n*p*(1-p)))*np.exp(-((k - n*p)**2)/(2*n*p*(1-p)))
    #when we iterate through k, n and p are held constant
    return results

#plots both with matplotlib
def plot(n, p):
    bi = binom(n, p)
    no = normal(n, p)
    #xaxis = np.arange(0, n, 1)
    plt.figure()
    plt.plot(bi, label='Binom')
    plt.plot(no, label='Normal')
    plt.title(f"n={n}, p={p}")
    plt.show()

#for close to 0.5..

'''
plot(5, 0.49)
plot(10, 0.49)
plot(15, 0.49)
plot(20, 0.49)
plot(25, 0.49)
'''

#n=20 is already pretty similar

#for close to 0, 0.02

'''
plot(5, 0.02)
plot(10, 0.02)
plot(20, 0.02)
plot(50, 0.02)
plot(100, 0.02)
plot(150, 0.02)
'''

#struggles for low k to match, even n = 100 has a little difference, though by at 150 basically the same

#for close to 1, 0.98

'''
plot(5, 0.98)
plot(10, 0.98)
plot(20, 0.98)
plot(50, 0.98)
'''

#looks decently similar at 50

#p closer to 0.5 generally converges at lower n compared to p closer to 0 or to 1