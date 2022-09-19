from .models import Experiments
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "diy/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('exp_list')

class ExpList(LoginRequiredMixin, ListView):
    model = Experiments
    context_object_name= "exp_list"
    template_name = "diy/experiments_list.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['exp_list'] = context['exp_list'].filter(user=self.request.user)
    #     return context

class ExpDetail(LoginRequiredMixin, DetailView):
    context_object_name= "experiment"
    model = Experiments
    template_name = "diy/experiment.html"

class ExpCreate(LoginRequiredMixin, CreateView):
    model = Experiments
    fields = ['exp_name', 'description', 'difficulty', 'subject', 'image', 'safety', 'steps']
    success_url = reverse_lazy('exp_list')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(ExpCreate, self).form_valid(form)

class ExpUpdate(LoginRequiredMixin, UpdateView):
    model = Experiments 
    fields = ['exp_name', 'description', 'difficulty', 'subject', 'image', 'safety', 'steps']
    success_url = reverse_lazy('exp_list')

class ExpDelete(LoginRequiredMixin, DeleteView):
    model = Experiments
    context_object_name= "experiment"   
    success_url = reverse_lazy('exp_list')


class Student_list(ListView):
    model = Experiments
    template_name = "diy/student_list.html"
    context_object_name = "exp_list"

    ordering = ['-claps']

class Student_Detail(DetailView):
    model = Experiments
    template_name = "diy/student_detail.html"
    context_object_name = "experiment"

@csrf_exempt
def clap(request, pk):
    if request.method == 'POST':
        model = Experiments.objects.get(id=pk)
        model.claps += 1
        model.save()
        content='Liked'
        return JsonResponse(content, safe=False)