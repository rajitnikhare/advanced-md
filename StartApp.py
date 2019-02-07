'''
@copyright: Personal
@author: Rajit Nikhare
@date: 12-Jan-2019



'''
from DataFromGithub import githubToJasonJob
from FindSolution import findDayOfMaximumCommit,findTheWeekWithMaxCommit
from JsonToSqlLite import jsonToSQLJob
from DataBackupToS3 import dataBackupToS3


print(">>>>>>>>>>Initiating Pipeline>>>>>>>>>>")
try:
    
    githubToJasonJob()
    findDayOfMaximumCommit()
    findTheWeekWithMaxCommit()
    jsonToSQLJob()
    dataBackupToS3()
    
except Exception as err:
    print("Error occurred in GitHubDataPipeLineJob",str(err))
print("<<<<<<<<<<Terminiating Pipeline<<<<<<<<<<")

