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

    def str2int(self, test_data: str="coucou") -> np.ndarray:
        """
        Format string to int numbers
        """
        tab = np.array(list(test_data))

        return tab.view(np.int32)
