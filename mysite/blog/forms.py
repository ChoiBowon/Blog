from django import forms
from blog.models import Blog

# class BlogUploadForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.CharField
#     thumbnail = forms.ImageField

class BlogUploadForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields = '__all__'
        exclude = ['user']
