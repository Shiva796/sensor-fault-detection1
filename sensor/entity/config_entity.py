from datetime import datetime
from dataclasses import dataclass
import os
from sensor.constant import training_pipeline
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
@dataclass
class TrainingPipelineConfig:
    pipeline_name: str =training_pipeline.PIPELINE_NAME

    artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, TIMESTAMP)

    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


class DataIngestionConfig:
  def __init__(self,training_pipeline_config:TrainingPipelineConfig):
       
    self.data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
    )

    self.feature_store_file_path: str = os.path.join(
        self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
    )

    self.training_file_path: str = os.path.join(
       self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
    )

    self.testing_file_path: str = os.path.join(
        self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
    )

    self.train_test_split_ratio: float =training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION

    self.collection_name: str =training_pipeline.DATA_INGESTION_COLLECTION_NAME
