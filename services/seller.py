import sqlite3
import pandas as pd
from db.connection import connect_db


class Seller:
    '''Seller singleton that use for fetch seller related data
    '''

    def get_seller_count_order():
        '''get grouped seller count of orders from db
        '''
        conn = connect_db()
        sql = '''SELECT seller_id, count(*) as total from olist_order_items_dataset ood group by seller_id'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_seller_city_total():
        '''get seller city that grouped to count most city
        from the seller that selling from database
        '''
        conn = connect_db()
        sql = '''SELECT seller_city, count(*) as total from olist_sellers_dataset osd inner join olist_order_items_dataset ood on osd.seller_id  = ood.seller_id group by seller_city;'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result
