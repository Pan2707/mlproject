import sys


#function showing how ur message will look like inside ur file w.r.t custom exception
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb-=error_detail.exc_info()  #this gives information about on whcih file or line the exception has occurred
    file_name = exc_tb.tb_frame.f_code.co_file_name
    error_message="Error occurred in python script name[{}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error) # this is for error message details
   
    return error_message
    )

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message) # inherit the init function from  Exception
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message # if i try to print it, it will get all the error messages over here


