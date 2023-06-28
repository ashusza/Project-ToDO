from django.urls import path
from App_tasks import views
urlpatterns = [
    path('show/',views.Show_Task,name="show-task"),
    path('add/', views.Add_Task, name="add-task"),
]
