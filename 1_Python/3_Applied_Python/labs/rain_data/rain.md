# Practice: Rain

The city of Portland has rain gauges that keep track of rainfall.
[A website](http://or.water.usgs.gov/non-usgs/bes/) has text data tables the history of all the daily measurements at these gauges.

It looks like:

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

The amounts are in hundredths of inches or are a `-` if the sensor was broken.

Print out a summary of the data:

* The specific date with the most rain.
* The year with the most rain.

#### Note:
1. The header has a totally different format than the data itself.  You will have to slice out the header lines from all the lines you read.

2. You can split a string by whitespace into a list of strings using `.split()`.

3. Extract the date sting from the date columns.

4. If there are any days with `-` for data, explicitly drop them from your dataset.

5. Avoid using un-named "pairs" outside of dictionaries.

6. If you need to group together individual instances of a date and a rainfall amount use a tuple! ( Or perhaps look at the namedtuple form collections. )

## Advanced

*   Find and print the day of the year with the most rain on average.
    E.g. December 30th has 1" of rain on average.

*   Allow someone to type in a date in the future and, using the average value for that day of the year, predict the amount of rain.

## Super Advanced

* URL open the [main listing website](http://or.water.usgs.gov/non-usgs/bes/).
Parse it and allow the user to select statistics from the available rain gauges.

Python gives you a module called `urllib.request` you can use a function `urllib.request.urlopen(url)` which returns a file-like object.
Look at [the docs](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for that module.

One little difference is the file-like object doesn't return strings, it returns **bytes**.
The following code snippet reads Pride and Prejudice into a list of strings:

```py
import urllib.request

with urllib.request.urlopen('http://www.gutenberg.org/ebooks/1342.txt.utf-8') as pride_and_prejudice_file:
  lines = [byte_line.decode('utf-8') for byte_line in pride_and_prejudice_file]
```

Read up on using [Pip and PyPI](/notes/py-pip.md) and installing third-party packages.
Use the `beautifulsoup` package to parse the HTML of that page.
You shouldn't hard code in any input other than the listing URL.
