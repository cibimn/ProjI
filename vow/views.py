import logging
import datetime
from django import contrib
from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from .serializers import customerserializers
from .pagination import StandardResultsSetPagination
# from vow.mixins import OrganisorAndLoginRequiredMixin
from .models import *
from .forms import CustomerUpdateForm, VowUpdateForm, LoginForm
# Create your views here.
logger = logging.getLogger(__name__)


class LandingPageView(generic.TemplateView):
    template_name= "landing.html"

class WelcomePageView(generic.TemplateView):
    template_name= "welcome-user.html"


class DashboardPageView(generic.TemplateView):
    
    template_name= "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(DashboardPageView, self).get_context_data(**kwargs)
        
        if self.request.GET.get('std') and self.request.GET.get('sec'):
            pass
        else:
            pass
        context.update({})
        return context
########Customer Class View#################
#CustomerCreate View
# class CustomerListView(LoginRequiredMixin,generic.ListView):
#     template_name= "customers/customers_list.html"
    
#     context_object_name= "Custom"
    
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_organisor:
#             queryset = customers.objects.filter(organization_id=self.request.user.organization_id)
#         else:
#             queryset = customers.objects.filter(agent__user=user)
#             queryset = queryset.filter(agent__user=user)
#         # queryset= customers.objects.all()
#         # if self.request.user.is_agent():
        
#         return queryset
def customerlist(request):
	return render(request, "customers/customers_list.html", {})

