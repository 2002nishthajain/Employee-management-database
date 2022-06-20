from ast import Delete
from django.shortcuts import render
from .models import Employees,Department,Project
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_emp = Employees.objects.all().count()
    num_dept =Department.objects.all().count()
    num_project =Project.objects.all().count()
    
    context = {
        'num_emp':  num_emp,
        'num_dept': num_dept,
        'num_project': num_project,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class EmployeesListView(generic.ListView) :
    model = Employees
    context_object_name = 'emp_list'
    template_name = 'emp_list.html'
    paginate_by = 5
    
class EmployeesDetailView(generic.DetailView) :
    model = Employees
    context_object_name = 'Employees_detail'
    template_name = 'Employees_detail.html'
    
class ProjectListView(generic.ListView) :
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'
    
class ProjectDetailView(generic.DetailView) :
    model = Project
    context_object_name = 'project_detail'
    template_name = 'project_detail.html'
    
class DepartmentListView(generic.ListView):
    model = Department
    context_object_name = 'dept_list'
    template_name = 'dept_list.html'
    
class DepartmentDetailView(generic.DetailView) :
    model = Department
    context_object_name = 'dept_detail'
    template_name = 'dept_detail.html'
    
class EmployeesCreate(CreateView) :
    model = Employees
    fields = '__all__'
    template_name = 'Employees_forms.html'
    
class EmployeesDelete(DeleteView) :
    model =Employees
    template_name = 'Emp_delete.html'
    success_url = reverse_lazy('Employees')
    