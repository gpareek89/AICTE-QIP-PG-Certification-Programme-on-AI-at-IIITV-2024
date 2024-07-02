def countingList(lst, item):
	count = 0
	for it in lst:
		if it == item:
			count = count + 1
	
	return count

def countIndex(lst, item):
	i = 0
	while i < len(lst):
		if item == lst[i]:
			print("The item was found at index ",i)
		i = i + 1
	
input_string = input("Enter the list elements separated by space : ")
lst = input_string.split()
item = input("Enter the item to be searched")
print("The item ",item,"occurs", countingList(lst, item), "times in the list")
countIndex(lst, item)