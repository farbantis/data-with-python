import pandas as pd
import psycopg2
from decimal import Decimal
from prettytable import PrettyTable

db_user = 'girosman'
db_password = 'ghjdjlf'
db_host = '191.96.53.71'
db_port = '5432'
db_name = 'postgres'

conn = psycopg2.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

cursor = conn.cursor()

# find max salary for departments for employees hired after 01/01/97
# sql_query = """
# SELECT department_name, MAX(salary) as max_salary, MIN(hire_date) as earlierst_date_hired
# FROM employees
# INNER JOIN departments
# ON employees.department_id = departments.department_id
# WHERE hire_date > '1997-01-01'
# GROUP BY department_name
# ORDER BY MAX(salary) DESC
# """

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
        WHEN salary > 50000 THEN 'high salary'
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

cursor.execute(sql_query)
conn.commit()
result = cursor.fetchall()
cursor.close()
conn.close()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(result, columns=columns)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df['salary_after_tax'] = (df['salary'] - 1200) * Decimal('0.8') + 1200
position = df.columns.get_loc('salary') + 1
df.insert(position, 'salary_after_tax', df.pop('salary_after_tax'))

table = PrettyTable()
table.field_names = df.columns
for row in df.itertuples(index=False):
    table.add_row(row)
print(table)
#print(df.head(50))
