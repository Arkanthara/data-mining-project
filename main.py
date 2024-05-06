import numpy as np
from classifier import Classifier


MyClassifier = Classifier()
MyClassifier.open_file()
print(MyClassifier.str2int())

print(np.unique(MyClassifier.data[:, 0]))
print(len(np.unique(MyClassifier.data[:, 0])))
print(len(MyClassifier.data))
