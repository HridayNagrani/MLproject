import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #Info about error like file and line number will be in exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messsage="Error occured in python Script name [{0}] line number [{1}] error message[{2}]".format(
      file_name,exc_tb.tb_lineno,str(e)  
    )

