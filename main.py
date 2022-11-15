from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
if __name__=='__main__':
     try:
          train_pipeline=TrainPipeline()
          train_pipeline.run_pipeline()
     except Exception as e: 
          logging.exception(e)
