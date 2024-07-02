lst = [11, 34, 21, 33, 10]
largest = lst[0]
index = 0
while index <= 4:
	if lst[index] > largest:
		largest = lst[index]
	index = index + 1
print(largest)