import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from decimal import Decimal
from prettytable import PrettyTable
from sqlalchemy import create_engine

db_user = 'girosman'
db_password = 'ghjdjlf'
db_host = '191.96.53.71'
db_port = '5432'
db_name = 'postgres'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# find all people working in a department with min salary, showing their full name, dep, job title, salary
# with adding a field to comment salary level
sql_query = """
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    department_name,
    INITCAP(REPLACE(LOWER(job_title), 'purchasing', '')) AS position,
    salary,
    salary * 12 AS salary_per_year,  
    CASE 
        WHEN salary < 3000 THEN 'low salary'
        WHEN salary BETWEEN 3000 AND 5000 THEN 'middle salary'
        WHEN salary > 5000 THEN 'high salary'
        ELSE 'wrong data'
    END as comment_to_salary    
FROM employees
INNER JOIN departments
    ON employees.department_id = departments.department_id
INNER JOIN jobs
    ON employees.job_id = jobs.job_id
WHERE employees.department_id = (
    SELECT department_id
    FROM employees
    GROUP BY employees.department_id
    ORDER BY MIN(salary) ASC
    LIMIT 1)
"""

df = pd.read_sql_query(sql_query, engine)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df['salary_after_tax'] = (df['salary'].apply(Decimal) - 1200) * Decimal('0.8') + 1200
position = df.columns.get_loc('salary') + 1
df.insert(position, 'salary_after_tax', df.pop('salary_after_tax'))


pie_df = df.groupby(['comment_to_salary'])['salary_per_year'].sum().reset_index()
labels = pie_df['comment_to_salary']
figures = pie_df['salary_per_year']
fig, ax = plt.subplots()
colors = ['red', 'green', 'yellow']
hatch=['**O', 'oO', 'O.O', '.||.']
explode = [0.1, 0.1, 0.1]
textprops={'size': 'smaller'}
ax.pie(figures,
       labels=labels,
       autopct='%1.1f%%',
       colors=colors,
       pctdistance=0.6,
       labeldistance=1.1,
       shadow=True,
       startangle=90,
       explode=explode,
       radius=1.3,
       textprops=textprops)
plt.show()

# table = PrettyTable()
# table.field_names = df.columns
# for row in df.itertuples(index=False):
#     table.add_row(row)
# print(table)
#print(df.head(50))
