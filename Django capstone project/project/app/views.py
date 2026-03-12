from django.shortcuts import render
from django.views.generic import TemplateView

class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContractPageView(TemplateView):
    template_name = 'contract.html'

class ListingsPageView(TemplateView):
    template_name = 'listings.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class SearchPageView(TemplateView):
    template_name = 'search.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class View_propertyPageView(TemplateView):
    template_name = 'view_property.html'