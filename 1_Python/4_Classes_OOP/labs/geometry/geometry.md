# Practice: Geometry

Write a program that can store and manipulate rectangles and points.

Implement two classes: `Point` and `Rectangle` in modules named `point` and `rectangle` respectively.

* Points should store their `x` and `y` coordinates
* Rectangles should store their top left point, then a `w` width and `h` height
* Both should have \_\_repr\_\_ and  \_\_eq\_\_ implemented

Then create some top-level functions in those modules that know how to operate on instances of each class.

In the `point` module:

* Find the distance between two points
* Return a new point moved by a specified amount

In the `rectangle` module:

* Know if a point is inside a rectangle
* Find the center point of a rectangle

All functions, even magic methods, should have tests.

#### Advanced

Create a bunch of Point instances and put them in a container.

Then, Given a single Point instance, return all of the point instances within a given radius.

#### Super Advanced

Implement the Haversine formula to compute the distance between two given points on the earth.  

[Haversine Formula Wiki](https://en.wikipedia.org/wiki/Haversine_formula)

[Haversine Formula Python Stack Overflow](http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
