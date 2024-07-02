# Program to write a function that returns the maximum and minimum values in the list of numbers

def maxmin(lst):
	a = max(lst)
	b = min(lst)
	return (a,b)

#beginning of the main suite
	
list1 = [10, 20, 30, 40]
list2 = ['hello', 'dear', 'John']
print(maxmin(list1))
maxmin(list1)
print(maxmin(list2))