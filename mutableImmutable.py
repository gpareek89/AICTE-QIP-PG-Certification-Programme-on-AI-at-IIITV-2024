def fun1(count):
	print("Inside fun1()")
	while count <= 100:
		count = count + 1
	return count
	
def fun2(lst):
	print("Inside fun2()")
	i = 0
	while i < len(lst):
		lst[i] = lst[i] + 10
		i = i + 1
	return lst
	
value = int(input("Enter the value"))
print(fun1(value))
print("Inside the main suite")
print("Value is ", value)

list1 = [10, 20, 30, 40, 50]
print(fun2(list1))

print("Inside the main suite")
print("Final list values ", list1)
