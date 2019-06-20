from django.contrib import messages
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.models import Post, PostImage
from blog.forms import PostForm, ImageForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
	    '''Return last five blog posts'''
	    return Post.objects.order_by('-published_date')[:5]

class DetailView(generic.DetailView):
	model = Post
	template_name = 'blog/detail.html'

class AboutView(generic.TemplateView):
	template_name = 'blog/about.html'

class TeamView(generic.TemplateView):
	template_name = 'blog/team.html'

class DownloadsView(generic.TemplateView):
	template_name = 'blog/downloads.html'

class ContactView(generic.TemplateView):
	template_name = 'blog/contact.html'

class ContribView(generic.TemplateView):
	template_name = 'blog/contributors.html'

def post(request):
	"""Handles new blog posts"""
	ImageFormSet = modelformset_factory(PostImage, form=ImageForm, extra=1)

	if request.method == 'POST':
		postForm = PostForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES,
							   queryset=PostImage.objects.none())
		
		if postForm.is_valid() and formset.is_valid():
			post_form = postForm.save(commit=False)
			#TODO: Change when users are implemented
			post_form.user = 'Admin'
			post_form.save()

			for form in formset.cleaned_data:
				if form:
					image = form['image']
					post_picture = PostImage(post=post_form, image=post_picture)
			messages.success(request, "Post successfully added")
			return HttpResponseRedirect('/')
	else:
		postForm = PostForm()
		formset = ImageFormSet(queryset=PostImage.objects.none())
	return render(request, 
					'blog/post.html', 
					{'postForm': postForm, 'formset': formset})

