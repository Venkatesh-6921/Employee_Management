from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employee

def details(request):
    # Get all employee records from the database
    service = Employee.objects.all()
    
    # Create context dictionary with the data
    data = {
        'service': service
    }
    
    # Pass the data to the template
    return render(request, 'details.html', data)

def register(request):
    if request.method == "POST":
        details = Employee()
        details.Name = request.POST.get('a')
        details.Age = int(request.POST.get("b"))
        details.Job_role = request.POST.get("c")
        details.Salary = int(request.POST.get("d"))
        details.Date_Of_Joining = request.POST.get("e")
        details.Department = request.POST.get("f")
        details.save()
        return redirect('/details')
    
    # This part only executes for GET requests
    service = Employee.objects.all()
    data = {
        'service': service
    }
    
    return render(request, 'form.html', data)

def edit_employee(request, employee_id):
    # Get the employee object or return 404 if not found
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == "POST":
        # Update the employee record with form data
        employee.Name = request.POST.get('name')
        employee.Age = request.POST.get("age")
        employee.Job_role = request.POST.get("job_role")
        employee.Salary = request.POST.get("salary")
        employee.Date_Of_Joining = request.POST.get("date_of_joining")
        employee.Department = request.POST.get("department")
        employee.save()
        
        # Redirect to details page after successful update
        return redirect('details')
    
    # For GET requests, render the edit form with current employee data
    context = {
        'employee': employee
    }
    return render(request, 'edit_employee.html', context)

def confirm_delete(request, employee_id):
    # Get the employee object or return 404 if not found
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == "POST":
        # Delete the employee record
        employee.delete()
        return redirect('details')
    
    # For GET requests, show a confirmation page
    context = {
        'employee': employee
    }
    return render(request, 'confirm_delete.html', context)

