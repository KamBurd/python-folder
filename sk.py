import sklearn
import pandas as pd
from sklearn.datasets import load_iris
iriss = load_iris()
df_iris = pd.DataFrame(iriss.data, columns=iriss.feature_names)
