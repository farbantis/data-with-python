import pandas as pd


def get_statistics(titanic):
    print(titanic.info())
    passengers = titanic['PassengerId'].nunique()
    youngest = titanic['Age'].min()
    most_expensive = titanic['Fare'].max()
    range_ticket = titanic['Fare'].median()
    no_cabins = titanic['Cabin'].count()
    embarked = titanic['Embarked'].mode()
    gender = titanic['Sex'].mode()
    sd = titanic['Age'].std()
    return passengers, youngest, most_expensive, range_ticket, no_cabins, embarked[0], gender[0], sd


titanic = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv')

actual = get_statistics(titanic)
expected = (891, 0.42, 512.3292, 512.3292, 204, 'S', 'male', 14.526497332334044)
print(actual)
print(expected)
if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed, expected", expected, "but got", actual)
