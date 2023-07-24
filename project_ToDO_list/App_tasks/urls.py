from django.urls import path
from App_tasks import views
urlpatterns = [
    path('show/',views.Show_Task,name="task-show"),
    path('list/',views.List_Task,name="task-list"),
    path('add/', views.Add_Task, name="task-add"),
    path('complete/', views.Completed_Task, name="task-completed"),
    path('edit/<int:id>/',views.Edit_task,name='task-edit'),
    path('delete/<int:id>/',views.delete_task,name="task-delete")
    
]
