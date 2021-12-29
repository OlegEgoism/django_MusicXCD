from django.urls import path
from xcd.views import *

urlpatterns = [
    path('', home, name='home'),

    path('style/<str:name>/', get_style, name='style'),
    path('author/<str:name>/', get_author, name='author'),
    path('info/<int:pk>', get_info, name='descriptions'),
]



