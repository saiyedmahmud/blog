from user.models import User
from user.forms.user import Userform

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,HttpResponse


# Create your views here.
def profile(request):
    if request.method == 'POST':
        form = Userform(request.POST or None)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Userform()
    table = User.objects.all()
    context = {
        'form':form,
        'table':table
    }
    return render(request, 'user/profile.html', context=context)
