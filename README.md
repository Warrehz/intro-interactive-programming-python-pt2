# intro-interactive-programming-python-pt2
Compilation of exercises and notes from Rice Universities - Introduction to Interactive Programming in Python (Part 2).

## Notes

* lists are the backbone of python programming - similar to a JavaScript array
* tuple is a list that is immutable - they cannot be changed
```python
tup1 = ("Monday", 6, 2017, "Hungry");
```
* "in" allows you to check for data in tuples or lists by evaluating to True or False
```python
6 in tup1 => True

if 2017 in tup1:
  print  "Yeah it's there."
```
* index will tell you where an item is in the lists
```python
tup1.index(2017); => 2
```
