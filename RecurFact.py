def recurFact(num):
	if num == 1:
		return num

	else:
		return num * recurFact(num - 1)

f = recurFact(5)
print (f)

