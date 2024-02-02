from django.shortcuts import render, redirect
from admin_app.models import *
from django.contrib import messages

# Create your views here.

def home(request):
    current_page = 'home'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/home.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/about.html', context)

def products(request):
    current_page = 'products'
    products = Product.objects.all()
    context = {
        'current_page': current_page,
        'products': products,
    }
    return render(request, 'user_app/pages/products.html', context)

def projects(request):
    current_page = 'projects'
    projects = Project.objects.all()
    context = {
        'current_page': current_page,
        'projects': projects
    }
    return render(request, 'user_app/pages/projects.html', context)

def contact(request):
    current_page = 'contact'
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message') 

        try:
            message = Message(
                name=name,
                phone=phone,
                email=email,
                message=message,
            )
            message.save()
            messages.success(request, 'Message send successfully')
            return redirect('contact')  
        except Exception as e:
            messages.error(request, f'Error adding message: {e}')
            return redirect('contact')  
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/contact.html', context)

