from django.urls import path

from measurement.views import SensorsView, MeasurementView, SensorsDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorsDetailView.as_view()),
]
