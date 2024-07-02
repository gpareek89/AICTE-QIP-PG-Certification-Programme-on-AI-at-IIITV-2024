def summation(low, high, div):
	sum = 0
	for item in range(low+1, high):
		if item % div == 0:
			sum = sum + item
	return sum

low = int(input("Enter the lower limit of the range"))
high = int(input("Enter the higher limit of the range"))
div = int(input("Enter the divisor"))
print(summation(low,high,div))
