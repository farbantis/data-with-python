import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    port="3306",
    user ="guest",
    password ="relational",
    database="SalesDB"
)

def execute_query(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    try:
        records = mycursor.fetchall()
        return records
    except:
        print("An error occurred: ")
        return None

result = execute_query("SELECT * FROM SalesDB")
df = pd.DataFrame(result)
