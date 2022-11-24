import sqlite3
import pandas as pd
from db.connection import connect_db


class Customer:
    '''Customer singleton that use for fetch customers related data
    '''

    def get_customers():
        '''get all customers from db
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_customer_dataset'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_customers_count_by_city():
        '''get all customers count by city from db
        '''
        conn = connect_db()
        sql = '''SELECT customer_city, count(*) as total from olist_order_customer_dataset oocd group by customer_city order by count(*) desc LIMIT 5'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_customers_and_city():
        '''get all customers and city from db
        using INNER JOIN 
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_customer_dataset oocd INNER JOIN (select DISTINCT geolocation_city FROM olist_geolocation_dataset) ogd ON oocd.customer_city = ogd.geolocation_city'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result
