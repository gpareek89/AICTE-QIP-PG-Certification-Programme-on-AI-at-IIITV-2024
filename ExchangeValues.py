def Exchange1(a,b):
	temp = a
	a = b
	b = temp
	return (a, b)
	
def Exchange2(a,b):
	a = a + b
	b = a - b
	a = a - b
	return ('x = ', a, 'y = ', b)
	
def Exchange3(a,b):
	a,b = b,a
	return ('x = ', a, 'y = ', b)


x = int(input("Enter the value for vriable x"))
y = int(input("Enter the value for vriable y"))

print("Output of Exchange1() function below : ")
(x, y) = Exchange1(x,y)
print('x = ', x)
print('y = ', y)

print("Output of Exchange2() function below : ")
print(Exchange2(x,y))
print('x = ', x)
print('y = ', y)


print("Output of Exchange3() function below : ")
print(Exchange3(x,y))
print('x = ', x)
print('y = ', y)

