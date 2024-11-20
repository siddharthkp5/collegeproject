from django.contrib import admin
from django.urls import path,include
from cmsapp import views

urlpatterns = [
    
    path('index',views.index,name='index'),  
    path('',views.mainhome,name='mainhome'),  

    path('adminhome',views.adminhome,name='adminhome'),  
    path('studenthome',views.studenthome,name='studenthome'),  
    path('teacherhome',views.teacherhome,name='teacherhome'),  
    path('logins',views.logins,name='logins'),  
    path('lgout',views.lgout,name='lgout'),  

    path('deletest/<int:sid>',views.deletest,name='deletest'),
    path('deletete/<int:tid>',views.deletete,name='deletete'),

    path('dep_add',views.dep_add,name='dep_add'),  
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('approved_therview',views.approved_therview,name='approved_therview'),
    
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),

    path('updatether',views.updatether,name='updatether'),
    path('updatetecher/<int:teid>',views.updatetecher,name='updatetecher'),

    
    path('test',views.test,name='test'),  


]
