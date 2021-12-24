from django.urls import path
from xcd.views import *

urlpatterns = [
    path('', home),
    path('style/<int:id>/', get_style, name='style'),

]



