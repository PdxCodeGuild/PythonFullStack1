# Lab: I before E except after C.

From wikipedia:
"The i before e except after c rule is not worth teaching. It applies only to words in which the ie or ei stands for a clear /ee/ sound and unless this is known, words such as 'sufficient', 'veil' and 'their' look like exceptions."

###### Delivery Method: Prompt

------------------------------

#### Goal

Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".**

Check the solution using the doctest in the heading of the file and simply return whether the word follows the rule or not.



---------------------------------------------------------

#### Instructions

1. Create a file named `spelling.py`
1. Write a function that searches for the index of any instances of `ie` in the string, then see if the preceding letter is `c`.
1. Execute the doctest. To do this:
  * run `$ python -m doctest spelling.py`
1. Save your solution in a Python file in `practice/` in a branch and make a GitHub pull request all named `spelling`.


------------------

#### Documentation


-----------------

#### Advanced

* Find a list of exceptions to use and check if the word given is an exception to the rule.


------------------

#### Key Concepts

- string lookup with `in`
