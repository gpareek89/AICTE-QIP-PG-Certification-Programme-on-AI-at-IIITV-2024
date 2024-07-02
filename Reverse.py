def ReverseNum(num):
	Reverse = 0
	while num > 0:
		Remainder = num % 10
		Reverse = (Reverse * 10) + Remainder
		num = num // 10
	return Reverse
 
n = int(input("Enter a number : "))
if ReverseNum(n) == n:
	print("Palindrome")
else:
	print("Not a Palindrome")
