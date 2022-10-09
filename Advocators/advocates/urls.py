from django.urls import path
from .views import AdvocateDetail , AdvocateList


urlpatterns = [
    path('advocates/' , AdvocateList.as_view(), name = "advocates"),
    path('advocates/<int:pk>/', AdvocateDetail.as_view(), name="advocates"),
]
