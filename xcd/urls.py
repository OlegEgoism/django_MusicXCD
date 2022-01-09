from django.urls import path
from xcd.views import *
from .import views

urlpatterns = [
    path('', home, name='home'),

    path("search/", search, name='search'),

    path('style/<int:pk>/', get_style, name='style'),
    path('author/<int:pk>/', get_author, name='author'),
    path('info/<int:pk>', get_info, name='descriptions'),

    path('add_author/', add_author, name='add_author'),
    path('add_samples/', add_samples, name='add_samples'),
    path('published/', add_published, name='published'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),


]



