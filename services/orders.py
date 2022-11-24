import sqlite3
import pandas as pd
from db.connection import connect_db


class Order:
    '''Order singleton that use for fetch orders related data
    '''

    def get_orders():
        '''get all orders from db
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_dataset'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_order_items(orderId: str):
        '''get all orders from db
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_items_dataset WHERE order_id = {orderId}'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_order_items(orderId: str):
        '''get all order items from db where orderId = ?
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_items_dataset WHERE order_id = {orderId}'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_order_reviews(orderId: str):
        '''get all order reviews from db where orderId = ?
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_items_dataset WHERE order_id = {orderId}'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_order_reviews(orderId: str):
        '''get all order reviews from db where orderId = ?
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_order_items_dataset WHERE order_id = {orderId}'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def get_order_payment():
        '''get get_order_payment order payments and aggregate
        '''
        conn = connect_db()
        sql = '''
            WITH payment_order AS (
                select * from olist_order_payments_dataset oopd inner join olist_order_dataset ood on oopd.order_id  = ood.order_id
            )
            select payment_type, count(*) as total from payment_order group by payment_type
        '''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result
