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

# conn = psycopg2.connect(
#     user=db_user,
#     password=db_password,
#     host=db_host,
#     port=db_port,
#     database=db_name
# )
#
# cursor = conn.cursor()



# cursor.execute(sql_query)
# conn.commit()
# result = cursor.fetchall()
# cursor.close()
# conn.close()

# columns = [desc[0] for desc in cursor.description]
# df = pd.DataFrame(result, columns=columns)
