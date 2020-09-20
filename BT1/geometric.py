def prob(n,p):
	result:float
	result = 1/pow(p, n)
	return result
#print(prob(n=1, p=2))

def infoMeasure(n,p):
	result:float
	result =n/pow(p, n)
	return result
#print(infoMeasure(n=10, p=2))


def sumProb(N,p):
	result:float
	result = 0
	list_N = range(1,N)
	for i in list_N:
		result = result+ prob(i,p)
	return result



#print(sumProb(N=99, p=2))

'''
Voi N = 5 => sumProb = 0.9375
Voi N = 10 => sumProb = 0.998046875
Voi N = 20 => sumProb = 0.9999980926513672
T thấy N càng lớn thì sumProb càng tiềm cận 1 => 
 '''

def approxEntropy(N,p):
	result:float
	total: float
	total = 0
	list_N = range(1,N)
	for i in list_N:
		total = total+ infoMeasure(i,p)
	result = total / N
	return result

print(approxEntropy(N=2000, p=2))







