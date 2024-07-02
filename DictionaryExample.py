daily_temps = {	("sun", "1st week"): 68.8, 
				"mon": 70.2, 
				'c': 67.2, 
				"wed": 71.8, 
				"thur": 73.2, 
				"fri": 75.6, 
				"sat": 74.0
				}
new_diction = dict(daily_temps)
print(daily_temps["mon"])
print(len(new_diction))
print(new_diction["mon"])
new_diction["zero"] = 0.0
print(new_diction)
print(daily_temps)
del new_diction['c']
print(new_diction)

print('c' in new_diction)
print("mon" in new_diction)

lst1 = (['banana', 20], ['apple', 10], ['Guava', 50])
new_diction_1 = dict(lst1)
print(new_diction_1)
print(new_diction_1["banana"])
print(new_diction_1["apple"])
print(new_diction_1["Guava"])





