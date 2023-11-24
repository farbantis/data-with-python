import pandas as pd


def get_grouped(titanic):
    sex_age = titanic.groupby(['Sex'])['Age'].mean()
    mean_ticket_price_sex = titanic.groupby(['Pclass', 'Sex'])['Fare'].mean()
    mean_ticket_price_port = titanic.groupby(['Embarked'])['Fare'].mean()
    survivors = titanic.groupby(['Pclass'])['Survived'].sum()
    survivors_1 = titanic[titanic['Survived']==1].groupby('Pclass')['Survived'].value_counts()
    return sex_age, mean_ticket_price_sex, mean_ticket_price_port, survivors, survivors_1


titanic = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv')
result = get_grouped(titanic)

for i in result:
    print(i)
    print()
