from Housing.config.configuration import Configuration
from Housing.logger import logging
from Housing.exception import HousingException
from Housing.component.data_ingestion import DataIngestion

from Housing.entity.artifact_entity import DataIngestionArtifact
from Housing.entity.config_entity import DataIngestionConfig

import os,sys

class pipeline:

    def __init__(self,config:Configuration=Configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e

    
    def run_pipeline(self):
        try:
            data_ingestion_artifcat=self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
