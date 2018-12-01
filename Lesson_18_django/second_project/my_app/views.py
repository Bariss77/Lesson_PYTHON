from django.shortcuts import render

from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages

from my_app.forms import MyForm

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'my_app/index.html')

class MyView(View):
    def get (self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'my_app/form.html', c)

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'validation failed')
        c = {'form': form}
        return render(request, 'my_app/form.html', c)
