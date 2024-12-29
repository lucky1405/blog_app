from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from django.views.generic import DeleteView, CreateView
from django.shortcuts import get_object_or_404
from myblog.models import Profile

# Create your views here.
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_link','facebook_link','twitter_link','instagram_link']
    success_url = reverse_lazy('home')

class ShowProfilePageView(DeleteView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class UserRgisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
