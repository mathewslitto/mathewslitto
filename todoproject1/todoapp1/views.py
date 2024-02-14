from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Tasks
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model=Tasks
    template_name = 'home.html'
    context_object_name = 'display'
class Taskdetailedview(DetailView):
    model = Tasks
    template_name = 'details.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')








def add(request):
    display=Tasks.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Tasks(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'display':display})


def delete(request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,idno):
    task=Tasks.objects.get(id=idno)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
