#from django.urls import path

#from .views import TaskListView, TaskCreateView, TestView

#urlpatterns = [
#    path("",TaskListView.as_view(),name="task_list"),
#    path("create/", TaskCreateView.as_view(), name="task_create"),
#    path("test/", TestView, name="test_view"),
#]

from django.urls import path
from .views import TaskListView, TaskCreateView, TestView, ContactListView, ContactCreateView
from .views import ContactDetailView, ContactDeleteView
from .views import ContactUpdateView


urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),  # This is the start page with an empty contact list
    path("create/", ContactCreateView.as_view(), name="contact_create"),  # URL for creating a new contact
    path("tasks/", TaskListView.as_view(), name="task_list"),  # Existing TaskListView
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),  # Existing TaskCreateView
    path("test/", TestView, name="test_view"),  # Existing TestView
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),

]

