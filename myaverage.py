def avg(n1,n2,n3):
	a = (n1+n2+n3)/3.0
	return a

print(avg(2,3,4))

x = 4 + avg(12,31,43)
print(x)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

print(avg(num1,num2,num3))

if avg(2,1,4) < 10:
	print("True")