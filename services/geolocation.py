import sqlite3
import pandas as pd
from db.connection import connect_db


class Geolocation:
    '''Geolocation singleton that use for fetch geolocations related data
    '''

    def get_geolocation():
        '''get all geolocation from db
        '''
        conn = connect_db()
        sql = '''SELECT * from olist_geolocation_dataset'''

        try:
            result = pd.read_sql_query(sql, conn)
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result
