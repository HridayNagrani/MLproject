import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exec_info() #Info about error like file and line n
