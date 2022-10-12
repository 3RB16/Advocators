from django.urls import path
from .views import AdvocateDetail , AdvocateList


urlpatterns = [
    path('' , AdvocateList.as_view(), name = "advocates"),
    path('<int:pk>', AdvocateDetail.as_view(), name="advocates"),
]
