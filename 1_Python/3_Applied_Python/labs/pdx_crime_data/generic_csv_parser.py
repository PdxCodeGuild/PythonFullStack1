import string
import csv
import glob

class CSVDataParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def extract_header_rows(self):
        with open(self.file_name, 'r') as csv_file:
            csv_rows = csv_file.readline()
            csv_rows = csv_rows.split(',')
            csv_rows = [row.casefold() for row in csv_rows]
            csv_rows = [row.strip(string.punctuation).strip() for row in csv_rows]
            csv_rows = [row.replace(' ', '_') for row in csv_rows]
            return csv_rows

    def generate_row_class(self, class_name):
        _class = f'''
class {class_name}:
    __slots__ = {self.extract_header_rows()}

    def __init__(self, **kwargs):
        [setattr(self, arg, value) for arg, value in kwargs.items()]
        '''
        exec(_class)
        self.csv_row_class = eval(class_name)
        return self.csv_row_class

    def parse(self, file_to_parse=''):
        file_to_parse = file_to_parse if file_to_parse else self.file_name
        csv_objects = list()

        with open(file_to_parse, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            next(csv_data)

            csv_row_names = self.extract_header_rows()

            for row in csv_data:
                csv_row = dict(zip(csv_row_names, row))
                csv_objects.append(self.csv_row_class(**csv_row))

        return csv_objects

    def parse_files_in_directory(self, directory):
        rows = list()

        for csv_file in glob.glob(f'{directory.rstrip("/")}/*.csv'):
            rows += self.parse(csv_file)

        return rows
