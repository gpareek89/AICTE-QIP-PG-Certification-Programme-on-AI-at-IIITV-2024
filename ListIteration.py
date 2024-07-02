lst = [1, 2, 33, 41, 5]
i = 0
while i <= 4:
	if lst[i] % 2 == 0:
		lst[i] = lst[i] + 1
	else:
		lst[i] = lst[i] - 1
	print(lst[i])
	i = i + 1
	