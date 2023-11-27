import pandas as pd
import psycopg2
import mysql.connector
from sqlalchemy import create_engine


skill_migration = pd.read_excel('https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true', "Skill Migration")

db_user = 'girosman'
db_password = 'ghjdjlf'
db_host = '191.96.53.71'
db_port = '5432'
db_name = 'postgres'

connection_str = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
skill_migration.to_sql('skill_migration', engine, if_exists='replace', index=False)
