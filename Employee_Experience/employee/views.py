from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Check if email already exists in User model
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('register')

        # Create a new User instance
        user = User.objects.create(
            username=email, 
            email=email,
            password=make_password(password), 
        )

        
        employee = Employee.objects.create(
            user=user, 
            name=name,
            phone=phone,
        )

        messages.info(request, 'Registration completed!')
        return redirect('loginUser')

    return render(request, 'register.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

      
        user = authenticate(username=email, password=password)
        if user is not None:
            # User found, login successful
            login(request, user)
            return redirect('homePage')
        else:
            # User not found or incorrect password, login failed
            messages.error(request, 'Invalid email or password')
            return redirect('loginUser')

    return render(request, 'loginUser.html')

@login_required
def homePage(request):
    employee = request.user.employee
    experiences = Experience.objects.filter(employee_id=employee)

    if request.method == "POST":
        
        for key, value in request.POST.items():
            if key.startswith('company_name_'):
                sl_no = key.split('_')[-1]
                experience = Experience.objects.create(
                    employee_id=employee,
                    company_name=value,
                    role=request.POST.get(f'role_{sl_no}'),
                    date_of_joining=request.POST.get(f'date_of_joining_{sl_no}'),
                    last_date=request.POST.get(f'last_date_{sl_no}')
                )
                experience.save()

        
        return redirect('homePage')
    
    context = {
        'experiences': experiences,
    }   
    return render(request, 'homePage.html', context)
   
def delete_experience(request,id):
   queryset=Experience.objects.get(id=id)
   queryset.delete()
   return redirect('homePage')

