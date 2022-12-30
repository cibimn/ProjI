from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin
from vow.models import organization,Agent
import random
from django.core.mail import send_mail
# Create your views here.

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name= "agents/agent_list.html"
    def get_queryset(self):
        organization = self.request.user.organization_id
        return Agent.objects.filter(organization_id=organization)
    

class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def form_valid(self, form):
        agen = form.save(commit=False)
        agen.is_agent = True
        agen.set_password(f"{random.randint(0, 1000000)}")
        agen.save()
        Agent.objects.create(
            user=agen,
            organization_id=self.request.user.organization_id
        )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on ProjectI. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[agen.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name= "agents/agent_detail.html"
    context_object_name= "agent"
    
    def get_queryset(self):
        organization = self.request.user.organization_id
        return Agent.objects.filter(organization_id=organization)
    
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    
    def get_queryset(self):
        organization = self.request.user.organization_id
        return Agent.objects.filter(organization_id=organization)
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name= "agent"
    
    def get_queryset(self):
        organization = self.request.user.organization_id
        return Agent.objects.filter(organization_id=organization)