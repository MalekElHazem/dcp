from django.urls import path
from django.urls.conf import include
from manage_club import views



urlpatterns = [
    path('', views.index),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('login', views.login),
    path('loginaction/', views.loginaction),
    path('events/', views.events),
    path('members/', views.members),
    path('add_event/', views.add_event),
    path('edit_event/<int:id>', views.edit_event),
    path('update_event/<int:id>', views.update_event),
    path('delete_event/<int:id>', views.destroy_event),
    path('event_details/<int:id>', views.event_details, name='event_details'),
    path('layout', views.layout),
    path('take_attendance/<int:event_id>', views.take_attendance, name='take_attendance'),
    path('create_task/<int:event_id>', views.create_task, name='create_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('edit_attendance/<int:id>', views.edit_attendance, name='edit_attendance'),
    path('delete_attendance/<int:id>', views.delete_attendance, name='delete_attendance'),
    path('update_attendance/<int:id>', views.update_attendance),
]