import math

def prob(n,p,r):
	result:float
	result = math.comb(n+r-1,n)*((1-p)**n)*(p**r)
	return result

#print(prob(n=1, p=0.5, r=1))

def infoMeasure(n,p,r):
	result:float
	result = -math.log2( prob(n, p, r) )
	return result
#print(infoMeasure(n=5,p=0.5, p=2))


def sumProb(N,p,r):
	result:float
	result = 0
	list_N = range(1,N+1)
	for i in list_N:
		result = result + prob(i,p,r)
	return result

#print(sumProb(n=50,p=0.5, p=50))

'''

 '''

def approxEntropy(N,p,r):
	result:float
	total: float
	total = 0
	list_N = range(1,N+1)
	for i in list_N:
		total = total + prob(i, p, r) +infoMeasure(i,p,r)
	result = total / N
	return result

#print(approxEntropy(N=10, p=0.5,r=3))
