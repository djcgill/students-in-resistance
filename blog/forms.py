from django import forms

from blog.models import Post, PostImage, Issue, Category

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label = 'Title')
    body = forms.Textarea()
    issue = forms.ModelChoiceField(queryset=Issue.objects.all(), to_field_name='issue_number')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='name')

    class Meta:
        model = Post
        fields = ('title', 'body', 'issue', 'category', )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    
    class Meta:
        model = PostImage
        fields = ('image', )
