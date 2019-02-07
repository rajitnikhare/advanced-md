# Advanced-MD
## This is a challenge project to perform ETL operation on various data points.

The task is to gather json data from the github API (pandas repository) and perform transformation and load the data to an SQLite file. 

1. StartApp.py is the Data pipeline initiator which starts the collection of data from the Github API

2. FindSolution.py is where the transformation of the data takes place. It gives the required solution of how many commits were made in the last 52 weeks for the pandas repository. Also, states how many of those were from the owner/creator. The day of maximum commit is also stated as output.

3. JsonToSQLlite.py takes all the data and saves it to a sqlite file

4. DataBackuptoS3.py makes a backup to an S3 bucket on AWS

