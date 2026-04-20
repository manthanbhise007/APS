"""
After deployment if an error occurs there is difficulty of finding filename and the type of error
therefore we create a logs folder which holds the logger file in that logger we store the
month/date/year/hour/minutes/seconds , filename , type of error

This logger file is much usefull afte the deployment of the project in AWS
"""


import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
"""
datetime.now():This syntax is used to fetch present time
.strftime('%m_%d_%Y_%H_%M_%S'):converts in string format to give the name of the file
.log:this is the file holding the error filename and type of error 
    in the format of:'%m_%d_%Y_%H_%M_%S.log'
"""

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
"""
os.getcwd:spelled as "get current directory" which fetch the error from current file or directory
logs:it creates a folder named logs and inside it keeps LOG_FILE therefore we get a directory here

"""
os.makedirs(logs_path,exist_ok=True)
"""
this is to monitor wether if the directory is already created
    if created,it will not create again
"""
LOGS_FILE_PATH=os.path.join(logs_path,LOG_FILE)
"""
here we will get the final directory of logs
"""


logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
"""
loggin.basicConfig has three main features

filename:the folder which we created before is fetched here after error detection

format:the format which we want the error to be appear
    "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s":time,line number,name of error,level of logger
    ,and message which is coustomizable

level=logging.INFO:there are five levels ->(CRITICAL 50 points),(ERROR	40),(WARNING 30),(INFO 20),(DEBUG 10)
                                            ,(NOTSET 0)
here the highest level is CRITICAL and lowest is DEBUG ,NOTSET is not commonly used therefore we cannot consider as
level
after "." should be written in capital
"""