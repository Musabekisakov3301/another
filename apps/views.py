from django.shortcuts import render,redirect
from apps.models import Product,Category
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from apps.decorators import unauthenticated_user
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from apps.forms import CreateUserForm


def AppsListView(request):
    
    category = request.GET.get('category')

    if category == None:
       
        
            projects = Product.objects.order_by('created_at').filter(is_published=True)[0:1]
            firsts = Product.objects.order_by('created_at').filter(is_published=True)[1:2]
            seconds = Product.objects.order_by('created_at').filter(is_published=True)[2:3]
            thirds = Product.objects.order_by('created_at').filter(is_published=True)[3:4]
            fourths = Product.objects.order_by('created_at').filter(is_published=True)[4:7]
    else:
       
            projects = Product.objects.filter(category__name=category)[0:1]
            firsts = Product.objects.filter(category__name=category)[1:2]
            seconds = Product.objects.filter(category__name=category)[2:3]
            thirds = Product.objects.filter(category__name=category)[3:4]
            fourths = Product.objects.filter(category__name=category)[4:7]

    categories = Category.objects.all()

    
    context = { 
       'projects': projects,
       'firsts':  firsts,
       'categories': categories,
       'seconds':  seconds,
       'thirds': thirds,
       'fourths': fourths ,


    }
    return render(request,'apps/apps_list.html',context)





class AppsDetailView(DetailView):
    
      template_name = 'apps/apps_detail.html'
      queryset = Product.objects.all()
      context_object_name = 'project'


class FirstAppsDetailView(DetailView):
    
      template_name = 'apps/apps_detail.html'
      queryset = Product.objects.all()
      context_object_name = 'first'
 

class SecondAppsDetailView(DetailView):
    
      template_name = 'apps/apps_detail.html'
      queryset = Product.objects.all()
      context_object_name = 'second'

class ThirdAppsDetailView(DetailView):
    
      template_name = 'apps/apps_detail.html'
      queryset = Product.objects.all()
      context_object_name = 'third'

class FourthAppsDetailView(DetailView):
    
      template_name = 'apps/apps_detail.html'
      queryset = Product.objects.all()
      context_object_name = 'fourth'

@unauthenticated_user
def registerPage(request):

        form = CreateUserForm()
        if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
           
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

        context = {
            'form': form
        }
        return render(request,'apps/register.html',context)

@unauthenticated_user
def loginPage(request):

        if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(request, username=username, password=password)

          if user is not None:
              login(request, user)
              return redirect('apps_list')
          else:
              messages.info(request, 'Username OR password is incorrect')


        context = {

        }
        return render(request, 'apps/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('landing_page')


def LandingPage(request):
    context = { }

    return render(request, 'apps/landing_page.html',context)

def OurTeamPage(request):
    return render(request,'apps/team.html')

def TechnologyPage(request):
    return render(request,'apps/technology.html')

def CoursePage(request):
    return render(request,'apps/course.html')