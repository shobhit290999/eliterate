from django import forms
from ckeditor.fields import RichTextFormField

class Blog(forms.Form):
    title = forms.CharField(max_length=200)
  
    post = RichTextFormField()

  