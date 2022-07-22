import logging
from Housing.pipeline.pipeline import Pipeline
from Housing.exception import HousingException
from Housing.config.configuration import Configuration
from Housing.component.data_validation import DataValidation
import dill
import os,sys

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        pipeline.start()
        # data_val=Configuration().get_data_validation_config()
        # print(data_val)
        # data_val=Configuration().get_data_transformation_config()
        # print(data_val)
        # model_train=Configuration().get_model_trainer_config()
        # print(model_train)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == ("__main__"):
     main()


 


