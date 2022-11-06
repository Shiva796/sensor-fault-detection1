from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact
class TrainPipeline:

    def __init__(self):
        training_pipelibe_config=TrainingPipelineConfig()
        self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipelibe_config)
        self.training_pipelibe_config=training_pipelibe_config

    def start_data_ingestion(self)->DataIngestionArtifact:

        try:
         logging.info("Starting data ingestion")
         logging.info("end data ingestion")
        except Exception as e:
            raise  SensorException(e,sys) 
    def start_data_validation(self):

        try:
            pass
        except Exception as e:
            raise  SensorException(e,sys) 
    def start_data_transformation(self):

        try:
            pass
        except Exception as e:
            raise  SensorException(e,sys) 
    def start_model_trainer(self):

        try:
            pass
        except Exception as e:
            raise  SensorException(e,sys) 
    def start_data_evaluation(self):

        try:
            pass
        except Exception as e:
            raise  SensorException(e,sys) 
    def start_data_pusher(self):

        try:
            pass
        except Exception as e:
            raise  SensorException(e,sys)                                           
    def run_pipleline(self):

        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise  SensorException(e,sys)         