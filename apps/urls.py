from django.urls import path
from apps.views import AppsListView,FirstAppsDetailView,AppsDetailView,FourthAppsDetailView,OurTeamPage, Page_404,registerPage,loginPage,logoutUser,LandingPage,OurTeamPage,TechnologyPage,CoursePage,Page_404


urlpatterns = [

    path('apps_list/',AppsListView,name='apps_list'),
    path('',LandingPage, name='landing_page' ),
    path('<int:pk>/',AppsDetailView.as_view(),name='apps_detail'),  
    path('<int:pk>/',FirstAppsDetailView.as_view(),name='firstapps_detail'), 
    path('<int:pk>/',FourthAppsDetailView.as_view(),name='fourthapps_detail'), 
    path('register/',registerPage,name='register'),
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('team/',OurTeamPage, name='team'),
    path('technology/',TechnologyPage, name='technology'),
    path('course/',CoursePage, name='course'),
    path('page_404/',Page_404, name='page_404'),
   
]
