from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import todoform
from todoapp.models import mod

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


class lview(ListView):
    model = mod
    template_name = 'details.html'
    context_object_name = 'info'

class dview(DetailView):
    model = mod
    template_name = 'home.html'
    context_object_name = 'info'

class uview(UpdateView):
    model =mod
    template_name = 'update.html'
    context_object_name = 'info'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('dview',kwargs={'pk':self.object.id})

class delview(DeleteView):
    model = mod
    template_name = 'delete.html'
    success_url = reverse_lazy('lview')



def home(request):
    info = mod.objects.all()
    if request.method == 'POST':
        item = request.POST.get('item','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = mod(item =item,priority=priority,date=date)

        task.save()
    return render(request,'home.html',{'info':info})

def delete(request,taskid):
    d = mod.objects.get(id=taskid)
    if request.method == 'POST':
        d.delete()
        return redirect('/')

    return render(request,'delete.html')


# def details(request):
#     info = mod.objects.all()
#     return render(request,'details.html',{'info':info})
#

def update(request,id):
    u = mod.objects.get(id=id)
    f = todoform(request.POST or None, instance=u)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'u':u})
