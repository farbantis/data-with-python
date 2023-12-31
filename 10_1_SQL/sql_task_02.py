import pandas as pd
import psycopg2
from password import db_password

db_user = 'girosman'
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
sql_query = "SELECT * FROM skill_migration WHERE country_name = 'Afghanistan' and wb_income='Low income'"


cursor.execute(sql_query)
conn.commit()
result = cursor.fetchall()
cursor.close()
conn.close()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(result, columns=columns)

print(df.head(50))
