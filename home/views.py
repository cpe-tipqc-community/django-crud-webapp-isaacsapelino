from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from login.models import Profile
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
# Create your views here.

@login_required(login_url='/')
def home(request):
	content = {
		'posts' : Post.objects.all()
	}
	return render(request, 'home.html', content)

class PostListView(LoginRequiredMixin, ListView):
	login_url = '/logout/'
	redirect_field_name = 'logout'

	model = Post
	template_name='home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile_user'] = Profile.objects.get(id=self.request.user.id)
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['category', 'title', 'post']

	def form_valid(self, form):
		form.instance.author = Profile.objects.get(id=self.request.user.id)
		return super().form_valid(form)
	
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['category', 'title', 'post']

	def form_valid(self, form):
		form.instance.author = Profile.objects.get(id=self.request.user.id)
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if Profile.objects.get(id=self.request.user.id) == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = 'home'

	def test_func(self):
		post = self.get_object()
		if Profile.objects.get(id=self.request.user.id) == post.author:
			return True
		else:
			return False