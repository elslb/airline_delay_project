import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

pd.set_option("max_columns", None)

df = pd.read_csv("../../data/airline_sample_10k.csv")

df = df.drop('no_name', axis = 1)