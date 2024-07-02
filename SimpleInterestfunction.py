def simple_interest(p, r, t):
	si = p*r*t/100.0
	amount = p + si
	return ('simple interest = ', si, 'amount = ', amount)
	
principle = float(input("Enter the principle amount"))
rate = float(input("Enter the rate"))
time = float(input("Enter the time period"))

print(simple_interest(principle, rate, time))
print(simple_interest(r = rate, p = principle, t = time))