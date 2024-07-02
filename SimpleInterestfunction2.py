def simple_interest2(p, r, t=10):
	si = p*r*t/100.0
	amount = p + si
	print("rate of the main suite ", rate)
	return ('simple interest = ', si, 'amount = ', amount)
	
principle = float(input("Enter the principle amount"))
rate = float(input("Enter the rate"))
time = float(input("Enter the time period"))

print(simple_interest2(principle, rate))
print(simple_interest2(principle, rate, time))
