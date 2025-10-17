from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.register, name='Register'),
    path('details',views.details,name='details'),
    path('edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('confirm-delete/<int:employee_id>/', views.confirm_delete, name='confirm_delete'),
]