from django.urls import path
from .views import *


urlpatterns = [
    path('',index),
    path('index/',index),
    path('aboutus/',aboutus),
    path('bca/',bca),
    path('read/',read),
    path('faculty_record/',faculty_record),
    path('login/', Login),
    path('admin_s/',admin_s),
    path('update/',update),
    path('create/',create),
    path('update/<int:id>/', update),
    path('delete/<int:id>/',Delete),
    path('login_h/', login_h),
    path('l_read/',l_read),
    path('l_record/',l_record),
    path('feedback_u/',feedback_u),
    path('f_read/',f_read),
    path('f_record/',f_record),
    path('sem1/',sem1),
    path('sem2/',sem2),
    path('sem3/',sem3),
    path('sem4/',sem4),
    path('sem5/',sem5),
    path('sem6/',sem6),
    path('s_create/',s_create),
    path('s_read/',s_read),
    path('s_update/<int:id>/',s_update),
    path('c/',c),
    path('s_record/',s_record),
    path('sem_record/',sem_record),
    path('se_create/',se_create),
    path('se_record/',se_record),
    path('div_create/', div_create),
    path('div_record/', div_record),
    path('faculty_index/',faculty_index),
    path('f_login/',f_login),
    path('f_feedback/',f_feedback),
    path('f_sem/',f_sem),
    path('f_student/',f_student),
    path('f_subject/',f_subject),
    path('div_sem/',div_sem),
    path('div_course/',div_course),
    path('logout/',logout),
    path('faculty_logout/',faculty_logout),
    path('faculty_login/',faculty_login),
    path('faculty_div1/',faculty_div1),
    path('faculty_div2/',faculty_div2),
    path('delete_d/<int:id>/', Delete_d),
    path('delete_di/<int:id>/', Delete_di),
    path('delete_su/<int:id>/', Delete_su),
    path('delete_sub/<int:id>/', Delete_sub),
    path('delete_s/<int:id>/', Delete_s),
    path('delete_se/<int:id>/', Delete_se),

]