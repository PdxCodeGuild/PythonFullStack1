from collections import namedtuple
from datetime import datetime
from pprint import pprint
from itertools import groupby

# Create a namedtuple to store our rain data.
RainDataPoint = namedtuple('RainDataPoint', 'date_recorded, rain_total, rainfall_by_hour')

def strip_file_header(data):
    """
    Scan the data for the end of the header, and return a slice from the next item.

    """
    for line_no, line_data in enumerate(data):
        if set(line_data.strip()) == set('-'):
            return data[line_no+1:]


def parse_data_from_file(file_name):
    """
    Parse the data from a specified file, format it and return a list of namedtuples.

    """
    rain_data = list()
    measurements = list()

    with open(file_name, 'r') as f:
        rain_data = strip_file_header(f.readlines())

    for measurement in rain_data:
        measurement = measurement.split()
        measurement = [value.strip() for value in measurement]

        if '-' in measurement:
            continue

        date_recorded = measurement.pop(0)
        date_recorded = datetime.strptime(date_recorded, '%d-%b-%Y')

        rain_total = int(measurement.pop(0))

        rainfall_by_hour = [int(total) for total in measurement]

        measurements.append((date_recorded, rain_total, rainfall_by_hour))

    return list(map(RainDataPoint._make, measurements))

def analyze_data(data):
    """
    Run some analytics on the data we've parsed!
    Print the raniest day and the raniest year.
    """
    # rain_data = list(sorted(data, key=lambda d: d.rain_total, reverse=True))
    rain_data = [max(data, key=lambda d: d.rain_total)]
    rainiest_day = rain_data[0].date_recorded.strftime("%x")

    # This is ****ed.
    # # Get all the unique occurances of years.
    # years = set(map(lambda d: d.date_recorded.year, data))
    # # Split our data into lists by year.
    # data_by_year = list(map(lambda x: list(filter(lambda y: y.date_recorded.year == x, data)), years))
    # # Zip a dictionary with year as the key and the data for each year.
    # data_by_year = dict(zip(years, data_by_year))
    # # Assert that the above worked!
    # assert {k == list(v)[:1][0].date_recorded.year for k, v in data_by_year.items()} == {True,}
    # # Jesus christ!!!
    #
    # rainfall_per_year = {k : sum(day.rain_total for day in v) for k, v in data_by_year.items()}
    # rainiest_year = max(rainfall_per_year, key=rainfall_per_year.get)


    # rainfall_per_year = groupby(data, key=lambda d: d.date_recorded.year)
    # rainfall_per_year = {k : sum(d.rain_total for d in list(g)) / 100 for k, g in rainfall_per_year}

    rainfall_per_year = {key : sum(value.rain_total for value in group) for key, group in groupby(data, key=lambda d: d.date_recorded.year)}

    rainiest_year = max(rainfall_per_year, key=rainfall_per_year.get)

    groups = groupby(data, key=lambda d: d.date_recorded.year)

    # Our output dictionary
    rainfall_per_year = dict()

    # Iterate over our keys and groups
    for key, group in groups:
        # Store a value for our sum.
        _sum = 0

        # Iterate over each item in the group.
        for value in group:
            # Add that to our sum.
            _sum += value.rain_total

        # Add our computed sum to our output_dictionary.
        rainfall_per_year[key] = _sum

    # print('-' * 50)
    # print(f'Rainiest day of the dataset: On {rainiest_day} it rained {rain_data[0].rain_total / 100} inches.')
    # print(f'Rainiest year of the dataset: In {rainiest_year} it rained {rainfall_per_year[rainiest_year]} inches.')
    # print('-' * 50)


if __name__ == '__main__':
    data = parse_data_from_file('sample.rain')
    analyze_data(data)
