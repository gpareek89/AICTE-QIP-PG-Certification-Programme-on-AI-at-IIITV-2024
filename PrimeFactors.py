def isPrime(num):
	flag = True
	j = 0
	for j in range(2,num):
		if (num % j) == 0:	# whether j is a factor of num
			flag = False
			break
	return flag
	
n = 720
for i in range(2,n):
	if n % i == 0 and isPrime(i):
		print(i)