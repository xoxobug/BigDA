import pandas as pd
import mysql.connector

try:
    sql = mysql.connector.connect(
        host='localhost',
        database='db_sma2',
        user='root',
        password='',

    )
    if sql.is_connected():
        print('Database connected.')

except mysql.connector.Error as error:
    print('Error establishing db connection:', error)

sql_query = pd.read_sql_query(''' 
                              SELECT * FROM `tbl_scraping` ORDER BY `tbl_scraping`.`follower_count` DESC
                              '''
                              ,sql)

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\Ali\Desktop\exported_data.csv', index = False)
