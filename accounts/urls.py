from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views

urlpatterns = [
    path('profile/', views.profile),
]
urlpatterns = format_suffix_patterns(urlpatterns)