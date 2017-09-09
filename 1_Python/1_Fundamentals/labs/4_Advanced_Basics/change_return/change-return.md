# Lab: Change Return

###### Delivery Method: Doctests

------------------------------

##### Goal

Write a python script that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

---------------------------------------------------------

##### Instructions

Some supermarkets have automatic change dispensers.

*   Ask for the amount of change to dispense _in cents_.
    Assume that the amount input will be less than 100 cents.

*   Calculate the number of quarters necessary first.

*   Then calculate the number of dimes, nickels, and pennies.
    If you do it in that order, you will minimize the number of coins.

This is easiest done by updating a _running total_ of number of cents left to be put into coins.

Also remember that the `//` operator divides and removes any remainder.

------------------

#### Documentation

##### [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

-----------------

#### Advanced

* Expand this problem to work on an amount of cents greater than 100 and include bills.
* Print out the total number of coins and bills dispensed.

--------------------
#### Super Advanced

* Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don't have enough coins to optimally give change.

------------------

#### Key Concepts

- Operators
- Variables
- Data Types
- PEP8
