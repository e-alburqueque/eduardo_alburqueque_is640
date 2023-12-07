from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic import DetailView, DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from tasks.forms import ContactForm


# Create your views here.
from .models import Task

from.task_form import TaskForm

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")



def TestView(request):  
    # You can pass data to the template if needed    
    context = {'message': 'Hello from custom view!'}     
    return render(request, 'tasks/test_view.html', context)


from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'tasks/contact_list.html'  # Specify your template name

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'notes']  # Specify the fields you want to include in your form
    template_name = 'tasks/contact_form.html'  # Specify your template name
    success_url = reverse_lazy('contact_list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'tasks/contact_detail.html'  # You need to create this template

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'tasks/contact_confirm_delete.html'  # You need to create this template
    success_url = reverse_lazy('contact_list')

    

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'tasks/contact_form.html'  # Reuse the form template
    success_url = reverse_lazy('contact_list')
