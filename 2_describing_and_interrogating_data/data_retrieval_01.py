import pandas as pd


def summary(titanic):
    print(titanic.head(5))
    print(titanic.info())
    print(titanic.describe())


titanic = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv')
summary(titanic)


