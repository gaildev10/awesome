from django import forms
from .models import *


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags', 'image']
        labels = {
            'body' : 'Caption',
            'tags' : 'Category',
            'image' : 'Upload Image',
        }

        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
            # 'url' : forms.TextInput(attrs={'placeholder': 'Add url ...'}),
            'tags' : forms.CheckboxSelectMultiple(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body' : '',
            'tags' : 'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add comment...', 'size': 60 })
            }
        labels = {
            'body' : ''
        }

class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add reply...', 'class': "!text-sm", 'size': 60 })
            }
        labels = {
            'body' : ''
        }
