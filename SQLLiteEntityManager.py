'''
Created on Jan 11, 2019

@author: Rajit
'''

import sqlite3
from sqlite3 import Error


dropA = "DROP TABLE week_with_max_commit";
dropB = "DROP TABLE day_with_max_commit";
dropC = "DROP TABLE punch_card";
dropD = "DROP TABLE participation";
    
A = "CREATE TABLE IF NOT EXISTS week_with_max_commit ( week_number integer );"
B = "CREATE TABLE IF NOT EXISTS day_with_max_commit ( commit_count integer,day_of_max_commit text);"
C = "CREATE TABLE IF NOT EXISTS punch_card ( day integer,hour integer,commit_count integer);"    
D = "CREATE TABLE IF NOT EXISTS participation ( week_number integer,commit_count integer);"  

def get_drop_query(req):
    if(req=='A'):
        return dropA
    if(req=='B'):
        return dropB
    if(req=='C'):
        return dropC
    if(req=='D'):
        return dropD
    
def get_create_query(req):
    if(req=='A'):
        return A
    if(req=='B'):
        return B
    if(req=='C'):
        return C
    if(req=='D'):
        return D

def get_database_path():
    database = "pythonsqlite.db"
    return database;

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall();
    for row in rows:
        print(row)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit();
    except Error as e:
        print(e)
        
def insert_table(conn, insert_table_sql):
    try:
        c = conn.cursor()
        c.execute(insert_table_sql)
        conn.commit();
    except Error as e:
        print(e)
        
def drop_table(conn,drop_table_sql):
    try:
        c = conn.cursor()
        c.execute(drop_table_sql)
        conn.commit();
    except Error as e:
        print(e)
        
      

        
def main():
    database = "C:\\Users\\jeev5\\Documents\\U\\Python Workstation\\advanced-md\\pythonsqlite.db"
    sql_create_projects_table = " CREATE TABLE IF NOT EXISTS tasks ( id integer PRIMARY KEY,name text NOT NULL,begin_date text,end_date text);"
    
    
      
    
    
    
    conn = create_connection(database)
    #create_table(conn, A);
    #create_table(conn, B);
    #create_table(conn, C);
    #create_table(conn, D);
    
    drop_table(conn, dropA);
    drop_table(conn, dropB);
    drop_table(conn, dropC);
    drop_table(conn, dropD);
    
    
    
    
    #sql_insert_projects_table = "INSERT into tasks values(10,'JeevanA',null,null);"
    
    
    
    #
    #insert_table(conn, sql_insert_projects_table);
    #select_all_tasks(conn)
    
    '''if conn is not None:
        # create projects table
        insert_table(conn, sql_insert_projects_table)
    else:
        print("Error! cannot insert into the database connection.");'''
    
    '''if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")'''
    '''with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)'''
 
 
if __name__ == '__main__':
    main()