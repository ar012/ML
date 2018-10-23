Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = {}
>>> b = set()
>>> a
{}
>>> b
set()
>>> type(a)
<class 'dict'>
>>> type(b)
<class 'set'>
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
>>> print(basket)
{'apple', 'pear', 'orange'}
>>> orange in basket
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    orange in basket
NameError: name 'orange' is not defined
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False
>>> c = set('abracadabra')
>>> c
{'a', 'd', 'r', 'c', 'b'}
>>> type(c)
<class 'set'>
>>> d = set('alacazam')
>>> d
{'l', 'a', 'z', 'm', 'c'}
>>> c - d
{'b', 'r', 'd'}
>>> c | d
{'l', 'a', 'd', 'r', 'z', 'm', 'c', 'b'}
>>> c & d
{'c', 'a'}
>>> c ^ d
{'l', 'z', 'm', 'd', 'b', 'r'}
>>> (c | d) - (c & d)
{'l', 'd', 'r', 'z', 'm', 'b'}
>>> 
>>> 
>>> thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> x = thisdict['model']
>>> x
'Mustang'
>>> y = thisdict.get("year")
>>> y
1964
>>> for n in thisdict:
	print(n)

	
brand
model
year
>>> for n in thisdict.values():
	print(n)

	
Ford
Mustang
1964
>>> thisdict["year"] = 2018
>>> for n in thisdict.values():
	print(n)

	
Ford
Mustang
2018
>>> for n in thisdict:
	print(thisdict[n])

	
Ford
Mustang
2018
>>> thisdict[0]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    thisdict[0]
KeyError: 0
>>> for x, y in thisdict.items():
	print(x, y)

	
brand Ford
model Mustang
year 2018
>>> if "model" in thisdicti:
	print("Yes, 'model' is eixts")

	
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    if "model" in thisdicti:
NameError: name 'thisdicti' is not defined
>>> if "modle" in thisdict:
	print("Yes, 'model' is exist")

	
>>> 
>>> print(len(thisdict))
3
>>> thisdict["color"] = "green"
>>> thisdict
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'green'}
>>> thisdict.pop("model")
'Mustang'
>>> thisdict
{'brand': 'Ford', 'year': 2018, 'color': 'green'}
>>> thisdict.popitem()
('color', 'green')
>>> thisdict
{'brand': 'Ford', 'year': 2018}
>>> thisdict.popitem()
('year', 2018)
>>> thisdict
{'brand': 'Ford'}
>>> thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> thisdict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> del thisdict["model"]
>>> thisdict
{'brand': 'Ford', 'year': 1964}
>>> thisdict.pop("model")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    thisdict.pop("model")
KeyError: 'model'
>>> del thisdict
>>> thisdict
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    thisdict
NameError: name 'thisdict' is not defined
>>> thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> thisdict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> thisdict.clear()
>>> thisdict
{}
>>> thisdict = dict(brand="Ford", model="Mustang", year=1964)
>>> thisdict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> dict_data = thisdict.items()
>>> dict_data
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
>>> car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> car
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> car.get("model")
'Mustang'
>>> car.brand
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    car.brand
AttributeError: 'dict' object has no attribute 'brand'
>>> 
