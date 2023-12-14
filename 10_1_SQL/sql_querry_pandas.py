import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from decimal import Decimal
from prettytable import PrettyTable
from sqlalchemy import create_engine
from password import db_password

db_user = 'girosman'
db_host = '191.96.53.71'
db_port = '5432'
db_name = 'postgres'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

sql_query = """
SELECT 
    *
FROM employees
INNER JOIN departments
    ON employees.department_id = departments.department_id
INNER JOIN jobs
    ON employees.job_id = jobs.job_id
"""

df = pd.read_sql_query(sql_query, engine)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df['salary_after_tax'] = (df['salary'].apply(Decimal) - 1200) * Decimal('0.8') + 1200
position = df.columns.get_loc('salary') + 1
df.insert(position, 'salary_after_tax', df.pop('salary_after_tax'))
print(df)

# table = PrettyTable()
# table.field_names = df.columns
# for row in df.itertuples(index=False):
#     table.add_row(row)
# print(table)
# print(df.head(50))
