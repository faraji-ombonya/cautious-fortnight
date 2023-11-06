import pandas as pd
from joblib import load
from django.conf import settings


class HeartDiseaseLogisticRegressionCLassifier():

    def __init__(self) -> None:
        self.clf = load(
            f"{settings.BASE_DIR}/estimators/{settings.MODEL_NAME}")

    def predict(self, X_dict):
        """
        Use Use a heart disiease logistic regression model classifier to predict heart disease.

        X_dict: A dictionary of parameters
        """
        X = pd.DataFrame(X_dict, index=[0])
        y_pred = self.clf.predict(X)
        result = {"has_heart_disease": y_pred[0]}
        return result
