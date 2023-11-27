import pandas as pd


def movies_project(data):
    df = pd.read_csv(data)
    print(df.info())
    blanks = df.isna().any()
    doubles = df.
    movies_of_each_genre = df.groupby(['genre'])['genre'].count()
    # ? how to sort by quantity?
    # director_rank_1 = df.loc[df['rank'].idxmax(), 'first_name']
    director_rank_2 = df[df['rank'] == df['rank'].max()]
    director_rank_2 = director_rank_2['first_name'].unique()
    rank_over_9 = df[df['rank'] > 9].value_counts().count()
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
