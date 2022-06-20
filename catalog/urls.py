from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/',views.EmployeesListView.as_view(),name ='Employees'),
    path('employees/<int:pk>',views.EmployeesDetailView.as_view(),name = 'Employees_detail'),
    path('projects/',views.ProjectListView.as_view(),name ='Projects'),
    path('project/<int:pk>',views.ProjectDetailView.as_view(),name = 'project_detail'),
    path('departments/',views.DepartmentListView.as_view(),name ='Departments'),
    path('department/<int:pk>',views.DepartmentDetailView.as_view(),name = 'Department_detail'),
    path('employees/create/', views.EmployeesCreate.as_view(), name='Employees_create'),
    path('employees/<int:pk>/delete/', views.EmployeesDelete.as_view(), name='Employees_delete'),
    ]