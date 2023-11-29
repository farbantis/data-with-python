import matplotlib
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def movies_project(data):
    df = pd.read_csv(data)
    #print(df.info())
    blanks = df.isna().any()
    # movies of each genre in descending order
    movies_of_each_genre = df.groupby(['genre'])['genre'].count().sort_values(ascending=False)
    # director with the highest rank -> turned out there lots of them
    director_rank_2 = df[df['rank'] == df['rank'].max()]
    director_rank_2 = director_rank_2['first_name'].unique()
    # quantity of movies with the rank over 9
    rank_over_9 = df[df['rank'] > 9].value_counts().count()
    # bar for mean rank and genre
    grouped_genres = df.groupby(['genre'])['rank'].mean()
    labels_bar = grouped_genres.keys()
    fig, ax = plt.subplots()
    plt.bar(labels_bar, grouped_genres)
    plt.show()

    return blanks, movies_of_each_genre, director_rank_2, rank_over_9

#link = "https://github.com/lilaceri/Working-with-data-/blob/main/Data%20Sets%20for%20code%20divisio/movies.csv?raw=true"
link = 'movie.csv'
result = movies_project(link)
text = ('checking for blanks', 'movies per genre:',
        'surnames of director with the highest rank', 'movies with rank over 9')
for index, value in enumerate(result):
    print()
    print(text[index])
    print(value)
    print()
