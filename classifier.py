import csv

import numpy as np


class Classifier:

    def __init__(self):
        self.data = None
        self.header = None
        pass

    def open_file(self, path: str = 'data.csv'):
        """
        Open a csv file and store it in a np.arrray
        """
        import csv
        with open('data.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            data = []
            for row in csvreader:
                data.append(row)

        data = np.array(data)
        self.data = data[1:, :]
        self.header = data[1, :]
        return

    def format_file(self):
        """
        Format a set of data to work only with numbers
        """
        pass
