import sys #Any exception that is been occured the sys library has that information

def error_message_detail(error,error_detail:sys):#this is the function that tells me how my message should look int our file 
    _,_,exc_tb=error_detail.exc_info()#the exc_tb has all the information related to the errors occured 
    file_name=exc_tb.tb_frame.f_code.co_filename# custom exception for the python 
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))#to  get the line number along with the error message details 

    return error_message
        

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)