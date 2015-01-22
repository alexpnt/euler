def calcNextPrime(p):
	while isPrime(p)==0:
		p+=1
		
	return p

def isPrime(n):							#check whether a number is prime or not
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            return False
            
    return True

#Miller-Rabin primality test
def checkMillerRabin(n,k):
	if n==2: return True
	if n==1 or n%2==0: return False

	#find s and d, with d odd
	s=0
	d=n-1
	while(d%2==0):
		d/=2
		s+=1
	assert (2**s*d==n-1)

	#witness loop
	composite=1
	for i in xrange(k):
		a=random.randint(2,n-1)
		x=modular_pow(a,d,n)
		if x==1 or x==n-1: continue
		for j in xrange(s-1):
			composite=1
			x=modular_pow(x,2,n)
			if x==1: return False #is composite
			if x==n-1: 
				composite=0
				break
		if composite==1:
			return False		#is composite
			
	return True					#is probably prime

#perform a Modular exponentiation
def modular_pow(base, exponent, modulus):
    result=1
    
    while exponent>0:
        if exponent%2==1:
           result=(result * base)%modulus
        exponent=exponent>>1
        base=(base * base)%modulus
        
    return result

def isEvenly(n,k):
	counter=0
	
	for i in range(1,k+1):
		if(n%i==0):
			counter+=1
			
	return counter==k

def primeFactorization(n,primes):	#find the factors of a number
	factors=[]
	i=0
	
	while(n!=1):
		if(n%primes[i]==0):
			factors.append(primes[i])
			n/=primes[i]
		else:
			i+=1
	return factors

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes
	primes=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in range(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in range(2,len(primes)-1) if primes[i]==True]
	
	return primes

def genOddComposites(n):		#generate a list of odd composite numbers, using the sieve of eratosthenes
	odds=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if odds[i]==True:
			for j in xrange(i**2,n+1,i):
				odds[j]=False

	odds=[i for i in xrange(2,len(odds)-1) if odds[i]==False and i%2==1]
	
	return odds

def collatz(n,dic):	#returns the lenght of a collatz sequence
	counter=1

	while(n!=1):
		if n in dic:			
			counter+=dic[n]
			break
		if n%2==0:
			n/=2
		else:
			n=3*n+1
		counter+=1
	
	return counter

def lattice(a,b):
	comb=fact(a+b)/(fact(a)*fact(b))	#Lattice Path
	return comb

def isAmicable(a,primes):
	b=d(a,primes)-a
	if(a==d(a,primes)-a):return 0
	if(a==(d(b,primes)-b)):		#a pair of amicable numbers
		return 1
	return 0

def d(n,primes):	#sum of proper divisors
	prod=1
	factors=primeFactorization(n,primes);
	while(len(factors)>0):					
		counter=factors.count(factors[0])
		prod*=sigma(factors[0],counter)			#multiplicativity property of the sigma function
		for i in range(0,counter):
			factors.remove(factors[0])
			
	return prod

def sigma(p,n):					#sigma(n,p) is the sum of divisors of the natural number, p. p is a also a prime.
	return (p**(n+1)-1)/(p-1)	

def findAbundant(n,primes):		#generate the abundant numbers
	ab=[]
	for i in range(1,n+1):
		if (d(i,primes)-i)>i:	#abundant number property
			ab.append(i)
			
	return ab

def countCycleLen(d,D):					#returns the length of the recurring cycle, for a given dividend and divisor
	remainders=[]
	r=q=1
	while r!=0 and r not in remainders:	#when we find a repeated remainder, we have a cycle (or not)
		q=d/D
		r=d%D
		remainders+=[r]					#save the remainders
		d=r*10
		r=d%D
		
	return len(remainders)

