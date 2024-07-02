def factorial(num):
	fact = 1
	i = 1
	
	if(num < 0):
		return 0
	
	while i <= num:
		fact = fact * i
		i = i + 1
	return fact
	
n = int(input("Enter the number : "))
value = factorial(n)


if(value == 0):
	print("Enter a positive number")
else:
	print("Factorial of ",n,"is ", value)
	