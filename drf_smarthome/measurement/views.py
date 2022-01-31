# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorDetailSerializer, SensorsSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor(name=request.data['name'], description=request.data['description']).save()
        return Response({'status': 'create'})


class SensorsDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(APIView):
    def post(self, request):
        q_set = Sensor.objects.filter(id=request.data['sensor'])
        Measurement(temperature=request.data['temperature'], sensor=q_set[0]).save()
        return Response({'status': 'create'})


