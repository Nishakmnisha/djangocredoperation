from django.shortcuts import render,redirect
from django.views import View
from employeeapp.models import Employee
# Create your views here.
class Home(View):
    def get(self,request):
        return render (request,'index.html')
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name=request.POST.get("name")
        salary=request.POST.get("salary")
        designation=request.POST.get("designation")
        email=request.POST.get("email")
        Employee.objects.create(name=name,salary=salary,designation=designation,email=email)
        return redirect('home')
class EmployeeList(View):
    def get(self,request):
        emp=Employee.objects.all()
        return render (request,'emp_list.html',{'data':emp})
class DeleteEmployee(View):
    def get(self,request,*args,**kwargs):  #kwargs={id:3}
        id=kwargs.get('id')  # to get the id we want to delete
        emp=Employee.objects.get(id=id)  # to get the datas corresponding to that id from the database
        emp.delete()  #@ to delete the data
        return redirect('employeelist')  # to redirect into the previous page
class UpdateEmployee(View):
    def get(self,request,*args,**kwargs):  #kwargs={id:3}
        id=kwargs.get('id')  # to get the id we want to delete
        emp=Employee.objects.get(id=id)  # to get the datas corresponding to that id from the database
        return render(request,'edit.html',{"data":emp})

    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        employee=Employee.objects.get(id=id)
        name=request.POST.get('name')
        salary=request.POST.get('salary')
        designation=request.POST.get('designation')
        email=request.POST.get('email')
        employee.name=name
        employee.salary=salary
        employee.designation=designation
        employee.email=email
        employee.save()
        return redirect('employeelist')


