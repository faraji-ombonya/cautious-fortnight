from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fortnight.serializers import PredictSerializer
from fortnight.utils.logistic_regression_classifier import HeartDiseaseLogisticRegressionCLassifier

model = HeartDiseaseLogisticRegressionCLassifier()


@api_view(['POST'])
def predict(request):
    """
    Make a prediction
    """
    if request.method == 'POST':
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():

            X_dict = serializer.save()
            prediction = model.predict(X_dict)

            return Response(prediction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
