from django.urls import path
from Base import views
from .views import get_students
from Base import Studentviews




urlpatterns = [
    
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('api/teachers/', views.get_teachers, name='get_teachers'),
    path('api/staff/', views.get_staff, name='get_staff'),
    path('api/students/',get_students,name ='get_students'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('home/', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', Studentviews.student_list, name='student_list'),
    path('add_teacher/',views.add_teacher, name = 'add_teacher'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('add_staff/',views.add_staff, name = 'add_staff'),
    path('staff_list/', views.staff_list, name='staff_list'),
    path('student_info/<int:pk>/', views.student_info, name='student_info'),
    path('attendance/<int:pk>/',views.attendance,name='attendance'),
    path('marks/<int:pk>/',views.marks,name='marks'),
    path('fees/<int:pk>/',views.fees,name='fees'),
    path('schools/',views.schools,name='schools'),
    path('add_schools/',views.add_schools,name='add_schools'),
    path('schools_list/',views.schools_list,name='schools_list')
    
   


]

