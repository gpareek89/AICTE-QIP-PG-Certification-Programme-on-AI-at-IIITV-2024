month = int(input("Enter the month:"))
if month in (1,3,5,7,8,10,12):
	print("31 days")
elif month in (4,6,9,11):
	print("30 days")
elif month == 2:
	year = int(input("Enter the year"))
	if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
		print("29 days")
	else:
		print("28 days")
else:
	print("Invalid year")