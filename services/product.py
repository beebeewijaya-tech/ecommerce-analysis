import sqlite3
import pandas as pd
from db.connection import connect_db


class Product:
    '''Product singleton that use for fetch products related data
    '''

    def get_products_categories_count():
        '''get all product categories from db
        '''
        conn = connect_db()
        sql = '''SELECT product_category_name, count(*) from olist_products_dataset opd group by product_category_name order by count(*) desc'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_products_categories_by_order_count():
        '''get all product categories based on orders from db 
        '''
        conn = connect_db()
        sql = '''
            WITH product_id_agg AS (
                select product_id, count(*) as total from olist_order_items_dataset ooid group by product_id
            )
            select
                opd.product_category_name, count(*) as total
            from olist_products_dataset opd
            inner join product_id_agg p ON opd.product_id = p.product_id
            group by opd.product_category_name
            order by count(*) desc;
        '''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result
