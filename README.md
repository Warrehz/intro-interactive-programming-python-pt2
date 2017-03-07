# intro-interactive-programming-python-pt2
Compilation of exercises and notes from Rice Universities - Introduction to Interactive Programming in Python (Part 2).

## Notes

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
* append and pop allow you to add or remove an item to the end of the list
```python
lst1.append("Mical"); => ["Monday", 6, 2017, "Hungry", "Mical"];
lst1.pop(); => "Mical"
```
