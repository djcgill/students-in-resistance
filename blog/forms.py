from django import forms

from blog.models import Post, PostImage, Issue, Category

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label = 'Title')
    body = forms.Textarea()

    class Meta:
        model = Post
        fields = ('title', 'body', 'issue', 'category', )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['issue'] = forms.ModelChoiceField(queryset=Issue.objects.order_by('issue_number').values_list('issue_number'))
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.order_by('name').values_list('name'))

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    
    class Meta:
        model = PostImage
        fields = ('image', )
