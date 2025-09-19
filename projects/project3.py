import numpy as np
import math as m

#estimate pi by randomly plotting values
#assuming x:[0,1] and y:[0,1] if sqrt(x^2+y^2) <= 1, it is on/in the circle with radius 1
#the area of the square is 1, while the area of the segment is pi*r^2, pi in our case
#given x:[0,1] and y:[0,1] and a circle with radius 1 at the origin, this is a quarter circle with area 
#pi/4. So, we expect that (pi/4)/1 = pi/4 = p of our random value will be in the circle
#thus, the ratio of plots in quarter circle should be 4p = pi

#construct 99% confidence interval using binomial -> normal
#estimator of p' = (1/n)*sum(X), sample mean
#Var[p'] = (1/n^2)*Var(X) = p'(1-p')/n, thus standard deviation estimator is sqrt(p(1-p')/n)
#however, we care about 4*p, so Var[4p'] = 16p'(1-p')/n and std dev is 4*sqrt(p'(1-p')/n), and E[4p'] is simply 4*sample mean
#using 99% middle CI, Z score of 99.5 is 2.576, so the bounds for CI would be 4p' +- 2.576*4*sqrt(p'(1-p')/n)

def simulate(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    #numpy uses vector operations to speed this up
    distance = np.sqrt(x**2+y**2)
    #comparison operation on a np.array creates an equal sized array of booleans denoting whether condiitonal is true at each part
    #we can sum this since it is 0s and 1s to get the number of matches
    p = (np.sum(distance <= 1))/n
    print(f"[{(4*p) - (2.576)*4*m.sqrt(p*(1-p)/n):.5f}, {(4*p) + (2.576)*4*m.sqrt(p*(1-p)/n):.5f}]")
    return ((np.sum(distance <= 1))/n)*4

print(simulate(100))
print(simulate(1000))
print(simulate(10000))
print(simulate(100000))
print(simulate(1000000))
print(simulate(10000000))

#bounds consistently get tighter and mean gets closer. Generally around 100,000 starts to round to 3.14 more often