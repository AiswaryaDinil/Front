from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from frontapp.models import*
from django.views.generic import TemplateView,FormView,CreateView
from django.contrib.auth import authenticate,login
from frontapp import forms
from django.contrib.auth.models import User,Permission

class LoginView(FormView):
    template_name = "index.html"
    form_class = forms.LoginForm
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            uname = User.objects.get(email=email)
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname,password=pwd)
            login(request, user)
            if request.user.is_superuser:
                return redirect("dashboard")
            else:
                return render(request, "index.html", {"form": form})

class IndexView(TemplateView):
    template_name = "dashboard.html"
class UserRoleView(TemplateView):
    template_name = "userandroles.html"
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        all_users=Useradd.objects.all()
        context["users"]=all_users
        return context
class CreateUserView(CreateView):
    model = Useradd
    form_class = forms.CreateUserForm
    template_name = "useradd.html"
    success_url = reverse_lazy("userrole")
    context_object_name = "users"
    def form_valid(self,form):
        return super().form_valid(form)



