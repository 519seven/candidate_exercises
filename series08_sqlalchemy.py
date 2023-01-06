#!/usr/bin/env python

#   Series 8

#
# # Topic
# # # Interacting with database using sqlalchemy and pandas dataframe
#
# # Challenge Level
# # # Medium
#
# # Description
# # # 1) Create table in your database using the information found in
#        mysql.show_drop_create.sh script
#     2) Populate table with data in sample_data directory
#     3) Query data
#
# # Your Solutions' Relative Levels:
# # # - N/A
#
## Example Use Cases(s)
# # # - N/A
#
# *******************************************************************
from dotenv import load_dotenv
from sqlalchemy import create_engine, types
import pymysql
import pandas as pd
from os import getenv
import csv
import sys

load_dotenv()
CSVFILE = getenv("CSV_FILE_PATH", "data/sample.csv")
DB_TYPE = getenv("DB_TYPE", "mysql+pymysql")
DB_HOST = getenv("DB_HOST", "localhost")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
DB_NAME = getenv("DB_NAME")
DEBUG = True if getenv("DEBUG") == "True" else "False"

# ps = Population By Sex
TABLE_NAME = getenv("TABLE_NAME", "ps_Zimbabwe")
print(f"Using TABLE_NAME set to {TABLE_NAME}")

class DB:

    def __init__(self, db_user, db_pass, db_name, db_type, db_host):
        self.db_type = db_type
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.connstr = f"{db_type}://{db_user}:{db_pass}@{db_host}/{db_name}" 

    def read_csv_into_table(self, table_name, csv_file):
        engine = create_engine(self.connstr)
        dbconn = engine.connect()
        # read csv into dataframe 
        df = pd.read_csv(csv_file, sep=',', quotechar='\'', encoding='utf-8')
        # send it!
        try:
            df.to_sql(table_name, con=dbconn, index=False, if_exists='fail')
        except ValueError as verr:
            if "table exists" in str(verr):
                print("Table exists, not inserting data")
        dbconn.close()
        return True

    def show_data(self, sql_statement):
        engine = create_engine(self.connstr)
        dbconn = engine.connect()
        # read data from table into dataframe
        df = pd.read_sql(sql_statement, con=dbconn)
        pd.set_option('display.expand_frame_repr', False)
        print(df)
        dbconn.close()
        return True

def failure(msg):
    print(f"Unable to {msg}")
    sys.exit(1)

def main():
    if DEBUG:
        print("Using:")
        print(f"   DB_HOST={DB_HOST}")
        print(f"   DB_USER={DB_USER}")
        print(f"   DB_PASS={DB_PASS}")
        print(f"   DB_NAME={DB_NAME}")
    my_db = DB(DB_USER, DB_PASS, DB_NAME, DB_TYPE, DB_HOST)
    if my_db.read_csv_into_table(TABLE_NAME, CSVFILE):
        limit = 20
        sql_statement = "SELECT * FROM {} LIMIT {};"
        if not my_db.show_data(sql_statement.format(TABLE_NAME, limit)):
            failure()

if __name__ == "__main__":
    main()
