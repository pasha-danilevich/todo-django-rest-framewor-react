
from django.urls import path
from . import views

# 'List':         '/task-list/',
# 'Detail View':  '/task-detail/<int:pk>/',
# 'Create':       '/task-create/',
# 'Update':       '/task-update/<int:pk>/',
# 'Delete':       '/task-delete/<int:pk>/',

urlpatterns = [
    path('', views.api_overview, name='api-overview'),

    path('task-list/', views.task_list, name='task-list'),
    path('task-details/<int:pk>', views.task_details, name='task-details'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<int:pk>', views.task_update, name='task-update'),
    path('task-delete/<int:pk>', views.task_delete, name='task-delete'),
]
