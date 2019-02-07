'''
Created on Jan 11, 2019

@author: Rajit
'''
import json
from SQLLiteEntityManager import create_connection, get_database_path, drop_table,\
    create_table, insert_table, get_drop_query, get_create_query
from botocore.vendored.requests.compat import str


def jsonToSQLJob():
    print(">>>>>>>>>>Initiating Persistence to SQLLite>>>>>>>>>>")
    conn = create_connection(get_database_path())
    drop_table(conn,get_drop_query('D'))
    create_table(conn,get_create_query('D'))
    
    drop_table(conn,get_drop_query('C'))
    create_table(conn,get_create_query('C'))
    
    with open('participation.json') as json_file:  
        data = json.load(json_file)
        i = 1
        for p in data['all']:
            insert_table(conn,"INSERT INTO participation values("+str(i)+","+str(p)+");")
            i=i+1
    
    
    with open('punch_card.json') as json_file:  
        data = json.load(json_file)
        for p in data:
            insert_table(conn,"INSERT INTO punch_card values("+str(p[0])+","+str(p[1])+","+str(p[2])+");")
                  
    print("<<<<<<<<<<<<<<<<<<Persistence to SQLLite Complete<<<<<<<<<<<<<")       
    
def SolutionToDbJob(type,solutionA,solutionB):
    conn = create_connection(get_database_path())
    
    if(type=="findDayOfMaximumCommit"):
        insert_table(conn, "INSERT INTO day_with_max_commit values("+str(solutionA)+",'"+str(solutionB)+"');")
    if(type=="findTheWeekWithMaxCommit"):
        insert_table(conn, "INSERT INTO week_with_max_commit values("+str(solutionA)+");")

def clean(type):
    if(type=="A"):
        conn = create_connection(get_database_path())
        drop_table(conn,get_drop_query('A'))
        create_table(conn,get_create_query('A'))
    if(type=="B"):
        conn = create_connection(get_database_path())
        drop_table(conn,get_drop_query('B'))
        create_table(conn,get_create_query('B'))
                    

#print("INSERT INTO participation values("+str(0)+","+str(2222)+")");