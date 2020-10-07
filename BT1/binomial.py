import math

def prob(n,p,N):
	result:float
	result =  math.comb(N,n)*((1-p)**(N-n))*(p**n)
	return result

#print(prob(n=2, p=0.5, N=10))

def infoMeasure(n,p,N):
	result:float
	result = -math.log2(prob(n, p, N))
	return result

#print(infoMeasure(2,0.5, 10));


def sumProb(N,p):
	result:float
	result = 0
	list_N = range(1,N+1)
	for i in list_N:
		result = result+ prob(i,p, N)
	return result

#print(sumProb(5,0.5));

'''
T thấy N càng lớn thì sumProb càng tiềm cận 1 => 
 '''

def approxEntropy(N,p):
	result:float
	total: float
	total = 0
	list_N = range(1,N+1)
	for i in list_N:
		total = total+ prob(i, p, N) + infoMeasure(i,p, N)
	result = total / N
	return result

#print(approxEntropy(N=10, p=0.5))



