from django.shortcuts import render,redirect
from App_tasks.models import Detail,Info
from App_tasks.forms import DetailForm,InfoForm
# Create your views here.
def Show_Task(request):
    title_obj=Info.objects.all()
    context={"data":title_obj}
    return render(request,'task/show_task.html',context)

def Add_Task(request):
    info_create_form=InfoForm()
    context={"info_create_form":info_create_form,"title":"Add New Task"}

    if request.method =="POST":
        task_name=request.POST.get('task_name')
        task_deadline=request.POST.get('task_deadline')
        task_priority=request.POST.get('task_priority')
        priority=Detail.objects.get(id=request.POST.get('task_priority'))
        
        # storing data with form class
        task_info=Info()
        task_info.task_name=task_name
        task_info.task_deadline=task_deadline
        task_info.task_priority=task_priority

        task_info.save()
        return redirect("show-task")   
    return render (request,'task/add_task.html',context) 
    
    
    