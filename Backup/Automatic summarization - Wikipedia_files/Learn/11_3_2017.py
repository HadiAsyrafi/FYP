Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'/home/hadi'
>>> import json
>>> f = open('car.json')
>>> car = json.load(f)
>>> car
{u'mycar': {u'transmission': u'auto', u'features': {u'power steering': True}, u'doors': 4}}
>>> type (car)
<type 'dict'>
>>> car.keys()
[u'mycar']
>>> f.close()
>>> car['mycar']['color'] = 'red'
>>> car
{u'mycar': {u'transmission': u'auto', 'color': 'red', u'features': {u'power steering': True}, u'doors': 4}}
>>> f = open('car.json', 'w')
>>> json.dump(car, f)
>>> f.close()
>>> f = open('car.json', 'w')
>>> json.dump(car, f, indent=2)
>>> f.close()
>>> f = open('car.json', 'w')
>>> json.dump(car, f, indent=1)
>>> f.close()
>>> f = open('car.json', 'w')
>>> json.dump(car, f, indent=5)
>>>  f.close()
 
  File "<pyshell#23>", line 1
    f.close()
    ^
IndentationError: unexpected indent
>>> 
KeyboardInterrupt
>>> f.close()
>>> f = open('car.json', 'w')
>>> json.dump(car, f, indent=2)
>>> f.close()
>>> print json.dumps(car, indent =2)
{
  "mycar": {
    "transmission": "auto", 
    "color": "red", 
    "features": {
      "power steering": true
    }, 
    "doors": 4
  }
}
>>> from car import Car
>>> mycar = Car(make = 'Ford', model = 'Olol', features = { 'power steering' = True})
SyntaxError: invalid syntax
>>> mycar = Car(make = 'Ford', model = 'Olol', features = { 'power steering' : True})
>>> vars(mycar)
{'make': 'Ford', 'model': 'Olol', 'features': {'power steering': True}}
>>> f = open('newcar.json', 'w')
>>> json.dump(vars(mycar), f, indent = 2)
>>> f.close()
>>> 
