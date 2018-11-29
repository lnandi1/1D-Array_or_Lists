Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = ['apples','bananas','pears']
>>> print(fruit)
['apples', 'bananas', 'pears']
>>> 
>>> fruit.append('grape')
>>> print(fruit)
['apples', 'bananas', 'pears', 'grape']

>>> print(fruit[2])
pears
>>> print(fruit[0])
apples
>>> print(fruit[-1])
grape
>>> print(fruit[0].title())
Apples
>>> message = "My favourite fruit is "+
SyntaxError: invalid syntax
>>>  message = "My favourite fruit is " +fruit[0]
SyntaxError: unexpected indent
>>> message = "L " +fruit[0]
>>> print(message)
L apples
>>> fruit.insert(0,"mango")
>>> print(fruit)
['mango', 'apples', 'bananas', 'pears', 'grape']
>>> 
>>> del fruit[0]
>>> print(fruit)
['apples', 'bananas', 'pears', 'grape']
>>> 
>>> one = fruit.pop()
>>> print(fruit)
['apples', 'bananas', 'pears']
>>> 
>>> 
>>> 
>>> fruit.remove('apples')
>>> print(fruit)
['bananas', 'pears']
>>> 
>>> 
>>> 
>>> fruit.sort()
>>> print(fruit)
['bananas', 'pears']
>>> len(fruit)
2
>>> fruit.reverse()
>>> print(fruit[4])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(fruit[4])
IndexError: list index out of range
>>> 
>>> 
>>> 
>>> 
>>> food = ['bread','egg','banana']
>>> for foo in food:
	print(foo)

	
bread
egg
banana
>>> for value in range(1,6):
	print(value)

	
1
2
3
4
5
>>> squares = []
>>> for value in range(1,5):
	square = value *2
	squares.append(square)

	
>>> print(squares)
[2, 4, 6, 8]
>>> 
>>> 
>>> digits = [1,2,3,4]
>>> min(digits)
1
>>> max(digits)
4
>>> sum(digits)
10
>>> 
>>> 
>>> players = ['martin','anna','jon']
>>> print(players[0:1])
['martin']
>>> 
>>> print(players[:2])
['martin', 'anna']
>>> print(players[:-1])
['martin', 'anna']
>>> print(players[:-2])
['martin']
>>> 
