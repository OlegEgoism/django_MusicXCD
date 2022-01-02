from django.urls import path
from xcd.views import *

urlpatterns = [
    path('', home, name='home'),

    path('style/<int:pk>/', get_style, name='style'),
    path('author/<int:pk>/', get_author, name='author'),
    path('info/<int:pk>', get_info, name='descriptions'),
]



