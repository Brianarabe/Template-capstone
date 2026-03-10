from django.urls import path
from .views import HomePageView,AboutPageView,ListingsPageView,LoginPageView,RegisterPageView,View_propertyPageView,SearchPageView,ContractPageView

urlpatterns = {
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', ListingsPageView.as_view(), name='listing'),
    path('', ContractPageView.as_view(), name='contact'),
    path('', LoginPageView.as_view(), name='login'),
    path('', View_propertyPageView.as_view(), name='view_property'),
    path('', RegisterPageView.as_view(), name='register'),
    path('', SearchPageView.as_view(), name='search'),
}