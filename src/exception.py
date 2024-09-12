import sys      #The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment.

def error_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()         #returns three values,First two value not important. it returns which file and which line having Exception
    file_name=exc_tb.tb_frame.f_code.co_filename
    Line_no=exc_tb.tb_lineno
    error_message="Error Occured in Python-script name [{0}] Line number [{0}] error message[{2}]".format(file_name,Line_no,str(error))
    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    