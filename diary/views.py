from django.shortcuts import render
from django.views import generic

# Create your views here.
# def index(request):
#     return render(request,'diary/index.html')

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"
class BaseView(generic.TemplateView):
    template_name = "diary/base.html"