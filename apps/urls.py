from django.urls import path
from apps.views import AppsListView,FirstAppsDetailView,AppsDetailView,FourthAppsDetailView,registerPage,loginPage,logoutUser,LandingPage


urlpatterns = [

    path('',AppsListView,name='apps_list'),
    path('',LandingPage, name='landing_page'),
    path('<int:pk>/',AppsDetailView.as_view(),name='apps_detail'),  
    path('<int:pk>/',FirstAppsDetailView.as_view(),name='firstapps_detail'), 
    path('<int:pk>/',FourthAppsDetailView.as_view(),name='fourthapps_detail'), 
    path('register/',registerPage,name='register'),
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('landing_page/',LandingPage, name='landing_page' ),
]
