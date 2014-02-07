from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from profiles.models import Profile

def index(request):
	profile_list = Profile.objects.all()
	context = {'profile_list': profile_list}
	return render(request, 'profiles/index.html', context)

class DetailedProfile(DetailView):
	model = Profile
	template_name = 'detail.html'

class CreateAProfile(CreateView):
	model = Profile
	template_name = 'edit.html'

	def get_success_url(self):
		return reverse('index')
	def get_context_data(self, **kwargs):
		context = super(CreateAProfile, self).get_context_data(**kwargs)
		context['action'] = reverse('create')
		return context

class DeleteAProfile(DeleteView):
	model = Profile
	template_name = 'delete.html'

	def get_success_url(self):
		return reverse('index')

class EditAProfile(UpdateView):
	model = Profile
	template_name = 'edit.html'

	def get_success_url(self):
		return reverse('index')
	def get_context_data(self, **kwargs):
		context = super(EditAProfile, self).get_context_data(**kwargs)
		context['action'] = reverse('edit', kwargs={'pk': self.get_object().id})
		return context
