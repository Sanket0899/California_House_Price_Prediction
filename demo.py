import logging
from tkinter.tix import MAIN
from Housing.pipeline.pipeline import pipeline
from Housing.exception import HousingException
def main():
    try:
        pipline=pipeline()
        pipline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == ("__main__"):
    main()


 


