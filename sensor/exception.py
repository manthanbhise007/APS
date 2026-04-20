"""
This folder we are creating to create our own spetialized error handling folder
    here the main aim is to get filename where that error is present then the line number where the error is present
    and the type of error or the error message
"""





import sys 
import os

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    """
    here error_details.exe_info() fetch the error from the system and gives three tupels
    first two are not important but the third is stored in exc_tb which contains
    filename,line number,type of error

    """
    filename=exc_tb.tb_frame.f_code.co_filename
    """
    we are storing the filename in a variable
    The "." here is to get directory inside directory 
    """
    error_message="error occured and the file name is [{0}] and the line number is [{1}] and error is [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message


class SensorException(Exception): #this is the first main step
    def __init__(self,error_message,error_details:sys): #we have to first initilize the error message
        """
        error_message:This is a variable we have created to store the error message from the system
        error_details:This stores the error information from the system

        """
        super().__init__(error_message)
        """
        super() used inside __init__() to ensure parent class attributes are correctly initialized without re-writing the code.
        """
        self.error_message=error_message_detail(error_message,error_details=error_details)
        """
        we have created a function to fetch the error message from the system
        """
    def __str__(self):
        return self.error_message
        """
        this returns error_message in a string format
        """