from django.urls import path
from .views import HomePageView,AboutPageView,ListingsPageView,LoginPageView,RegisterPageView,View_propertyPageView,SearchPageView,ContractPageView,BasePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('listings/', ListingsPageView.as_view(), name='listings'),
    path('contact/', ContractPageView.as_view(), name='contact'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('property/', View_propertyPageView.as_view(), name='property'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('search/', SearchPageView.as_view(), name='search'),
]