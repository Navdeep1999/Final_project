#from django.conf.urls import url
from django.urls import path, include
from .views import (
    APLListApiView,
     
)

urlpatterns = [
    path('api', APLListApiView.as_view()),
    #path('api/<int:APL_id>', APLListApiView.as_view())
]