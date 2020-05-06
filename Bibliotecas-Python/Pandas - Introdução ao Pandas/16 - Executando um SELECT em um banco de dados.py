import pandas as pd
import mysql.connector


ligacao = mysql.connector.connect(host='localhost', user='root', passwd='', database='rf_db_v')

query = "select * from pessoas"

ler = pd.read_sql(query, con=ligacao)

ler.to_csv('rf_db_v.csv', index=False)

