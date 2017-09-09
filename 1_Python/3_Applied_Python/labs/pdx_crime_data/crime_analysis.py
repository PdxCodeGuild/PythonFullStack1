import itertools
import glob

from datetime import datetime
from collections import OrderedDict

from generic_csv_parser import CSVDataParser

def group_by_attribute(data_set, attribute):
    # Create a dynamic key function with our attribute string.
    key = eval(f'lambda x: x.{attribute}')
    # Sort our data by our key function...
    sorted_data = sorted(data_set, key=key)
    # Dictionary comprehension out our itertools.groupby values.
    groups = {k : list(v) for k, v in itertools.groupby(sorted_data, key)}
    return groups

def parse_date_for_rows(data_set):
    for obj in data_set:
        obj.report_date = datetime.strptime(obj.report_date, '%m/%d/%Y')
        obj.report_time = datetime.strptime(obj.report_time, '%X')

def get_by_occurance(data_set):
    return sorted(data_set.items(), key=lambda x: len(x[1]), reverse=True)

parser = CSVDataParser('data/crime_incident_data_2011.csv')
parser.generate_row_class('Crime')
crime_data = parser.parse_files_in_directory('data')

parse_date_for_rows(crime_data)

print('\nTop 10 neighborhoods in order of crime occurances:\n'
      '-------------------------------------------\n')

for neighborhood, crimes in get_by_occurance(group_by_attribute(crime_data, 'neighborhood')):
    print(neighborhood, len(list(crimes)))

print('\nTop 10 crime types in by occurance:\n'
      '----------------------------\n')
for offense, crimes in get_by_occurance(group_by_attribute(crime_data, 'major_offense_type')):
    print(offense, len(list(crimes)))

print('\nTop years for crime:\n'
      '----------------------------\n')
for k, v in get_by_occurance(group_by_attribute(crime_data, 'report_date.year')):
    print(k, len(list(v)))

print('\n')
