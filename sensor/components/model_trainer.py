from sensor.utils.main_utils import load_numpy_array_data
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from sensor.entity.config_entity import ModelTrainerConfig
import os,sys
from xgboost import XGBClassifier
from sensor.ml.metric.classsification_metric import get_classification_score
from sensor.ml.model import SensorModel
from sensor.utils.main_utils import save_object,load_object
class ModelTrainer
def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
    try:
        self.model_trainer_config=model_trainer_config
        self.data_transformation_artifact=data_transformation_artifact
    except Exception as e:
       raise SensorException(e,sys)  

def trained_model(self,x_train,y_train): 
    try:
        xgb_clf=XGBClassifier()
        xgb_clf.fit(x_train,y_train)
         return xgb_clf
    except Exception as e:
        raise e  

def initiate_model_trainer(self)->ModelTrainerArtifact:
    try:
       train_file_path=self.data_transformation_artifact.transformed_object_file_path
       test_file_path=self.data_transformation_artifact.transformed_object_file_path

       #loading training array and testing arr 
       train_arr=load_numpy_array_data(train_file_path)
       test_arr=load_numpy_array_data(test_file_path)
        x_train,y_train,x_test,y_test=(
         train_arr[:,:-1],
         train_arr[:,-1],
         test_arr[:,:-1],
         test_arr[:,-1]) 
        model=self.trained_model(x_train,y_train)
        y_train_pred=model.predict(x_train)
        classsification_train_metric=get_classification_score(y_true=y_train,y_pred=y_train_pred)

        if classsification_train_metric.f1_score<self.model_trainer_config.expected_accuracy:
            raise Exception("Trained model is not good to provide excepcted accurancy")

        y_test_pred=model.predict(x_test)

        classsification_test_metric=get_classification_score(y_true=x_test,y_pred=y_test_pred)
        # overfitting and underfitting #

        diff=abs(classsification_train_metric.f1_score.classsification_test_metric.f1_score)

        if diff>self.model_trainer_config.overfitting_underfitting_threshold:
            raise Exception("Model is not good raise the Raise Exception")
        preprocessor=load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
        
        model_dir_path=os.path.dirname(self.model_trainer_config.trained_file_path)
        os.makedirs(model_dir_path,exist_ok=True)
        sensor_model=SensorModel(preprocessor=preprocessor,model=model)
        save_object(self.model_trainer_config.trained_file_path,obj=sensor_model)
        # model trainer artifict #   
        model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,train_metric_artifact=classsification_train_metric,test_metric_artifact=classsification_test_metric)
        logging.info(f"Model trained artifact:{model_trainer_artifact}")
        return model_trainer_artifact   
    except Exception as e:
        raise SensorException(e,sys)  

