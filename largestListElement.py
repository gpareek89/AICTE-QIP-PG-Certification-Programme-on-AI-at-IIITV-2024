lst = [11, 34, 21, 33, 10]
largest = lst[0]
smallest = lst[0]
for item in lst:
	if item > largest:
		largest = item
	if item < smallest:
		smallest = item
	
print(largest)
print(smallest)