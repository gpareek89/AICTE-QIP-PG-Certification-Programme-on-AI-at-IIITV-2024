num = 100

def fun1():
	print("Number is global and is accessible inside fun1() ", num)
	
def fun2():
	print("Number is global and is accessible inside fun2() ", num)

fun1()
fun2()