from django.urls import path
from .views import *

urlpatterns = [
    path('', ListDetails.as_view()),

]
