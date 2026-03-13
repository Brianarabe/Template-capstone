from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import HomePageView,AboutPageView,ListingsPageView,View_propertyPageView,SearchPageView,ContactPageView,BasePageView,register_view, login_view,BrokerDashboardView, AgentDashboardView, BuyerDashboardView


urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('listings/', ListingsPageView.as_view(), name='listings'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('property/', View_propertyPageView.as_view(), name='property'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('broker_dashboard/', BrokerDashboardView.as_view(), name='broker_dashboard'),
    path('agent_dashboard/', AgentDashboardView.as_view(), name='agent_dashboard'),
    path('buyer_dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
]