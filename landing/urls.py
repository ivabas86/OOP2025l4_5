from django.urls import path

from landing.views import MyTempView

app_name = 'landing'

urlpatterns = [
    path('template', MyTempView.as_view(), name = 'template'),
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
]