class CustomerListView(LoginRequiredMixin, ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = customerserializers

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = customers.objects.filter(organization_id=self.request.user.organization_id)
        else:
            queryset = customers.objects.filter(agent__user=user)
            queryset = queryset.filter(agent__user=user)
        # queryset = queryset.only("name","phone","classes_std","classes_sec")
        classes_std = self.request.query_params.get('classes_std', None)
        classes_sec = self.request.query_params.get('classes_sec', None)
        name = self.request.query_params.get('name', None)
        if classes_std:
            queryset = queryset.filter(classes__std=classes_std)
        if classes_sec:
            queryset = queryset.filter(classes__sec=classes_sec)
        if name:
            queryset = queryset.filter(name = name)
            # print(queryset)
        # queryset= customers.objects.all()
        # if self.request.user.is_agent():
        
        return queryset
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getClassesSTD(request):
    # get all the countreis from the database excluding 
    # null and blank values
    if request.method == "GET" and is_ajax(request=request):
        user = request.user
        
        queryset = classes.objects.filter(agent__user=user)

        classe = queryset.exclude(std__isnull=True).\
            exclude(std__exact='').values_list('std').distinct()
        classe = [f'{i[0]}' for i in list(classe)]
        data = {
            "classes": classe, 
        }
        return JsonResponse(data, status = 200)

def getClassesSec(request):
    # get all the countreis from the database excluding 
    # null and blank values
    if request.method == "GET" and is_ajax(request=request):
        user = request.user
        
        queryset = classes.objects.filter(agent__user=user)

        classe = queryset.exclude(sec__isnull=True).\
            exclude(sec__exact='').values_list('sec').distinct()
        classe = [f'{i[0]}' for i in list(classe)]
        data = {
            "classes": classe, 
        }
        return JsonResponse(data, status = 200)

def getName(request):
    # get all the countreis from the database excluding 
    # null and blank values
    if request.method == "GET" and is_ajax(request=request):
        user = request.user
        if user.is_organisor:
            queryset = customers.objects.filter(organization_id= request.user.organization_id)
        else:
            queryset = customers.objects.filter(agent__user=user)
            queryset = queryset.filter(agent__user=user)
        # print(queryset)
        name = queryset.exclude(name__isnull=True).\
            exclude(name__exact='').order_by('name').values_list('name').distinct()
        # print(name)
        name = [i[0] for i in list(name)]
        data = {
            "name": name, 
        }
        return JsonResponse(data, status = 200)


#CustomerDetail View        
class CustomerDetailView(LoginRequiredMixin,generic.DetailView):
    template_name= "customers/customer_detail.html"
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organisor:
            queryset = customers.objects.filter(organization_id=self.request.user.organization_id)
        else:
            queryset = customers.objects.filter(agent__user=user)
            
        return queryset
    context_object_name= "customer"

#CustomerUPdateView
class CustomerUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "customers/customer_update.html"
    form_class = CustomerUpdateForm
    
    def get_queryset(self):
        user = self.request.user
        return customers.objects.filter(organization_id=self.request.user.organization_id)
    
    context_object_name = "customer_update"
    
    def get_success_url(self):
        return reverse("I:customers-list")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this Customer")
        return super().form_valid(form)
##################################################


########Affirmation Class View########################


class AffirmationListView(LoginRequiredMixin,generic.ListView):
    template_name= "vow/Affirmations_list.html"
    
    context_object_name= "affirmation"
    
    def get_queryset(self):
        queryset= VOW.objects.all()
        print(queryset,"queryset")
        # if self.request.user.is_agent:
        #     queryset = queryset.filter(agent__user=self.request.user)
        return queryset

class AffirmationCreateView(LoginRequiredMixin,generic.CreateView):
    template_name= "vow/Affirmations_create.html"
    form_class = VowUpdateForm
    
    def get_success_url(self):
        return reverse("I:affirmation-list")
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         print("successfully created")
    #         # Process the form data
    #         ...
    #         return redirect(self.get_success_url())
    #     else:
    #         print(form.errors)
    #         print("fail; created")
    #         return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.datetime.today()
        print(datetime.datetime.today(),"date")
        return context
class AffirmationDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name= "vow/Affirmations_delete.html"
    queryset = VOW.objects.all()
    
    def get_success_url(self):
        return reverse("I:affirmation-list")
    

class AffirmationDetailView(LoginRequiredMixin,generic.DetailView):
    template_name= "vow/Affirmations_detail.html"
    
    def get_queryset(self):
        user = self.request.user
        queryset = VOW.objects.filter(agent__user=user)
        return queryset
    
    context_object_name= "affirmation"

class AffirmationUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "vow/Affirmations_update.html"
    form_class = VowUpdateForm
    
    def get_queryset(self):
        user = self.request.user
        return VOW.objects.filter(agent__user=user)
    
    context_object_name = "affirmation_update"
    
    def get_success_url(self):
        return reverse("I:affirmation-list")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this Affirmation")
        return super(VowUpdateForm, self).form_valid(form)

####################################################


#############Category View #################




###########################################
def landing_page(request):
    return render(request, "landing.html")

########Customer#################

def Customer_List(request):
    customer_list = customers.objects.all()
    context = {
        "Custom": customer_list
    }
    return render(request, "customers/customers_list.html", context)

def Customer_Detail(request, pk):
    customer_detail = customers.objects.get(id=pk)
    context = {
        "customer": customer_detail
    }
    return render(request, "customers/customer_detail.html", context)

def customer_create(request):
    return render(request, "customers/customer_create.html")


def customer_update(request, pk):
    customer_update = customers.objects.get(id=pk)
    form = CustomerUpdateForm(instance=customer_update)
    if request.method == "POST":
        form = CustomerUpdateForm(request.POST, instance=customer_update)
        if form.is_valid():
            form.save()
            return redirect("/I/customers")
    context = {
        "form": form,
        "customer_update": customer_update
    }
    return render(request, "customers/customer_update.html", context)

def customer_delete(request, pk):
    if request.user.is_organisor:
        customer_delete = customers.objects.get(id=pk)
        customer_delete.delete()
        return redirect("/I/customers")
    else:
        customer_delete = customers.objects.get(id=pk)
        customers.objects.filter(id=pk).update(agent=1)
        return redirect("/I/customers")

def Affirmation_list(request):
    Affirmations_list = VOW.objects.all()
    context = {
        "Affirmations_list": Affirmations_list
    }
    return render(request, "vow/Affirmations_list.html", context)

def Affirmation_Detail(request, pk):
    affirmation_detail = VOW.objects.get(id=pk)
    context = {
        "affirmation": affirmation_detail
    }
    return render(request, "vow/Affirmations_detail.html", context)

def Affirmation_create(request):
    form = VowUpdateForm()
    if request.method == "POST":
        form = VowUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/I/affirmations")
    context = {
        "form": form
    }
    return render(request, "vow/Affirmations_create.html", context)

def Affirmation_update(request, pk):
    affirmation_update = VOW.objects.get(id=pk)
    form = VowUpdateForm(instance=affirmation_update)
    if request.method == "POST":
        form = VowUpdateForm(request.POST, instance=affirmation_update)
        if form.is_valid():
            form.save()
            return redirect("/I/affirmations")
    context = {
        "form": form,
        "affirmation_update": affirmation_update
    }
    return render(request, "vow/Affirmations_update.html", context)

def Affirmation_delete(request, pk):
    affirmation_delete = VOW.objects.get(id=pk)
    affirmation_delete.delete()
    return redirect("/I/affirmations")