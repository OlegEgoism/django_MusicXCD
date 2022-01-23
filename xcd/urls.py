from django.urls import path
from xcd.views import *
from .import views

urlpatterns = [
    path('', views.HomeSamples.as_view(), name='home'),
    path('author/<slug:slug>/', views.HomeAuthor.as_view(), name='author'),
    path('style/<slug:slug>/', views.HomeStyle.as_view(), name='style'),
    path('descriptions/<int:pk>/', views.Descriptions.as_view(), name='descriptions'),

    path('add_author/', add_author, name='add_author'),
    path('add_samples/', add_samples, name='add_samples'),
    path('published/', add_published_samples, name='published'),

    path('register/', get_register, name='register'),
    path("search/", search_all, name='search'),


    # path('', home, name='home'),
    # path('author/<slug:slug>/', get_author, name='author'),
    # path('style/<slug:slug>/', get_style, name='style'),
    # path('info/<int:pk>', get_info, name='descriptions'),

    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user, name='logout'),
    # path('register/', RegisterUser.as_view(), name='register'),

]

