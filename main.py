import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("credits.csv")
print(credits)
credits.head()

credits.info()

print(credits["character"].isna())

print(np.unique(credits["role"], return_counts=True))

na_characters = credits[credits["character"].isna()]

print(np.unique(na_characters["role"], return_counts=True))

print(credits["role"])

# Маска
print((credits[(credits["role"] == "ACTOR") & ~ (credits["id"] == "tm1059008")]))

titles = pd.read_csv("titles.csv")
print(titles.shape)
titles.head()

titles.info()

print(titles["type"].unique)
print(titles["imdb_score"])
