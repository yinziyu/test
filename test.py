def trim(s):
	while(s[:1] == ' '):
		s = s[1:]
		trim(s)
	while(s[-1:] == ' '):
		s = s[:-1]
		trim(s)	
	return s
	
s = trim(' Hello World   ')
print(s)		

def findMinAndMax(L):
	if(len(L)==0):
		return(None, None)
	else:
		min = L[0]
		max = L[0]
		for v in L:
			if v > max:
				max = v
			elif v < min:
				min = v
		return(min, max)
		
print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7,1,3,9,14]))

L1 = ['Hello','World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

g = (x*x for x in range(10))

for n in g:
	print(n)
	
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n+1

def triangles():
	L = [1]
	while True:
		yield L
		L = [x+y for x,y in zip([0]+L,L+[0])]
t = 0;	
for n in triangles():
	print(n)
	t = t+1
	if t == 10:
		break
		
def normalize(name):
	if len(name)<=1:
		return name.upper()
	else:
		name_nd = name[0].upper()+name[1:].lower()
		return name_nd
	
L1 = ['adam','LISA','barT','']
L2 = list(map(normalize,L1))
print(L2)

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
	return DIGITS[s]

def mult(x,y):
	return x*y
from functools import reduce	
def prod(L):
	#return reduce(mult,map(char2num,L))
	return reduce(mult,L)
	
print(prod([3,5,7,9]))

def fn(x,y):
	return x*10+y
	
def str2float(L):
	d1 = reduce(fn,map(char2num,L.replace('.','')))
	return d1/(10**(len(L)-L.find('.')-1))
	
print(str2float('12.3456'))	
	
