from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContractPageView(TemplateView):
    template_name = 'app/contract.html'

class ListingsPageView(TemplateView):
    template_name = 'app/listings.html'

class RegisterPageView(TemplateView):
    template_name = 'app/register.html'

class SearchPageView(TemplateView):
    template_name = 'app/search.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class View_propertyPageView(TemplateView):
    template_name = 'app/view_property.html'