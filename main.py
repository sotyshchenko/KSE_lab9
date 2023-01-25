import inline as inline
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#print(titles["type"].unique)
# TASK 1

scores_shows = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()
plt.hist(scores_shows, np.arange(0, 10.2, 0.2))
plt.xlabel('imdb score')
plt.ylabel('frequency')
plt.title('SHOWS')
mean_shows = titles[titles["type"] == "SHOW"]["imdb_score"].mean()
plt.annotate(f'mean score = {round(mean_shows, 2)}', xy=(0, 50), xytext=(0, 50))
plt.show()

scores_movies = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
plt.hist(scores_movies, np.arange(0, 10.2, 0.2))
plt.xlabel('imdb score')
plt.ylabel('frequency')
plt.title('MOVIES')
mean_movies = titles[titles["type"] == "MOVIE"]["imdb_score"].mean()
#plt.text(50, 3, r'$\{mean_movies}$')
plt.annotate(f'mean score = {round(mean_movies, 2)}', xy=(0, 50), xytext=(0, 50))
plt.show()


