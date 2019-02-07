import boto3
import botocore
from config import config
import datetime

BUCKET = config.AWS_CONFIG.get('bucket')   
print(BUCKET)
#KEY = config.AWS_CONFIG.get('key')
#print(KEY)
now = datetime.datetime.now()
filerecognizer = str(now.year) +'_'+ str(now.month) +'_'+ str(now.day)
s3 = boto3.resource('s3')

#upload
def dataBackupToS3():
    print(">>>>>>Initializing Data Backup>>>>>>>>>")
    try:
        data = open('DayVsCommit.png', 'rb')
        data2 = open('participation.json', 'rb')
        data3 = open('punch_card.json', 'rb')
        data4 = open('pythonsqlite.db', 'rb')
        s3.Bucket(BUCKET).put_object(Key='datasource-s3-b1/'+filerecognizer+'/DayVsCommit.png', Body=data)
        s3.Bucket(BUCKET).put_object(Key='datasource-s3-b1/'+filerecognizer+'/participation.json', Body=data2)
        s3.Bucket(BUCKET).put_object(Key='datasource-s3-b1/'+filerecognizer+'/punch_card.json', Body=data3)
        s3.Bucket(BUCKET).put_object(Key='datasource-s3-b1/'+filerecognizer+'/pythonsqlite.db', Body=data4)
    
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
     
    print("<<<<<<<<<<Data Backup Complete<<<<<<<<<<<")
#data = open('DayVsCommit.png', 'rb')
#s3.Bucket(BUCKET_NAME).put_object(Key='datasource-s3-b1/test.png', Body=data)

#def download_file_from_s3():
#    #download
#    try:
#        s3.Bucket(BUCKET).download_file(KEY, 'punch_card_from_s3.json')
#    except botocore.exceptions.ClientError as e:
#        if e.response['Error']['Code'] == "404":
#            print("The object does not exist.")
#        else:
#            raise