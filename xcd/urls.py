from django.urls import path
from xcd.views import *

urlpatterns = [
    path('', home, name='home'),
    path('style/<int:name>/', get_style, name='style'),

]



