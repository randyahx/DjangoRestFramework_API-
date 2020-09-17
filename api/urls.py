"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'messages', views.MessagesViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Using Router + ViewSets removes the need to state a url for different methods(GET/UPDATE/DELETE)
    # path('messages/', views.MessagesListCreate.as_view()),
    # path('messages/<int:pk>/', views.MessagesUpdateDelete.as_view()),
    # path('users/', views.UserListCreate.as_view()),
    # path('users/<int:pk>/', views.UserUpdateDelete.as_view()),
]

"""as_view() needed when converting function based views to class based views"""


