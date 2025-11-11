import logging#any execution that is happening is log that into the text file for exasily navigation the exception
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)#even we have files just keep on appending the logs 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(#this is the basic template whenever we want to the logging.info and this the format that we will bw getting 
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__=="__main__":
    logging.info("logging has started")