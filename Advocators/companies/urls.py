from django.urls import path
from .views import CompanyList , CompanyDetail


urlpatterns = [
    path('' , CompanyList.as_view(), name = "companies"),
    path('<int:pk>', CompanyDetail.as_view(), name="companies"),
]
