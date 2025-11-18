#WWe are split the data into treain and test split
import os #this is used because we are using the custom exception 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#now the whenever we are performing the data ingestion component then there is always are input where and we have to save the input somewhere and we will save that into data ingestion config class

@dataclass#decorator:to define your class variable we use init but from this we can directly define the class variable 
class DataIngestionConfig:#Any input required i will write that into dataIngestion config 
    #this is the input we are giving to the component and now it knows that where to save the test ,train,raw file path 
    
    train_data_path: str=os.path.join('artifacts',"train.csv")#there is the artifacts where it will output the files 
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")


#if we have to just define the variables then we can do that by dataclass but if we have some other functions as well then we have to use init
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#when we call this class , then the three variable will get stored in this class

    def initiate_data_ingestion(self):#write the code to read in the database 
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('/Users/I578409/Documents/MLproject_naik/notebook/data/stud.csv')
            logging.info("Exported or read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiator")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")


            return (#it is returning to this to the next step that is data transformation
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()