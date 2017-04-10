# intro-interactive-programming-python-pt2
Compilation of exercises and notes from Rice Universities - Introduction to Interactive Programming in Python (Part 2).
The exercises and mini-projects are to be used in conjunction with codeskulptor.org

## Notes

### Lists and Their Methods

* lists are the backbone of python programming - similar to a JavaScript array
* tuple is a list that is immutable - they cannot be changed
```python
lst1 = ["Monday", 6, 2017, "Hungry"];
tup1 = ("I'm sleepy.");
```
* "in" allows you to check for data in lists by evaluating to True or False
```python
6 in lst1 => True

if 2017 in lst1:
  print  "Yeah it's there."
```
* index will tell you where an item is in the lists
```python
lst1.index(2017); => 2
```
* append and pop allow you to add or remove an items in the list
```python
lst1.append("Mical"); => ["Monday", 6, 2017, "Hungry", "Mical"];
lst1.pop(); => "Mical"
```

### Iteration

* allows you to repeatedly complete tasks through use of logic such as for loops
* when iterating over a list you cannot make changes to that list
```python
for item in lst1:
  print item;

numbers = [1, 2, 3, 4, 5];

for num in numbers:
  print num;
```

### Dictionaries

* lets you map keys to values - similar to JavaScript objects
```python
dict1 = {1:2, 2:5, 3:9}

dict1[2] => 5

dict2 = {"a":1, "b":2, "c":3}

dict2["b"] => 2
```

### Object-Oriented Programming & Classes

* object-oriented programming encapsulates behavior, making it simple to change only what needs to be altered
* each data types have built in functions called methods
* classes allow you to create an object with unique methods
* all classes should have an __init__ and __str__ method defined
* "self" is never passed as an argument
```python
class Character:
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s

    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health

def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()

example()
```

### Sets

* allows you to keep track of collections of data
* they are an unordered collection of data with no duplicates
```python
names = set(["Mical", "Myranda", "Biscuit"])
print names
```
