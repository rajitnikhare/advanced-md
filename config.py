'''
Created on Jun 18, 2018

@author: Rajit Nikhare
'''

#bucket_name = AWS_ACCESS_KEY_ID.lower() + 'adapt-s3'
class config(object):
     
    FOLDERS = {
    'SOURCE':'ftpDump/',
    'READY':'/advanced-md/com/amd',
    'ERROR':'ftpDump/error',
    'COMPLETED':'ftpDump/complete',
    'ARCHIVE':'ftpArchive/'
    }
    
    AWS_CONFIG = {
        'ACCESS_KEY_ID':'',
        'SECRET_ACCESS_KEY':'',
        'host':'',
        'bucket': '',
        'key':'datasource-s3-b/punch_card.json'
    }


    DATA = {
    'ftp_staging':'/AA_FTP/FTP_STAGING',
    'source':'//incoming/aa_test/',
    'target':'datasource-s3-b'
    
    }
    ##Below ones are for reference
    DATA_TEST = {
    'ftp_staging':'/AA_FTP/FTP_STAGING',
    'source':'//incoming/aa_test/',
    'target':'njd/Input/sport_logiq/playsequence/_new_g1_test'
    }
    
    DATA_PROD = {
    'ftp_staging':'/AA_FTP/FTP_STAGING',
    'source':'/incoming/20172018',
    'target':'njd/Input/sport_logiq/playsequence/_new_g1_test/'
    }
    
    
    
   
    

