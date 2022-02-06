import debug_toolbar
from django.urls import path, include
from xcd.views import *
from .import views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('captcha/', include('captcha.urls')),

    path('', views.HomeSamples.as_view(), name='home'),
    path('author/<slug:slug>/', views.HomeAuthor.as_view(), name='author'),
    path('style/<slug:slug>/', views.HomeStyle.as_view(), name='style'),
    path('descriptions/<int:pk>/', views.Descriptions.as_view(), name='descriptions'),

    path('add_author/', add_author, name='add_author'),
    path('add_samples/', add_samples, name='add_samples'),
    path('published/', add_published_samples, name='published'),

    path('register/', get_register, name='register'),
    path('login/', get_login, name='login'),
    path('logout/', get_logout, name='logout'),
    path('email/', get_email, name='email'),

    path('search/', search_all, name='search'),

    # path('views/', views, name=views),


    # path('', home, name='home'),
    # path('author/<slug:slug>/', get_author, name='author'),
    # path('style/<slug:slug>/', get_style, name='style'),
    # path('info/<int:pk>', get_info, name='descriptions'),

]
