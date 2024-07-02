lst=[23, 34, 56, 10, 11]
largest=lst[0]
s=lst[0]
for i in lst:
	if i>largest:
		largest=i

	else:
		largest=largest

for s in lst:
	s=lst[len(lst)-1]

print(largest)
print(s)