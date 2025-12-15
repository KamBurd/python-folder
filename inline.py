%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd

from aklearn.datasets import load_iris


data = load_iris
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = data.target
df.head()
