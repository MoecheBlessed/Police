from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pcapp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.CrimeListView.as_view(), name='index'),
    path('<int:pk>', views.CaseDetailView.as_view(), name='detail'),
    path('inputcase/', views.CaseCreateView.as_view(), name='inputcase'),
    path('<int:pk>/updatecrime/', views.CrimeUpdateView.as_view(), name='update'),
    path('criminals/', views.criminals, name='criminals'),
    path('staffs/', views.staff, name='staffs'),
    path('<int:pk>/updatecriminal/', views.CriminalUpdateView.as_view(), name='updatecriminal'),
    path('<int:pk>/updatestaff/', views.StaffUpdateView.as_view(), name='updatestaff'),
    path('<int:pk>/addcriminal/', views.CriminalCreateView.as_view(), name='addcriminal'),
    #path('logout/', views.logout_user, name='logout_user'),
    path('crimes/', views.CrimeCreateView.as_view(), name='crimes'),
    path('crimelist/', views.CrimeListView.as_view(), name='crimelist'),
    path('recordlist/', views.RecordListView.as_view(), name='recordlist'),
    path('<int:pk>/updaterecord/', views.RecordUpdateView.as_view(), name='updaterecord'),


]
