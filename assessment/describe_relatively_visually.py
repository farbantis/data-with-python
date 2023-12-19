import pandas as pd
from scipy.stats import linregress

def describing_data_1_2(link):
    # 1 - is age closely related to income?
    county_level_df = pd.read_excel(link, sheet_name='county-level')
    print(county_level_df.info())
    x = county_level_df['Age']
    y = county_level_df['Income']
    regression = linregress(x, y)
    print(regression)
    print(f'slope: {regression.slope}, intercept: {regression.intercept}, r_value: {regression.rvalue}')
    # 2. Could Population predict Income?
    x = county_level_df['Population']
    y = county_level_df['Income']
    regression = linregress(x, y)
    print(f'the r_value which shows correlations is {regression.rvalue}')
    # r-value is 0.11 which shows that the dependency is low.


def describing_data_3(link):
    """firstlanguage contains empty rows"""
    # 3. Does Stress predict Wellbeing?
    df = pd.read_csv(link)
    print(df.info())
    columns = df.columns
    result = dict()
    for column in columns:
        if column != 'Wellbeing':
            try:
                x = pd.to_numeric(df[column])
                regression = linregress(x, df['Wellbeing'])
                if abs(regression.rvalue) > 0.5:
                    result[column] = regression.rvalue
            except ValueError:
                print()
    # best_r_value = max(result.values(), key=lambda x: abs(x))
    print(f'the good correlation is for: {result}')


url = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/Income-Data.xlsx?raw=true'
describing_data_1_2(url)

url3 = "https://github.com/lilaceri/Working-with-data-/blob/b157a2feceb7709cf82426932385706d65446270/Data%20Sets%20for%20code%20divisio/Positive_Psychology_2017.csv?raw=true"
describing_data_3(url3)
