from django.urls import path
from xcd.views import *

urlpatterns = [
    path('', home, name='home'),
    path('style/<int:name>/', get_style, name='style'),
    path('author/<int:name>/', get_author, name='author'),
    # path('info/<int:name>/', get_info, name='info'),
    path('info/', get_info, name='info'),
]



