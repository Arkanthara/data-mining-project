import csv

import numpy as np


class Classifier:

    def __init__(self, column: int = 0):
        self.data = None
        self.header = None
        self.list_char = None
        self.max_len = 0

        result = ''
        for i in range(self.data.shape[0]):
            result += self.data[i, column]
        self.list_char = np.sort(np.unique(np.array(list(result))))

        def getsize(string: str) -> int:
            return len(string)

        getsizetab = np.vectorize(getsize)

        self.max_len = max_len = np.max(getsizetab(self.data[:, column]))



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
        result = ''
        for i in range(self.data.shape[0]):
            result += self.data[i, column]
        self.list_char = np.sort(np.unique(np.array(list(result))))

        def getsize(string: str) -> int:
            return len(string)

        getsizetab = np.vectorize(getsize)

        self.max_len = max_len = np.max(getsizetab(self.data[:, column]))



    def str2int(self, test_data: str="coucou") -> np.ndarray:
        """
        Format string to int numbers
        """
        tab = np.array(list(test_data))

        return tab.view(np.int32)

    def getnumberofchar(self, column: int) -> int:

        result = ''
        for i in range(self.data.shape[0]):
            result += self.data[i, column]
        return len(np.unique(np.array(list(result))))

    def format_data(self, column: int):

        nb_chars = self.getnumberofchar(column)

        max_len = self.data[:, column]

        def getsize(string: str) -> int:
            return len(string)

        getsizetab = np.vectorize(getsize)

        max_len = np.max(getsizetab(self.data[:, column]))

        print(getsizetab(self.data[:, column])[0])
        print(self.data[0, column])
        print(max_len)
