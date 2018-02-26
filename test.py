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

def not_empty(s):
	return s and s.strip()
	
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
		
def _not_divisible(n):
	return lambda x: x % n > 0
	
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
		
# for n in primes():
	# if n < 1000:
		# print(n)
	# else: 
		# break
	
L = list(filter(lambda n: n%2==1,range(1,20)))
print(L)

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

print(list(filter(is_palindrome,range(1,200))))

print(sorted([36,5,-12,9,-21],key=abs,reverse = True))

def by_name(t):
	return t[0].lower()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]	

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]
	
L2 = sorted(L,key = by_score, reverse=True)
print(L2)

# 函数式编程部分返回函数、装饰器没看懂。

# def createCounter():
	# n = 0
	# def counter(n):
		# return n+1
	
	
	# return counter

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())
# counterB = createCounter()
# print(counterB(), counterB(), counterB(), counterB())

# def log(func):
	# def wrapper(*args,**kw):
		# print('call %s():' % func.__name__)
		# return func(*args,**kw)
	# return wrapper

# @log
# def now():
	# print('2015-3-25')
	
# now()

#偏函数实质就是给一个部分参数固定的函数定义新名字的函数，好处是只需要涉及函数名，不用触及函数内部具体内容




	
