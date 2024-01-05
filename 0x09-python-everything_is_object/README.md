# Alx tasks: Everything is object

* 0-answer.txt: a function used to get the type of objects in python
* 1-answer.txt: get the variable identifier (which is the memory address in the CPython implementation)
* 2-answer.txt: do a, and b point to the same object: ">>> a = 89, b = 100"
* 3-answer.txt: do a, and b point to the same object: ">>> a = 89, b = 89"
* 4-answer.txt: do a, and b point to the same object: ">>> a = 89, b = a"
* 5-answer.txt: do a, and b point to the same object: ">>> a = 89, b = a + 1"
* 6-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = s1
print(s1 == s2)
```
* 7-answer.txt: print the output of the following code   
```python
s1 = "Best School"
s2 = s1
print(s1 is s2)
```
* 8-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = "Best school"
print(s1 == s2)
```
* 9-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = "Best school"
print(s1 is s2)
```
* 10-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)
```
* 11-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)
```
* 12-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```
* 13-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l2
print(l1 is l2)
```
* 14-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
* 15-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l2
l1 = l1 + [4]
print(l2)
```
* 16-answer.txt: print the output of the following code  
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* 17-answer.txt: print the output of the following code  
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* 18-answer.txt: print the output of the following code  
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
* 19-copy_list.py: create a function with max 3-line long to copy a list
* 20-answer.txt: is (a) a tuple?  ( >>> a = () )
* 21-answer.txt: is (a) a tuple? ( >>> a = (1, 2) )
* 22-answer.txt: is (a) a tuple? ( >>> a = (1) )
* 23-answer.txt: is (a) a tuple? ( >>> a = (1, ) )
* 24-answer.txt: print the output of the following code  
```python
a = (1)
b = (1)
a is b
```
* 25-answer.txt: print the output of the following code  
```python
a = (1, 2)
b = (1, 2)
a is b
```
* 26-answer.txt: print the output of the following code  
```python
a = ()
b = ()
a is b
```
* 27-answer.txt: will the id of 'a' change?  
```python
a = [1, 2, 3, 4]
id(a)
a = a + [5]
id(a)
```
* 28-answer.txt: will the id of 'a' change?  
```python
a = [1, 2, 3, 4]
id(a)
a += [5]
id(a)
```
* 100-magic_string.py: a function magic_string() that returns a string “BestSchool” n times the number of the iteration (following the format fount in 100-main.py)  

* 101-locked_class.py: a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

* 103: Assuming we are using a CPython implementation of Python3 with default options/configuration:
```python
a = 1
b = 1
```  
How many int objects are created by the execution of the first line of the script? (103-line1.txt)  
How many int objects are created by the execution of the second line of the script (103-line2.txt)

* 104:  
```python
a = 1024
b = 1024
del a
del b
c = 1024
```
How many int objects are created by the execution of the first line of the script? (104-line1.txt)  
How many int objects are created by the execution of the second line of the script (104-line2.txt)  
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)  
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)  
How many int objects are created by the execution of the last line of the script (104-line5.txt)  

* 105: Assuming we are using a CPython implementation of Python3 with default options/configuration:  
```python
print("I")
print("Love")
print("Python")
```
Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)

* 106:  
```python
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```

How many string objects are created by the execution of the first line of the script? (106-line1.txt)  
How many string objects are created by the execution of the second line of the script (106-line2.txt)  
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)  
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)  
How many string objects are created by the execution of the last line of the script (106-line5.txt)  
