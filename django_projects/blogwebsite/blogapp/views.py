from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def custom_login_view(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               if user.is_superuser:
                   return redirect('admin:index')  # Redirect to admin panel
               else:
                   return redirect('dashboard')  # Redirect to dashboard
           else:
               # Handle invalid login
               return render(request, 'login.html', {'error': 'Invalid credentials'})
       return render(request, 'login.html')

@login_required
def dashboard(request):
       return render(request, 'dashboard.html')
   
