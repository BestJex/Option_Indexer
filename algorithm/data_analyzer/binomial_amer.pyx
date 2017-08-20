from libc.math cimport exp,sqrt,pow
from collections import defaultdict as ddt

cdef float _binomial_amer(float s0,float k,float T, int n,float r,float sigma):
    cdef float delta = T / n
    cdef float u = exp(sigma * sqrt(delta))
    cdef float d = exp(-sigma*sqrt(delta))
    cdef float p = (exp(r*delta)-d)/(u-d)
    cdef float q = 1.-p
    nm = ddt(ddt)
    for j in range(1,n):

        for i in range(1,j+1):
            temp = s0 * pow(u, j+1-i) * pow(d, i-1)
            nm[j][i] = max(temp - k, 0)
    f=ddt(ddt)
    for w in range(1,n):
        f[n - 1][w] = max(nm[n-1][w], exp(-r*delta) * (p*nm[n][w] + q*nm[n,w+1]))
    for g in range(n-2,1,-1):
        for h in range(1,g+1):
            f[g][h] = max(nm[g][h], exp(-r * delta) * (p*f[g+1][h] + q*f[g+1][h+1]))
    return max(exp(-r * delta) * (p*f[1][1] + q * f[1][2]), s0-k)

def binomial_amer(s,k,t,n,r,sg):
    return _binomial_amer(s,k,t,n,r,sg)