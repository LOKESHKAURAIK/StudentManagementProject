from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index),
    path('sign-up.html', views.sign_up),
    path('sigin', views.sign_in),
    path('addstudent', views.addstudent),
    path('courses', views.courses),
    path('addcourse', views.addcourses),
    path('update_view/<int:uid>/',views.update_view, name='Updatecourse'),
    path('update_course/', views.update_course),
    url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path('addteacher', views.addteacher),
    path('dashboard', views.dashboard),

    
    


    
    path('hostel', views.hostel),
    path('notification', views.notification),
    path('pg', views.pg),
    path('profiletable', views.profiletable),
    path('table', views.table),
    path('tenants', views.tenants),

]
