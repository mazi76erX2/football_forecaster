from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'home_page.html'


@method_decorator(login_required, name='get')
class HomeLoggedInView(TemplateView):
    template_name = 'home_page_logged_in.html'
