from django.shortcuts import render
from django.views import generic

from blog.models import Post

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
