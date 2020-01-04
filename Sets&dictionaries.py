#sets {}

#includes a data type for sets.
#Curly braces or the set() function can be used to create sets.

#only one show duplicate 
basket = {'apple', 'orange', 'appple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket
'crabgrass' in basket		# fast membership testing


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 		#unique letters in a
a - b 	#letters in a but not in b
a | b 	#letters in a or b or both
a & b 	#letters in both a and b
a ^ b 	#letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits.update("grape", "water melon")
frutis.remove("banana")
fruits.discard("kiwi")
fruits


>>>Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
'guido' in tel
'sape' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

#When looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.item():
	print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

questions = ['name', 'quest','favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answer):
	print('What is your {0}? It is {1}.'.format(q, a))

