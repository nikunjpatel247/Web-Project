from django.urls import path
from.import views
urlpatterns = [
    path('', views.hi, name='home-page'),
    path('portfolio-details.html', views.portfolio, name='portfolio-page'),
]
