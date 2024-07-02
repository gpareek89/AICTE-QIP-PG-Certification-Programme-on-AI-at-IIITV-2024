lst = [0,'',0,0.0,0]

for k in range(len(lst)):
	if k == 1:
		lst[k] = input("Enter the list element: ")
	else:
		lst[k] = int(input("Enter the list element: "))

print(lst)