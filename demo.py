import logging
from Housing.pipeline.pipeline import pipeline
from Housing.exception import HousingException
from Housing.config.configuration import Configuration
from Housing.component.data_validation import DataValidation
def main():
    try:
        pipline=pipeline()
        pipline.run_pipeline()
        # data_val=Configuration().get_data_validation_config()
        # print(data_val)

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == ("__main__"):
    main()


 


