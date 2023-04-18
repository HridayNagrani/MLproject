import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngentionConfig:
    train_data_path: str=os.path.join('artifact','train.csv')
    test_data_path: str=os.path.join('artifact','test.csv')
    raw_data_path: str=os.path.join('artifact','raw.csv')

class DataIngention:
    def __init__(self) :
        self.ingestion_config=DataIngentionConfig()

    def initiate_data_ingestion(self):
        # Code for read from databse
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path)
        except:
            pass
