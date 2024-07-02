lst = [11, 34, 21, 33, 10]
largest = lst[0]
second_largest = lst[0]

for item in lst:
	if item >= largest:
		second_largest = largest
		largest = item
	elif item > second_largest and item != largest:
		second_largest = item
		
print(largest)
print(second_largest)