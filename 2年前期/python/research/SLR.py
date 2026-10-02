import pandas as pd
from sklearn.datasets import load_boston

bs = load_boston()
df = pd.read_csv(bs.filename, header =1)
df


