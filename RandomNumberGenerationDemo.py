import random

print(random.random())	# generates random number between the range 0 and 1

print(random.randrange(10))	# generates random integer between 0 and 10
print(random.randrange(2,10)) # generate random integer between 2 and 10

print(random.randint(2,10))

name = "Dr. Gaurav Pareek"
print(random.choices(name, k=2))

num = [10, 20, 30, 40, 50]
random.shuffle(num)
print(num)