def isDigitPower(n):
	while (n > 0) {
    	int d = number % 10;
        number /= 10;

	original=n
	sum=0
	for d in str(n):
		sum+=int(d)**5;
	if(sum==n):
		return 1
		
	return 0

#merge the given integer values
def mergeIntegers(a,b,c):
	return int(str(a)+str(b)+str(c))

#merge the given integer values
def mergeIntegers(a,b):
	return int(str(a)+str(b))

#returns the length of a given number
def nLength(n):
	return math.floor(math.log(n,10))+1

def isCurious(num,den):
	expected=num/float(den)
	n=list(str(num))
	d=list(str(den))

	potential=False
	for i in xrange(0,2):
		for j in xrange(0,2):
			if(n[i]==d[j]):
				n.pop(i)
				d.pop(j)
				if((float(int(n[0]))/int(d[0]))==expected and expected<1.0):
					return 1
				else:
					return 0
	return 0

#perform a binary search
def binary_search(l, target):
    low=0
    high = len(l)
    while low < high:
        mid = (low+high)//2
        midval = l[mid]
        if midval < target:
            low = mid+1
        elif midval > target: 
            high = mid
        else:
            return mid
    return -1

#circular prime
def isCircular(n,primes):
	l=nLength(n)
	while(l!=0):	
		rotated=list(numpy.roll(list(str(n)),int(-l)))	#rotate
		num=int(''.join(rotated))						
		if(binary_search(primes,num)==-1):				#check if its a prime number
			return 0
		l-=1

	return 1

def isPalindrome(n): #check if a number is a palindrome
	n=str(n)
	if(n[len(n):-(len(n)+1):-1]==n):
		return 1

def isTruncablePrime(n,primes):
	for i in xrange(0,len(str(n))):	#remove digits from left to right
		test=int(str(n)[i:])
		if binary_search(primes,test)==-1:
			return 0

	while(n!=0):					#remove digits from right to left
		if binary_search(primes,n)==-1:
			return 0
		n/=10	
		
	return 1

def isPanDigit(n):
	original=n
	array=[0]*9													#boolean array used to check if a number is a pandigit
	while(n!=0):
		array[n%10-1]=1 										#mark that position
		n/=10
	if(sum(array)==9):											#check if number is a pandigit	
		for l in str(original):									#check if numbre doesnt have any 0
			if(l=='0'):
				return 0
		return 1
		
	return 0

def isTriangle(x):					#check whether a number is a triangular number or not
	test=(math.sqrt(8*x+1)+1)
	return test==int(test)

def genTriangleNumbers(n):
	tri=[]
	for i in xrange(0,n+1):
		tri+=[int(0.5*i*(i+1))]
	return tri

def isPentagonal(x):				#check whether a number is a pentagonal number or not
	test=(math.sqrt(24*x+1)+1)/6
	return test==int(test)

def genPentagonalNumbers(n):
	penta=[]
	for i in xrange(1,n+1):
		penta+=[int(i*(3*i-1)/2)]
	return penta

def triPascal(n):		#build a pascal triangle
	pascal=[[1],[1,1]]

	length=2
	for i in xrange(2,n+1):
		newRow=[1]
		for j in xrange(1,length):
			newRow+=[pascal[i-1][j-1]+pascal[i-1][j]]
		newRow+=[1]
		pascal+=[newRow]
		length+=1
		
	return pascal

def isLychrel(n):
	iterations=0
	while(iterations<50):
		n+=int(str(n)[::-1])
		if(str(n)==str(n)[::-1]):
			return False
		iterations+=1
		
	return True

def digitSum(n):
	s=0
	for d in list(str(n)):
		s+=int(d)
	return s

#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
#obtain a list of triplets (mn, dn, an). The sequence [a0; a1, a2, a3,...] is the continued fraction expansion
def continued_fraction_expansion(n):
	m_before=0
	d_before=1
	a0=a_before=int(floor(sqrt(n)))

	mda_triplets=[]
	period_lenght=0

	while True:

		m_next=d_before*a_before-m_before
		d_next=int((n-m_next**2)/d_before)
		a_next=int(floor((a0+m_next)/d_next))

		if(a_before==2*a0 or  ((m_next,d_next,a_next) in mda_triplets)):
			break
		else:
			mda_triplets+=[(m_next,d_next,a_next)]
			m_before=m_next
			d_before=d_next
			a_before=a_next
			period_lenght+=1

	return mda_triplets,period_lenght


# compute the continued fraction convergents to sqrt(D) (potential solutions for the Pell Equation)
# compute the convergents using the recurrent relations presented in http://mathworld.wolfram.com/PellEquation.html
def continued_fraction_covergents(D,n_periods):
	expansion,l=continued_fraction_expansion(D)

	for p in xrange(n_periods):			#add periods of triplets (m,d,a)
		expansion+=expansion[0:l]

	a0=int(floor(sqrt(D)))

	#initialize
	pn_2=1
	pn_1=a0

	qn_2=0
	qn_1=1

	convergents=[]
	for i in xrange(0,l*(n_periods+1)):			#recursive relations to find convergents	
		pn=expansion[i][2]*pn_1+pn_2
		pn_2=pn_1
		pn_1=pn

		qn=expansion[i][2]*qn_1+qn_2
		qn_2=qn_1
		qn_1=qn

		convergents+=[(pn,qn)]
		
	return convergents

#find the minimal solution in x , for the Pell Equation
def find_minimal_solution(convergents,D):
	found=False
	max_x=2**128
	y=0
	for c in convergents:
		if c[0]**2-D*c[1]**2==1 and c[0]<max_x:		#check if convergent is solution of the Pell Equation
			max_x=c[0]
			y=c[1]
			found=True

	return [found,max_x,y]

def generate_non_square_roots(N):
	return [non_square_root(i) for i in xrange(1,N+1) if non_square_root(i)<=N]

#n + floor(1/2 + sqrt(n))
def non_square_root(n):
	return n + int(floor(0.5+sqrt(n)))

def sum_digits(n):
    s=0
    while n:
        s+=n%10
        n/=10
    return s

def convert_to_number(num):
	s=''
	for t in num:
		s+=''.join(map(str,t))
	return int(s)

def phi(n,primes):
	#some useful properties
	if (checkMillerRabin(n,10)==True):		#fast prime check
		return n-1

	factors=primeFactorization(n,primes)	#prime factors
	distinctive_prime_factors=set(factors)	

	totient=n
	for f in distinctive_prime_factors:		#phi = sum (n * 1 - 1/p), p is a distinctive prime factor
		totient*=(1-1.0/f)

	return totietn

def main():
	#TODO: testing
	pass

if __name__ == '__main__':
	main()
