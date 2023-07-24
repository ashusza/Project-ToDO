from django.shortcuts import render,redirect
from App_tasks.models import Detail,Info
from App_tasks.forms import DetailForm,InfoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def delete_task(request, id):
    menu_obj = Info.objects.get(id=id)
    menu_obj.delete()
    return redirect('task-show')

@login_required(login_url='/login/')
def Show_Task(request):
    title_obj=Info.objects.all()
    context={"data":title_obj}
    return render(request,'task/show_task.html',context)

def List_Task(request):
    title_obj=Info.objects.all()
    context={"data":title_obj}
    return render(request,'task/list_task.html',context)


@login_required(login_url='/login/')
def Completed_Task(request):
    title_obj=Info.objects.all()
    context={"data":title_obj}
    return render(request,'task/completed_task.html',context)


@login_required(login_url='/login/')
def Add_Task(request):
    info_create_form = InfoForm()
    context = {"info_create_form": info_create_form, "title": "Add New Task"}

    if request.method == "POST":
            task_name = request.POST.get('task_name')
            task_deadline = request.POST.get('task_deadline')
            priority = request.POST.get('priority')
            task_obj = Detail.objects.get(id=request.POST.get('priority'))

            info_task=Info()
            info_task.task_name=task_name
            info_task.task_deadline=task_deadline
            info_task.priority=task_obj
            
            info_task.save()
            return redirect("task-show")
    return render(request, 'task/add_task.html', context)

    
@login_required(login_url='/login/')
def Edit_task(request, id):
    info_obj=Info.objects.get(id=id)
    detail_obj=Detail.objects.all()
    context ={"data": info_obj,"details":detail_obj}
    #to update data 
    if request.method =="POST":
        info_obj=InfoForm(data=request.POST,instance=info_obj)

        if info_obj.is_valid():
            info_obj.save()
            return redirect("task-edit",id)#redirection to url

    return render(request,'task/edit_task.html',context)
