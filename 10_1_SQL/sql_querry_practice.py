import pandas as pd
import psycopg2

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

# selecting employees with salary > 10_000, concatenating name and surname, add department name
sql_query_1 = """
SELECT CONCAT(first_name, ' ', last_name) as full_name, department_name, salary 
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE salary > 10000
ORDER BY salary DESC
"""

# find max salary for departments for employees hired after 01/01/97
sql_query_02 = """
SELECT department_name, MAX(salary) as max_salary, MIN(hire_date) as earlierst_date_hired
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE hire_date > '1997-01-01'
GROUP BY department_name
ORDER BY MAX(salary) DESC
"""

# find all people working in a department with max salary, showing their full name, dep, job title, salary
# with adding a field to comment salary level
sql_query = """
SELECT first_name, last_name, department_name, job_title, salary, 
    CASE 
        WHEN salary < 10000 THEN 'low salary'
        WHEN salary BETWEEN 10000 AND 20000 THEN 'middle salary'
        WHEN salary > 20000 THEN 'high salary'
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
    ORDER BY MAX(salary) DESC
    LIMIT 1)
"""



cursor.execute(sql_query)
conn.commit()
result = cursor.fetchall()
cursor.close()
conn.close()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(result, columns=columns)

print(df.head(50))
