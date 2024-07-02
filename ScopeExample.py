def fun1():
	n = 10
	print("n in fun1() : ",n)
	
def fun2():
	n = 20
	print("n in fun2() before call to fun1() : ",n)
	fun1()
	print("n in fun2() after call to fun1() : ",n)

n = 30
fun2()
print("The global copy of n = ",n)